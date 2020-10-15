    Copyright(c) 2019-
    Author: Chaitanya Tejaswi (github.com/CRTejaswi)    License: GPL v3.0+


# Python3
> Personal notes for Python3 language.

# References (General)

[__Socratica__](https://www.youtube.com/playlist?list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-) <br>
[__CoreySchafer__](https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU) <br>

- [Matplotlib](https://www.youtube.com/playlist?list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_)
- [Pandas](https://www.youtube.com/playlist?list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS)
- [Flask](https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH)
- [Django](https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)

# Index

- [myScripts](scripts.md)
- [General](#general)
- [IPython](#ipython)
- [IO Access](#io-access)
- [File Access](#file-access)
- [Data Structures](#data-structures)
- [Algorithms](#algorithms)
- [CLI/GUI](#cligui)
- [Structured Data (CSV, JSON, XML)](#structured-data-csv-json-xml)
- [Databases](#databases)
- [Design Styles](style/style.md)
- [Design Patterns](pattern/pattern.md)
- [Processing: Text](#text-processing)
- [Processing: File](#file-processing)
- [Processing: Image](#image-processing)
- [Custom Containters](#custom-containers)
- [Data Analysis](../../topics/dataanalysis/dataanalysis.md)
- [Unsorted](#Unsorted)

## General

__Imports__ <br>

Refer: [Import](https://realpython.com/python-import/) <br>

- Import, Un-Import, Re-Import, CheckIfImported Modules
```python
import this
del this
...
dir(this)
```

- Discovering a new module/package
```python
import this
dir(); dir(this); # GlobalScope, LocalScope ('this')
# ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'this']
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'c', 'd', 'i', 's']

globals(); this.__dict__; # NameSpace: Global, Local ('this')
# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'this': <module 'this' from 'C:\\Users\\Chaitanya Tejaswi\\AppData\\Local\\Programs\\Python\\Python37\\lib\\this.py'>}
# {...}
```

__Shell__ <br>

- Clear Screen
```python
import subprocess; subprocess.run('cls', shell=True); del subprocess;
```

__Access Environment Variables__ <br>
You can access User/System environment variables using:
```python
import os; API_KEY = os.environ.get('Youtube_ApiKey');
```

## IPython
IPython is a REPL interpreter with extensive functionality. <br>

[__Keyboard Shortcuts__](https://jakevdp.github.io/PythonDataScienceHandbook/01.02-shell-keyboard-shortcuts.html) <br>

| Shortcut | Description |
| :-- | :-- |
| `Ctrl+L` or `cls` | Clear Screen |
| `exit` | Exit IPython session |
| `Ctrl+A/E` or `Home/End` | Move cursor to start/end of line |
| `Ctrl+U/K` | Cut startOfLineToCursor/CursorToEndOfLine |
| `Ctrl+R` | Search command history |

[__Useful Shortcuts/Instructions__](https://www.youtube.com/watch?v=3i6db5zX3Rw)

| Instruction | Description | Example |
| :-- | :-- |  :-- |
| item? | Print item's documentation | import os; os? os.*dir*? |
| item?? | Print item's source-code | os?? |
| _iN, _N | Copy input/output of line #N (error if it doesn't exist) | _i12, _12 |
| Ctrl+R | Search command history (PSReadline) | . |
| expression;  | Suppress caching output for expression  | 1+3; |
| %lsmagic  | List all inbuilt (magic) methods | . |

Alike Pythonic inbuilt methods (double-underscore methods), IPython provides it's own set, expressed using `%` (line-specific) or `%%` (cell-specific). <br>
```ipython
%timeit -m 100 -r 3 sum(range(10000))
# 171 fs  4.26 fs per loop (mean  std. dev. of 3 runs, 100 loops each)

%%timeit -n 100 -r 3
total = 0
for x in range(10000):
     total +=x

# 421 fs  15.8 fs per loop (mean  std. dev. of 3 runs, 100 loops each)
```

To set default text-editor, <br>

1. Run `ipython profile create` to create `ipython_config.py, ipython_kernel_config.py` in `C:\Users\Chaitanya Tejaswi\.ipython\profile_default`.
2. In `ipython_config.py`, uncomment `# c.IPythonWidget.editor = ''` => `c.IPythonWidget.editor = nano`.

Running `%edit` now opens up in GNU Nano. <br>
Access `ipython_config.py` using:
```
nano "C:\Users\Chaitanya Tejaswi\.ipython\profile_default\ipython_config.py"
```

You can run multi-language code using methods such as `%%javascript, %%bash`. <br>
The option `%%powershell` doesn't exist by default, but you can use [an extension](https://pypi.org/project/powershellmagic/). <br>

1. Install package using: `pip install powershellmagic`.
2. In `ipython_config.py`, uncomment/edit `c.InteractiveShellApp.extensions = ['powershellmagic']`. <br>
This option loads `powershell` extension on startup, so you don't have to import it using `%load_ext` each time. <br>

__%history__ <br>

```py
# Access lines of current session
%history 10
%history 2-5 11-15 18-20

# Access previous sessions
%history ~1/   # Complete last session
%history ~10/  # Complete last 10th session
%history ~1/2-5 ~1/11-15 ~1/18-20 # Lines from last session

# List all sessions stored in history
?

# Save session history to file
%history -f history.txt     <- Save current session history to file
%history -g -f history.txt  <- Save all session histories to file
```
Session histories are saved in `history.sqlite` file that can be accessed using:
```
sqlite ~/.ipython/profile_default/history.sqlite
# query db for entries
# See: https://stackoverflow.com/questions/19606275/ipython-how-to-wipe-ipythons-history-selectively-securely/39047405
```

__%edit__ <br>

```py
# Open temporary file to input code from
%edit    # Creates new file each time
%edit p  # Use this to access same file each time (when building up code)

# Acceptable arguments
'''
%edit <args>
    filename:      test.py
    input history: 1-5  ~1/1-5
    variable:
    Python Object: get_metadata <- opens up file containing function definition
                                   for editing.
    macro:         ?
'''
```

[__%run__](https://ipython.org/ipython-doc/dev/interactive/magics.html#magic-run) <br>
Run a Py3 script and load it's definitions into current namespace. <br>

__%alias, %rehashx__ <br>

`%rehashx` loads all binaries from $PATH into alias table, allowing you to use them in the session. <br>
```
%rehashx

# Convert pdf to text
pdftotext test.pdf

# Execute code in python repl and come back.
python
# ... (Ctrl+Z)
```
It's best to use this for binaries only, and not executing PS cmdlets, since simple aliases like `del` can become ambiguous. <br>
Leave that to `%powershell` (from `powershellmagic`). <br>

__%xmode__ <br>
Defines verbosity of reported exceptions.

```
%xmode minimal : Specific info only
%xmode context : (default)
%xmode verbose : Full traceback info
```

## CLI/GUI

Review: [argparse](argparse/argparse.md), [Tkinter](tkinter/tkinter.md).

## IO Access

## File Access

__R/W text files__ <br>

```python
# Read (all) / Read (line-by-line)
with open('test.txt','r',encoding='utf-8') as f:
    content = f.read()
with open('test.txt','r',encoding='utf-8') as f:
    lines = list(f)
# Write/Append
with open('test.txt','w',encoding='utf-8') as f:
    f.write(content)
with open('test.txt','a',encoding='utf-8') as f:
    f.write(content)
```

__R/W binary files (structured binary data)__ <br>

Refer: [`struct`](https://python.readthedocs.io/en/stable/library/struct.html#examples)

Use `struct` module to serialize/deserialize values. <br>
This serializes (=packs) `char`,`int`,`long`,`float`,`double` values. (Byte-Size = 1,4,4,4,8) <br>

```python
import struct

# 1024 = 0x400
data = struct.pack('>cilfd', b'A', 1024, 1024, 1024, 1024)
print(data) # b'A\x00\x00\x04\x00\x00\x00\x04\x00D\x80\x00\x00@\x90\x00\x00\x00\x00\x00\x00'
```

A practical use would be to de-serialize bytes from a TCP packet. <br>

<center>
<img src="resources/file-access-1.png">
</center>

```python
import struct

with open('packet.dump','rb') as f:
    data = struct.unpack_from('>HHLL',f.read())
print(data) # (50291, 80, 2778997212, 644363807)

with open('packet.dump','wb') as f:
    data = struct.pack('>HHLL', 50291, 80, 2778997212, 644363807)
    f.write(data)
print(data) # b'\xc4s\x00P\xa5\xa4!\xdc&h6\x1f'
```

__Serializing/De-Serializing Python Objects (pickle, shelve)__ <br>

Refer: [pickle](https://docs.python.org/3/library/pickle.html#examples), [shelve](https://docs.python.org/3/library/shelve.html#example) <br>

Binary file access is serialization/de-serialization of values. <br>
"Pickling/Unpickling" is serialization/de-serialization of Python objects. <br>
This allows for persistent storage (file/db) of data & its transfer over a network. <br>

```python
import pickle

data = {
    'a': [1, 2.0, 3, 4+6j],
    'b': ("character string", b"byte string"),
    'c': {None, True, False}
}
# result = pickle.dumps(data)
# b'\x80\x03}q\x00(X\x01\x00\x00\x00aq\x01]q\x02(K\x01G@\x00\x00\x00\x00\x00\x00\x00K\x03cbuiltins\ncomplex\nq\x03G@\x10\x00\x00\x00\x00\x00\x00G@\x18\x00\x00\x00\x00\x00\x00\x86q\x04Rq\x05eX\x01\x00\x00\x00bq\x06X\x10\x00\x00\x00character stringq\x07C\x0bbyte stringq\x08\x86q\tX\x01\x00\x00\x00cq\ncbuiltins\nset\nq\x0b]q\x0c(\x89\x88Ne\x85q\rRq\x0eu.'

with open('data.pickle', 'wb') as f:
    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
with open('data.pickle', 'rb') as f:
    data = pickle.load(f)
# pickle.loads(result)
# {'a': [1, 2.0, 3, (4+6j)], 'b': ('character string', b'byte string'), 'c': {False, True, None}}
```

"Pickling" an object using `pickle` module serializes it; but it's difficult to access parts of the object when it is deserialized. This is overcome by "Shelving" (pickled objects) into dictionaries using `shelve` module. <br>

```python
import shelve

data = {
    'a': [1, 2.0, 3, 4+6j],
    'b': ("character string", b"byte string"),
    'c': {None, True, False}
}

class Value:
    def __init__(self, value):
        self.value = value

with shelve.open('test.db') as f:
    f['data']  = data
    f['value'] = Value(10)

with shelve.open('test.db') as f:
    print(f['data']['a'], f['value'].value) # [1, 2.0, 3, (4+6j)] 10
```

__R/W structured file-formats (CSV, JSON, XML)__ <br>

Refer: [JSON (Schafer)](https://www.youtube.com/watch?v=9N6a-VLBa2I), [JSON APIs (Schafer)](https://www.youtube.com/watch?v=1lxrb_ezP-g) <br>

__R/W to/from databases__ <br>

Review: [Databases](#databases)

- [SQLite](https://github.com/CRTejaswi/Resources/blob/master/Databases/resources/SQLite.py)
- [SQLServer](https://github.com/CRTejaswi/Resources/blob/master/Databases/resources/SQLServer.py)

__R/W XML/HTML files__ <br>
    __R/W compressed files (archives)__ <br>
__R/W configuration files__ <br>

## Data Structures
Review: [DSA](dsa/DSA.md)

### List, Set, Tuple, Dictionary

__Unpack Values__ <br>
Use dynamic assignment with `*_`. <br>
```py
items = [1,2,3,4,5]
head,*tail = items

head # 1
tail # [2,3,4,5]
```

- Calculate average grade from a set of test marks barring the first & last.
```py
_,total,_ = marks
avg(total)
```

- Get trailing & current values.
```py
*trailing,current = values
```

- Split a string and save values as variables.
```py
*_,crs = 'urn:ogc:def:crs:OGC:1.3:CRS84'.split(':')
crs # 'CRS84'
```
```py
records = [
    ('name', 'address', 'phone'),
    ('Alice', 104, 62355),
    ('Bob', 201, 23144),
]
headers,*_ = records
headers # ('name', 'address', 'phone')
```
```py
# Custom sort/select entries before unpacking
```

__Get Min/Max__ <br>
To get smallest/largest element, use: `min(), max()`. <br>
To get 'n' smallest/largest elements (n << sizeof(Object)), use: `heapq.nsmallest(n), heapq.nlargest(n)`. <br>
To get 'n' smallest/largest elements (n ~ sizeof(Object)), use: `sorted(Object)[:N], sorted(Object)[-N:]`. <br>

```py
import heapq

portfolio = [
    {'name': 'ABC', 'shares': 100, 'price': 90.1},
    {'name': 'BCD', 'shares': 50, 'price': 190.1},
    {'name': 'CDE', 'shares': 200, 'price': 290.1},
    {'name': 'DEF', 'shares': 10, 'price': 590.1},
    {'name': 'FGH', 'shares': 30, 'price': 80.1},
]
cheap = heapq.nsmallest(3, portfolio, key=lambda x: x['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda x: x['price'])
# [{'name': 'FGH', 'shares': 30, 'price': 80.1}, {'name': 'ABC', 'shares': 100, 'price': 90.1}, {'name': 'BCD', 'shares': 50, 'price': 190.1}]
# [{'name': 'DEF', 'shares': 10, 'price': 590.1}, {'name': 'CDE', 'shares': 200, 'price': 290.1}, {'name': 'BCD', 'shares': 50, 'price': 190.1}]
```

__Dict: Insert/Remove Values__ <br>

```py
records = {}
records['Alice'] = [32, 'Host', 12]
records['Bob'] = [24]
records['Cathy'] = set()
records['Dell'] = {}

records['Bob'].append('Client')
records['Bob'].append(1)
records['Cathy'].update({'Client',2})
records['Dell'].update({'credentials': [27,'Host',12]})
records
'''
{
'Alice': [32, 'Host', 12],
'Bob': [24, 'Client', 1],
'Cathy': {'Client', 2},
'Dell': {'credentials': [27, 'Host', 12]}
}
'''
```

__Dict: Maintain Insertion Order__ <br>

```py
from collections import OrderedDict
records = OrderedDict()
records['Alice'] = [32, 'Host']
records['Bob'] = [24, 'Client']

import json
json.dumps(records)
# '{"Alice": [32, "Host"], "Bob": [24, "Client"]}'
```

__Dict: Set Arithmetic__ <br>
`keys()`/`items()` (but not `values()`) support set-arithmetic. <br>
```py
A = {'x': 10, 'y': 11, 'z': 12}
B = {'y': 15, 'z': 12}

# Common Keys
A.keys() & B.keys() # {'z', 'y'}
# Keys in A, but not in B
A.keys() - B.keys() # {'x'}
# Common (key,value) pairs
A.items() & B.items() # {('z', 12)}

# Create a new dict with some keys removed
C = {key:A[key] for key in A.keys() - {x}} # {'z': 12, 'y': 11}
```

__Dict: Custom Operations__ <br>
To process & assign dictionary entries, use `zip()` to access `key, value`.
```py
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
minPrice = min(zip(prices.values(), prices.keys()))
maxPrice = max(zip(prices.values(), prices.keys()))
ascPrices = sorted(zip(prices.values(), prices.keys()))
descPrices = sorted(zip(prices.values(), prices.keys()), reverse=True)

minPrice; maxPrice; ascPrices;descPrices;
'''
(10.75,'FB')
(612.78,'AAPL')
[(10.75, 'FB'), (37.2, 'HPQ'), (45.23, 'ACME'), (205.55, 'IBM'), (612.78, 'AAPL')]
[(612.78, 'AAPL'), (205.55, 'IBM'), (45.23, 'ACME'), (37.2, 'HPQ'), (10.75, 'FB')]
'''
```

__Remove Duplicates__ <br>
Unordered: `set()` <br>
Ordered: `remove_duplicates()` <br>

```py
def remove_duplicates(items, key=None):
    seen = set()
    for item in items:
        value = item if key is None else key(item)
        if value not in seen:
            yield item
            seen.add(value)

A = [{'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
# Remove duplicates of type (x,y)
list(remove_duplicates(A, key=lambda f: (f['x'], f['y'])))
# Remove duplicates of type 'x'
list(remove_duplicates(A, key=lambda f: f['x']))
# [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]
# [{'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
```

## Algorithms
Review: [DSA](dsa/DSA.md)

<center>
<img src="resources/algorithms-1.png">
</center>

__Search, Sort & Filter__ <br>

Refer: [sorted](https://docs.python.org/3/howto/sorting.html), [bisect](https://docs.python.org/3/library/bisect.html), [bisect - recipie](https://code.activestate.com/recipes/577197-sortedcollection/). <br>

When the size of data is small, it's better to get all the elements, and sort it exactly once using `sorted`. <br>
When the size of data is large, `bisect` is more effective. `bisect` module implements an algorithm for inserting elements into a list while maintaining the list in sorted order. <br>

```python
import bisect

values = [14, 85, 77, 26, 50, 45, 66, 79, 10, 3, 84, 77, 1]
_list = []

print('Val  Pos  Contents')
print('---  ---  --------')
for value in values:
    index = bisect.bisect(_list,value)
    bisect.insort(_list,value)
    print(f'{value:3}  {index:3}  {_list}')
```
```
Val  Pos  Contents
---  ---  --------
 14    0  [14]
 85    1  [14, 85]
 77    1  [14, 77, 85]
 26    1  [14, 26, 77, 85]
 50    2  [14, 26, 50, 77, 85]
 45    2  [14, 26, 45, 50, 77, 85]
 66    4  [14, 26, 45, 50, 66, 77, 85]
 79    6  [14, 26, 45, 50, 66, 77, 79, 85]
 10    0  [10, 14, 26, 45, 50, 66, 77, 79, 85]
  3    0  [3, 10, 14, 26, 45, 50, 66, 77, 79, 85]
 84    9  [3, 10, 14, 26, 45, 50, 66, 77, 79, 84, 85]
 77    8  [3, 10, 14, 26, 45, 50, 66, 77, 77, 79, 84, 85]
  1    0  [1, 3, 10, 14, 26, 45, 50, 66, 77, 77, 79, 84, 85]
```

```python
import bisect

def grade(score, breakpoints=[60,70,80,90], grades='FDCBA'):
    index = bisect.bisect(breakpoints, score)
    return grades[index]

[ grade(score) for score in [33,99,73,81,90,24,77,95] ]
# ['F', 'A', 'C', 'B', 'A', 'F', 'C', 'A']
```

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

## Custom Containers

__List__ <br>

- Implements a list with modified methods

```python
#!/usr/bin/env python3
class _list:
    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return f'{self.values}'

    def __len__(self):
        return len(self.values)

    def extend(self, newList=None, *values):
        if newList and type(newList) == list:
            return self.values.extend(newList)
        elif values:
            values = list(values)
            return self.values.extend(values)

    def __add__(self, values=[]):
        for i in range(len(values)):
            self.values[i] += values[i]
        return self.values

    def __sub__(self, values=[]):
        for i in range(len(values)):
            self.values[i] -= values[i]
        return self.values

    def __mul__(self, values=[]):
        for i in range(len(values)):
            self.values[i] *= values[i]
        return self.values

    def __div__(self, values=[]):
        for i in range(len(values)):
            self.values[i] /= values[i]
        return self.values

    def __floordiv__(self, values=[]):
        for i in range(len(values)):
            self.values[i] //= values[i]
        return self.values

    def __mod__(self, values=[]):
        for i in range(len(values)):
            self.values[i] %= values[i]
        return self.values

    def type(self):
        return [type(self.values), self.values]
```

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

### Unsorted (Generic Content)
- [Generic Content](generic/generic.md)

