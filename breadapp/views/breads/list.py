import sqlite3
from django.shortcuts import render, redirect, reverse
from breadapp.models import Bread
from breadapp.models import model_factory
from ..connection import Connection


def bread_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:

            conn.row_factory = model_factory(Bread)

            db_cursor = conn.cursor()
            db_cursor.execute("""
            SELECT * FROM breadapp_bread
            ORDER BY name ASC 
            """)

            all_breads = db_cursor.fetchall()

        template = 'breads/list.html'
        context = {
            'all_breads': all_breads
        }

        return render(request, template, context)
    
    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO breadapp_bread
            (
                name, region
            )
            VALUES (?, ?)
            """,
            (form_data['name'], form_data['region']))

        return redirect(reverse('breadapp:bread_list'))