#!/usr/bin/env python3
import sqlite3
from datetime import datetime
from flask import Flask, render_template, g, request
app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods=['GET', 'POST'])
def index():
    db = get_db('food.db')
    cursor = db.cursor()

    if request.method == 'POST':
        date = request.form['date']                         # assuming YYYY-MM-DD format
        cursor.execute("INSERT INTO log_date (entry_date) values(?)", [date])
        db.commit()
        try:
            date = datetime.strptime(date, '%Y-%m-%d')      # assuming YYYY-MM-DD format
            date = datetime.strftime(date, '%d %B, %Y')     # assuming DD Month, YYYY format
            # return f'Entered Time: {date}'
        except Exception as error:
            print(error)

    cursor.execute("SELECT entry_date FROM log_date ORDER BY entry_date DESC")
    entries = cursor.fetchall()
    results = []
    for entry in entries:
        try:
            date = {}
            x = datetime.strptime(str(entry['entry_date']), '%Y-%m-%d')
            date['entry_date'] = datetime.strftime(x, '%d %B, %Y')
            results.append(date)
        except Exception as error:
            print(error)
    return render_template('home.html', results=results)


@app.route('/view/<date>')
def view(date):
    db = get_db('food.db')
    cursor = db.cursor()
    cursor.execute("SELECT entry_date from log_date WHERE entry_date = ? ", [date])
    result = cursor.fetchone()
    # return f'''Entered Date: {result['entry_date']}'''
    return render_template('day.html')


@app.route('/food', methods=['GET', 'POST'])
def food():
    db = get_db('food.db')
    cursor = db.cursor()

    if request.method == 'POST':

        data = request.form.to_dict()
        name = data['food-name']
        protein = int(data['protein'])
        carbohydrates = int(data['carbohydrates'])
        fat = int(data['fat'])
        calories = 4 * protein + 4 * carbohydrates + 9 * fat

        cursor.execute("INSERT INTO food (name, protein, carbohydrates, fat, calories) values(?,?,?,?,?)",
                       [name, protein, carbohydrates, fat, calories])
        db.commit()
        # return f'Entered Record: {data}'

    cursor.execute("SELECT * FROM food")
    results = cursor.fetchall()
    return render_template('add_food.html', results=results)


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
