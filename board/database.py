import sqlite3
import click
from flask import current_app, g

def init_app(app):
    app.cli.add_command(init_db_command)

@click.command("init-db")
def init_db_command():
    db = get_db()

def get_db():
    pass