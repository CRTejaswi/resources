    Copyright(c) 2019-
    Author: Chaitanya Tejaswi (github.com/CRTejaswi)    License: GPL v3.0+


# Python3
> Personal notes for Python3 language.


# Index

- [Data Structures & Algorithms](#data-structures-algorithms)
- [CLI/GUI](#cligui)
- [Databases](#databases)
- [Processing: Text](#text-processing)
- [Processing: File](#file-processing)
- [Processing: Image](#image-processing)
- [Unsorted](#Unsorted)

## Data Structures & Algorithms
Review: [DSA](dsa/DSA.md)

## CLI/GUI

Review: [argparse](argparse/argparse.md), [Tkinter](tkinter/tkinter.md).

## Databases

### SQLite

__CRUDing A Database__ <br>

- A database can be of type `:memory:` or `file.db`. <br>
`:memory:` is stored on RAM, and creates a new database on every execution. <br>
`file.db` is a file stored on harddrive. <br>
The former is useful when testing code to avoid loss of data. <br>
- The steps to manage a database are:
    1. Create a connection to database.
    2. Create a cursor to execute SQL commands.
    3. Make changes to, or query the database.
    4. Commit changes to database.
    5. Close the connection to database.

__Table Insertions__ [\*](https://www.youtube.com/watch?v=pd-0G0MigUA&t=490s) <br>

- [x] Explicit Insertions

``` py
import sqlite3


connection = sqlite3.connect(':memory:')
cursor = connection.cursor()

cursor.execute(""" create table employees (
                    fname text,
                    lname text,
                    pay integer
                    )""")

cursor.execute("INSERT INTO employees VALUES ('John', 'Doe', 50000)")
cursor.execute("INSERT INTO employees VALUES ('Mary', 'Jane', 70000)")
cursor.execute("INSERT INTO employees VALUES ('George', 'Doe', 35000)")
cursor.execute("INSERT INTO employees VALUES ('Josie', 'Jane', 37000)")

cursor.execute("SELECT * FROM employees WHERE lname='Doe'")
print(cursor.fetchall())

connection.commit()
connection.close()
```
```
[('John', 'Doe', 50000), ('George', 'Doe', 35000)]
```

- [x] Implicit Insertions

``` py
# employee.py
class Employee:
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay

    @property
    def email(self):
        return '{}_{}@email.com'.format(self.fname, self.lname)

    @property
    def name(self):
        return '{} {}'.format(self.fname, self.lname)

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.fname, self.lname, self.pay)
```
``` py
import sqlite3
from employee import Employee

connection = sqlite3.connect(':memory:')
cursor = connection.cursor()

cursor.execute(""" create table employees (
                    fname text,
                    lname text,
                    pay integer
                    )""")

emp1 = Employee('John', 'Doe', 50000)
emp2 = Employee('Mary', 'Jane', 70000)
emp3 = Employee('George', 'Doe', 35000)
emp4 = Employee('Josie', 'Jane', 37000)

cursor.execute("INSERT INTO employees VALUES (?,?,?)", (emp1.fname, emp1.lname, emp1.pay))
cursor.execute("INSERT INTO employees VALUES (?,?,?)", (emp2.fname, emp2.lname, emp2.pay))
cursor.execute("INSERT INTO employees VALUES (:fname, :lname, :pay)", {'fname': emp3.fname, 'lname': emp3.lname, 'pay': emp3.pay})
cursor.execute("INSERT INTO employees VALUES (:fname, :lname, :pay)", {'fname': emp4.fname, 'lname': emp4.lname, 'pay': emp4.pay})

cursor.execute("select * from employees where lname='Doe'")
print(cursor.fetchall())

connection.commit()
connection.close()
```
```
[('John', 'Doe', 50000), ('George', 'Doe', 35000)]
```

__Create a custom SQLite Shell__ <br>

``` py
import sqlite3


connection = sqlite3.connect(":memory:")
connection.isolation_level = None
cursor = connection.cursor()
buffer = ""

print('>> SQLite: (Blank Line to exit)')
while True:
    line = input()
    if line == "":
        break
    buffer += line
    if sqlite3.complete_statement(buffer):
        try:
            buffer = buffer.strip()
            cursor.execute(buffer)
            if buffer.lstrip().upper().startswith("SELECT"):
                print(cursor.fetchall())
        except sqlite3.Error as error:
            print("ERROR: ", error.args[0])
        buffer = ""
conection.close()
```
```
>> SQLite: (Blank Line to exit)
CREATE TABLE books (title TEXT, isbn INTEGER, pages INTEGER);
INSERT INTO books VALUES ('Book Name', 6549825563, 256);
SELECT * FROM books;
[('Book Name', 6549825563, 256)]
```

__Templates__ <br>

- This uses multiple methods to represent individual queries to a DB. Helpful when solving a multi-part problem.

```py
#!/usr/bin/env python3
import sqlite3


class SQL:

    def connect(self):
        connection = sqlite3.connect('sample.db')
        cursor = connection.cursor()
        return connection, cursor

    def Q1(self):
        connection, cursor = self.connect()
        cursor.execute('''SELECT transactions.cust_id, segments.seg_name, segments.update_at
            FROM transactions
                INNER JOIN segments
                ON transactions.cust_id=segments.cust_id
            WHERE active_flag="N"
            ORDER BY update_at''')
        print(cursor.fetchone())
        connection.commit()
        connection.close()

    def Q2(self):
        connection, cursor = self.connect()
        cursor.execute('''SELECT DISTINCT products.prod_id, products.prod_name, count(transactions.trans_id) as count
                FROM products
                    INNER JOIN transactions
                    ON products.prod_id = transactions.prod_id
                WHERE transactions.trans_dt BETWEEN "2016-01-01" AND "2016-05-01"
                GROUP BY transactions.trans_dt, products.prod_id, transactions.prod_id, products.prod_name
                ORDER BY prod_name''')
        print(cursor.fetchone())
        connection.commit()
        connection.close()

    def Q3(self):
        connection, cursor = self.connect()
        cursor.execute('''SELECT cust_id,seg_name,max(update_at) as update_at
                FROM segments
                WHERE update_at <= "2016-03-01" AND active_flag = 'Y'
                GROUP BY cust_id,seg_name
                ORDER BY update_at''')
        print(cursor.fetchone())
        connection.commit()
        connection.close()

if __name__ == '__main__':
    sql = SQL()
    sql.Q1()
    sql.Q2()
    sql.Q3()

```

### Unsorted (Generic Content)
- [Generic Content](generic/generic.md)


### Web Applications
- [Flask](flask/flask.md)
- [WSGI](wsgi/wsgi.md)

### Numerical Computations (SciPy Stack)
- [NumPy](wsgi/wsgi.md)
- [Matplotlib](matplotlib/matplotlib.md)
- [Pandas](pandas/pandas.md)
- [TensorFlow](tensorflow/tensorflow.md)

### Image Processing
- [PIL/Pillow](pil/pil.md)
- [OpenCV](opencv/opencv.md)

# Text Processing
> Notes on Text Processing, NLTK, ...

__Modules:__ [NLTK](https://www.nltk.org/) <br>

# Image Processing
> Notes on Image Processing, Computer Vision.

__Modules:__ [Pillow (PIL)](https://pillow.readthedocs.io/en/stable/), [OpenCV](https://docs.opencv.org/4.3.0/) <br>
__Resources:__ <br>

- [Adrian Rosebrock](https://www.pyimagesearch.com/blog/)
- [Satya Mallick](https://www.learnopencv.com/)
- [Philipp Wagner](https://bytefish.de/tag/opencv/)
- [Phillip Hasper](http://hasper.info/tag/opencv/)


