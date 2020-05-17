import sqlite3
from ...connection import Connection
from breadapp.models import model_factory, BreadIngredient


def get_bread_ingredients(bread_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(BreadIngredient)

        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
        bi.id,
        bi.amount,
        bi.bread_id,
        bi.ingredient_id,
        i.name
        FROM breadapp_breadingredient bi
        LEFT JOIN breadapp_ingredient i on bi.ingredient_id = i.id
        WHERE bi.bread_id = ?
        """, (bread_id, ))

        dataset = db_cursor.fetchall()
        ingredient_list = []
        for item in dataset:
            ingredient_list.append(item)
        return ingredient_list