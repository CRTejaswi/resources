#!/usr/bin/env python3
import sqlite3
from datetime import datetime
from flask import Flask, render_template, g, request
app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods=['GET', 'POST'])
def index():
    # db = get_db('food.db')
    # cursor = db.cursor()
    # cursor.execute("SELECT entry_date FROM log_date ORDER BY entry_date DESC")
    # entries = cursor.fetchall()
    return '''<h1>Test Page<h1>'''


'''
Database Implementation
    Query a list of books from database
'''


def connect_db(filename):
    connection = sqlite3.connect(filename)
    connection.row_factory = sqlite3.Row    # Return dict instead of list
    return connection


def get_db(filename):
    if not hasattr(g, 'db'):
        g.db = connect_db(filename)
    return g.db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'db'):
        g.db.close()


if __name__ == '__main__':
    app.run()
