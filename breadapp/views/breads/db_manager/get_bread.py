import sqlite3
from ...connection import Connection
from breadapp.models import model_factory, Bread
def get_bread(bread_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Bread)

        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
        b.id,
        b.name,
        b.region
        FROM breadapp_bread b
        WHERE b.id = ?
        """, (bread_id, ))

        dataset = db_cursor.fetchone()

        return dataset

