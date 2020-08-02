#!/usr/bin/env python3
import sqlite3


class SQL:
    '''
    Base SQL class to CRUD a SQLite database.
    '''
    result = []

    def connect(self):
        connection = sqlite3.connect('dataset.db')
        cursor = connection.cursor()
        return connection, cursor

    def createTable(self):
        connection, cursor = self.connect()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS dataset (
                id INTEGER,
                title TEXT,
                equation TEXT
        )''')
        connection.commit()
        connection.close()

    def insertEntry(self, id, title, equation):
        connection, cursor = self.connect()
        cursor.execute('''INSERT INTO dataset VALUES (?,?,?)''', (id, title, equation))
        result = cursor.fetchall()
        connection.commit()
        connection.close()
        return result

    def readEntry(self, id):
        connection, cursor = self.connect()
        cursor.execute('''SELECT * FROM dataset WHERE id=?''', (id,))
        result = cursor.fetchall()
        connection.commit()
        connection.close()
        return result

    def updateEntry(self, id, title, equation):
        connection, cursor = self.connect()
        cursor.execute('''UPDATE dataset SET title=?, equation=? WHERE id=?''', (title, equation, id))
        result = cursor.fetchall()
        connection.commit()
        connection.close()
        return result

    def deleteEntry(self, id):
        connection, cursor = self.connect()
        cursor.execute('''DELETE FROM dataset WHERE id=?''', (id))
        result = cursor.fetchall()
        connection.commit()
        connection.close()
        return result

    def showAllEntries(self):
        connection, cursor = self.connect()
        cursor.execute('''SELECT rowid,* FROM dataset''')
        result = cursor.fetchall()
        connection.commit()
        connection.close()
        return result

    def query(self, query, data=None):
        connection, cursor = self.connect()
        if data:
            cursor.execute(f'''{query}''', data)
        else:
            cursor.execute(f'''{query}''')
        result = cursor.fetchall()
        connection.commit()
        connection.close()

    def outCsv(self):
        pass


if __name__ == '__main__':
    sql = SQL()
    '''
    NOTE: Run this only once! Comment it out after that.
    Creates a SQLite database from JSON file.
    (dataset.json -> dataset.db)
    Modify variables to fit a different JSON file.
    '''
    # sql.createTable()
    # import requests
    # response = requests.get('https://crtejaswi.github.io/API/latex1.json')
    # entries = response.json()
    # for entry in entries:
    #     sql.insertEntry(entry['id'], entry['title'], entry['equation'])
