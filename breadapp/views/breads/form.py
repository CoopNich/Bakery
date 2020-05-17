import sqlite3
from django.shortcuts import render
from breadapp.models import Bread
from breadapp.models import model_factory
from .db_manager.get_bread import get_bread
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
        breads = get_breads()
        template = 'breads/form.html'
        context = {
        }

        return render(request, template, context)

def bread_edit_form(request, bread_id):

    if request.method == 'GET':
        bread = get_bread(bread_id)

        template = 'breads/form.html'
        context = {
            'bread': bread
        }

        return render(request, template, context)