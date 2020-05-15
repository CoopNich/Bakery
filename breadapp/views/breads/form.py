import sqlite3
from django.shortcuts import render
from breadapp.models import Bread
from breadapp.models import model_factory
from ..connection import Connection


def get_breads():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Bread)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT * FROM breadapp_bread 
        """)

        return db_cursor.fetchall()

def bread_form(request):
    if request.method == 'GET':
        libraries = get_breads()
        template = 'breads/form.html'
        context = {
        }

        return render(request, template, context)