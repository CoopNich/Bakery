import sqlite3
from django.shortcuts import render, redirect, reverse
from .db_manager.get_bread import get_bread
from .db_manager.get_bread_ingredients import get_bread_ingredients
from ..connection import Connection

def bread_details(request, bread_id):
    if request.method == "GET":
        bread = get_bread(bread_id)
        bread_ingredients = get_bread_ingredients(bread_id)
        template = "breads/details.html"

        context = {
            "bread_ingredients": bread_ingredients,
            "bread": bread
        }

        return render(request, template, context)


    elif request.method == 'POST':
        form_data = request.POST
        
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                UPDATE breadapp_bread
                SET name = ?,
                    region = ?
                WHERE id = ?
                """,
                (
                    form_data['name'], form_data['region'],
                     bread_id,
                ))


            return redirect(reverse('breadapp:bread_list'))


        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                DELETE FROM breadapp_breadingredient
                WHERE id = ?
                """, (bread_id,))

            return redirect(reverse('breadapp:bread_list'))