import sqlite3

from app_site import app


def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row  # данные из БД представленны в виде словаря
    return conn


def create_db():
    db = connect_db()
    with app.open_resource('db_schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


# create_db()
