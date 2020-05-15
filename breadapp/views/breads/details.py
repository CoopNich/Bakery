import sqlite3
from django.shortcuts import render, redirect, reverse
from .db_manager.get_bread import get_bread
from .db_manager.get_bread_ingredients import get_bread_ingredients
from ..connection import Connection

def bread_details(request, bread_id):
    if request.method == "GET":
        bread = get_bread(bread_id)
        bread_ingredients = [i.ingredient for i in get_bread_ingredients(bread_id)]
        template = "breads/details.html"

        context = {
            "bread_ingredients": bread_ingredients,
            "bread": bread
        }

        return render(request, template, context)