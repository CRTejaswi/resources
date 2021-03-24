    Copyright(c) 2019-
    Author: Chaitanya Tejaswi (github.com/CRTejaswi)    License: GPL v3.0+


# Python3
> Personal notes for Python3 language.


# Index

- [Resources](#resources)
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

## Resources

| Link | Description |
| :--: | :-- |
| [Projects](#projects) | Useful list of projects |

# References (General)

[__Socratica__](https://www.youtube.com/playlist?list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-) <br>
[__CoreySchafer__](https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU) <br>

- [Matplotlib](https://www.youtube.com/playlist?list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_)
- [Pandas](https://www.youtube.com/playlist?list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS)
- [Flask](https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH)
- [Django](https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)

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
| `_iN, _N` | Copy input/output of line #N (error if it doesn't exist) | `_i12, _12` |
| Ctrl+R | Search command history (PSReadline) | . |
| expression;  | Suppress caching output for expression  | 1+3; |
| %lsmagic  | List all inbuilt (magic) methods | . |

Alike Pythonic inbuilt methods (double-underscore methods), IPython provides it's own set, expressed using `%` or `%%` (line/cell). <br>
```ipython
%timeit -m 100 -r 3 sum(range(10000))
# 171 fs  4.26 fs per loop (mean  std. dev. of 3 runs, 100 loops each)

%%timeit -n 100 -r 3
total = 0
for x in range(10000):
     total +=x

# 421 fs  15.8 fs per loop (mean  std. dev. of 3 runs, 100 loops each)
```

__%history__ <br>

```ipython
# Access lines of current session
%history 10
%history 2-5 11-15 18-20

# Access previous sessions
%history ~1/   # Complete last session
%history ~10/  # Complete last 10th session
%history ~1/2-5 ~1/11-15 ~1/18-20 # Lines from last session

# List all sessions stored in history
%history -g -f history.txt
(cat .\history.txt | where {$_ -match '(\d+)/(\d+)'} | forEach {$Matches[1]} | Get-Unique).count

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

To setup __Vim__ as default:
```
c.TerminalInteractiveShell.editor = 'vim'
c.TerminalInteractiveShell.editing_mode = 'vi'
c.TerminalInteractiveShell.prompt_includes_vi_mode = True
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

__IPython: Custom in-built (magic/dunder) functions__ <br>
Use `@register_line_magic()`, `@register_cell_magic()` decorators to create custom magic functions. <br>
All arguments to a magic function are passed as string. <br>

```py
from IPython.core.magic import register_line_magic, register_cell_magic


@register_line_magic("reverse")
def reverseLine(line):
    '''
    Reverses a string
    '''
    return line[::-1]

@register_cell_magic("")
...
```
```
>> %reverse hello world
'dlrow olleh'
```
To use these across sessions, you can either create an "extension" or add "startup-files" (save `.py/.ipy` files in `~./ipython/profile_default/startup` directory). <br>
Extensions can be easily shared over `PyPI`; Startup-files are more suited for quick, personal use. <br>

This is the same thing published as an "extension". Load it using `%load_ext reverser`. <br>
```py
# ~/.ipython/extensions/reverser.py
from IPython.core.magic import register_line_magic, register_cell_magic

def load_ipython_extension(ipython):
    @register_line_magic("reverse")
    def reverseLine(line):
        '''
        Reverses a string
        '''
        return line[::-1]

    @register_cell_magic("")
    ...
...

```
When using startup-files, if the written methods are memory-intensive, it significantly impacts IPython startup-time. <br>
A solution is to create "profiles" dedicated to each use-case (eg. debug, demo, computation, image-processing, ...) <br>
Create a new profile using `ipython profile create debug`. To access this, start IPython using `ipython --profile=debug`. <br>

__IPython: Configuration__ <br>
IPython can be configured using a `config.py` file located at `~/.ipython/profile_default/ipython_config.py`. <br>
For first time use, it has to be created using `ipython profile create`. <br>

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


- Live Server
Use the default `http.server` to start a testing server using:
```
python -m http.server
py -m http.server
```

# Projects
(currently lifted from https://github.com/tuvtran/project-based-learning#python)

- [Build a Simple Interpreter](https://ruslanspivak.com/lsbasi-part1/)
- [Build a Simple Blockchain in Python](https://hackernoon.com/learn-blockchains-by-building-one-117428612f46)
- [Write a NoSQL Database in Python](https://jeffknupp.com/blog/2014/09/01/what-is-a-nosql-database-learn-by-writing-one-in-python/)
- [Building a Gas Pump Scanner with OpenCV/Python/iOS](https://hackernoon.com/building-a-gas-pump-scanner-with-opencv-python-ios-116fe6c9ae8b)
- [Build a Distributed Streaming System with Python and Kafka](https://codequs.com/p/S14jQ5UyG/build-a-distributed-streaming-system-with-apache-kafka-and-python)
- [Writing a basic x86-64 JIT compiler from scratch in stock Python](https://csl.name/post/python-jit/)
- Making a low level (Linux) debugger
  - [Part 1](https://blog.asrpo.com/making_a_low_level_debugger)
  - [Part 2: C](https://blog.asrpo.com/making_a_low_level_debugger_part_2)
- Implementing a Search Engine
  - [Part 1](http://www.ardendertat.com/2011/05/30/how-to-implement-a-search-engine-part-1-create-index/)
  - [Part 2](http://www.ardendertat.com/2011/05/31/how-to-implement-a-search-engine-part-2-query-index/)
  - [Part 3](http://www.ardendertat.com/2011/07/17/how-to-implement-a-search-engine-part-3-ranking-tf-idf/)
- [Build the Game of Life](https://robertheaton.com/2018/07/20/project-2-game-of-life/)
- [Create terminal ASCII art](https://robertheaton.com/2018/06/12/programming-projects-for-advanced-beginners-ascii-art/)
- [Write a Tic-Tac-Toe AI](https://robertheaton.com/2018/10/09/programming-projects-for-advanced-beginners-3-a/)
- [Create photomosaic art](https://robertheaton.com/2018/11/03/programming-project-4-photomosaics/)
- [Build the game "Snake" in the terminal](https://robertheaton.com/2018/12/02/programming-project-5-snake/)
- [Write yourself a Git](https://wyag.thb.lt/)
- [A Python implementation of a Python bytecode runner](https://www.aosabook.org/en/500L/a-python-interpreter-written-in-python.html)

### Web Scraping:

- [Mining Twitter Data with Python](https://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/)
- [Scrape a Website with Scrapy and MongoDB](https://realpython.com/blog/python/web-scraping-with-scrapy-and-mongodb/)
- [How To Scrape With Python and Selenium WebDriver](http://www.byperth.com/2018/04/25/guide-web-scraping-101-what-you-need-to-know-and-how-to-scrape-with-python-selenium-webdriver/)
- [Which Movie Should I Watch using BeautifulSoup](https://medium.com/@nishantsahoo.in/which-movie-should-i-watch-5c83a3c0f5b1)

### Web Applications:

- [Build a Microblog with Flask](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- Create a Blog Web App In Django
  - [Part I : Introduction](https://tutorial.djangogirls.org/en/)
  - [Part II : Extension To Add More Features](https://legacy.gitbook.com/book/djangogirls/django-girls-tutorial-extensions/details)
- [Choose Your Own Adventure Presentations](https://www.twilio.com/blog/2015/03/choose-your-own-adventures-presentations-wizard-mode-part-1-of-3.html)
- [Build a Todo List with Flask and RethinkDB](https://realpython.com/blog/python/rethink-flask-a-simple-todo-list-powered-by-flask-and-rethinkdb/)
- [Build a Todo List with Django and Test-Driven Development](http://www.obeythetestinggoat.com/)
- [Build a RESTful Microservice in Python](http://www.skybert.net/python/developing-a-restful-micro-service-in-python/)
- [Microservices with Docker, Flask, and React](https://testdriven.io/)
- [Build A Simple Web App With Flask](https://pythonspot.com/flask-web-app-with-python/)
- [Build a RESTful API with Flask – The TDD Way](https://scotch.io/tutorials/build-a-restful-api-with-flask-the-tdd-way)
- [Create A Django API in under 20 minutes](https://codeburst.io/create-a-django-api-in-under-20-minutes-2a082a60f6f3)

### Bots:

- [Build a Reddit Bot](http://pythonforengineers.com/build-a-reddit-bot-part-1/)
- [How to Make a Reddit Bot - YouTube](https://www.youtube.com/watch?v=krTUf7BpTc0) (video)
- [Build a Facebook Messenger Bot](https://blog.hartleybrody.com/fb-messenger-bot/)
- [Making a Reddit + Facebook Messenger Bot](https://pythontips.com/2017/04/13/making-a-reddit-facebook-messenger-bot/)
- How To Create a Telegram Bot Using Python
  - [Part 1](https://khashtamov.com/en/how-to-create-a-telegram-bot-using-python/)
  - [Part 2](https://khashtamov.com/en/how-to-deploy-telegram-bot-django/)
- [Create a Twitter Bot In Python](https://medium.freecodecamp.org/creating-a-twitter-bot-in-python-with-tweepy-ac524157a607)

### Data Science:

- Learn Python For Data Science by Doing Several Projects (video):
  - [Part 1: Introduction](https://www.youtube.com/watch?v=T5pRlIbr6gg)
  - [Part 2: Twitter Sentiment Analysis](https://www.youtube.com/watch?v=o_OZdbCzHUA)
  - [Part 3: Recommendation Systems](https://www.youtube.com/watch?v=9gBC9R-msAk&list=PL2-dafEMk2A6QKz1mrk1uIGfHkC1zZ6UU&index=3)
  - [Part 4: Predicting Stock Prices](https://www.youtube.com/watch?v=SSu00IRRraY&index=4&list=PL2-dafEMk2A6QKz1mrk1uIGfHkC1zZ6UU)
  - [Part 5: Deep Dream in TensorFlow](https://www.youtube.com/watch?v=MrBzgvUNr4w&list=PL2-dafEMk2A6QKz1mrk1uIGfHkC1zZ6UU&index=5)
  - [Part 6: Genetic Algorithms](https://www.youtube.com/watch?v=dSofAXnnFrY&index=6&list=PL2-dafEMk2A6QKz1mrk1uIGfHkC1zZ6UU)

### Machine Learning:

- [Write Linear Regression From Scratch in Python](https://www.youtube.com/watch?v=uwwWVAgJBcM) (video)
- [Step-By-Step Machine Learning In Python](https://machinelearningmastery.com/machine-learning-in-python-step-by-step/)
- [Predict Quality Of Wine](https://medium.freecodecamp.org/using-machine-learning-to-predict-the-quality-of-wines-9e2e13d7480d)
- [Solving A Fruits Classification Problem](https://towardsdatascience.com/solving-a-simple-classification-problem-with-python-fruits-lovers-edition-d20ab6b071d2)
- [Learn Unsupervised Learning with Python](https://towardsdatascience.com/unsupervised-learning-with-python-173c51dc7f03)
- [Build Your Own Neural Net from Scratch in Python](https://towardsdatascience.com/how-to-build-your-own-neural-network-from-scratch-in-python-68998a08e4f6)
- [Linear Regression in Python without sklearn](https://medium.com/we-are-orb/linear-regression-in-python-without-scikit-learn-50aef4b8d122)
- [Multivariate Linear Regression without sklearn](https://medium.com/we-are-orb/multivariate-linear-regression-in-python-without-scikit-learn-7091b1d45905)
- [Music Recommender using KNN](https://towardsdatascience.com/how-to-build-a-simple-song-recommender-296fcbc8c85)
- Find Similar Quora Questions-
  - [Using BOW, TFIDF and Xgboost](https://towardsdatascience.com/finding-similar-quora-questions-with-bow-tfidf-and-random-forest-c54ad88d1370)
  - [Using Word2Vec and Xgboost](https://towardsdatascience.com/finding-similar-quora-questions-with-word2vec-and-xgboost-1a19ad272c0d)

### OpenCV:

- [Build A Document Scanner](https://www.pyimagesearch.com/2014/09/01/build-kick-ass-mobile-document-scanner-just-5-minutes/)
- [Build A Face Detector using OpenCV and Deep Learning](https://www.pyimagesearch.com/2018/02/26/face-detection-with-opencv-and-deep-learning/)
- [Build a Face Recognition System using OpenCV, Python and Deep Learning](https://www.pyimagesearch.com/2018/06/18/face-recognition-with-opencv-python-and-deep-learning/)
- [Detect The Salient Features in an Image](https://www.pyimagesearch.com/2018/07/16/opencv-saliency-detection/)
- [Build A Barcode Scanner](https://www.pyimagesearch.com/2018/05/21/an-opencv-barcode-and-qr-code-scanner-with-zbar/)
- [Learn Face Clustering with Python](https://www.pyimagesearch.com/2018/07/09/face-clustering-with-python/)
- [Object Tracking with Camshift](https://www.pyimagesearch.com/wp-content/uploads/2014/11/opencv_crash_course_camshift.pdf)
- [Semantic Segmentation with OpenCV and Deep Learning](https://www.pyimagesearch.com/2018/09/03/semantic-segmentation-with-opencv-and-deep-learning/)
- [Text Detection in Images and Videos](https://www.pyimagesearch.com/2018/08/20/opencv-text-detection-east-text-detector/)
- [People Counter using OpenCV](https://www.pyimagesearch.com/2018/08/13/opencv-people-counter/)
- [Tracking Multiple Objects with OpenCV](https://www.pyimagesearch.com/2018/08/06/tracking-multiple-objects-with-opencv/)
- [Neural Style Transfer with OpenCV](https://www.pyimagesearch.com/2018/08/27/neural-style-transfer-with-opencv/)
- [OpenCV OCR and Text Recognition](https://www.pyimagesearch.com/2018/09/17/opencv-ocr-and-text-recognition-with-tesseract/)
- [Text Skew Correction Tutorial](https://www.pyimagesearch.com/2017/02/20/text-skew-correction-opencv-python/)
- [Facial Landmark Detection Tutorial](https://www.pyimagesearch.com/2017/04/03/facial-landmarks-dlib-opencv-python/)
- [Object Detection using Mask-R-CNN](https://www.learnopencv.com/deep-learning-based-object-detection-and-instance-segmentation-using-mask-r-cnn-in-opencv-python-c/)
- [Automatic Target Detection Tutorial](https://www.pyimagesearch.com/2015/05/04/target-acquired-finding-targets-in-drone-and-quadcopter-video-streams-using-python-and-opencv/)
- [EigenFaces using OpenCV](https://www.learnopencv.com/eigenface-using-opencv-c-python/)
- [Faster(5-point) Facial Landmark Detection Tutorial](https://www.pyimagesearch.com/2018/04/02/faster-facial-landmark-detector-with-dlib/)
- [Hand Keypoint Detection](https://www.learnopencv.com/hand-keypoint-detection-using-deep-learning-and-opencv/)
- Dlib Correlation Object Tracking -
  - [Single Object Tracker](https://www.pyimagesearch.com/2018/10/22/object-tracking-with-dlib/)
  - [Mutiple Object Tracker](https://www.pyimagesearch.com/2018/10/29/multi-object-tracking-with-dlib/)
- [Image Stitching with OpenCV and Python](https://www.pyimagesearch.com/2018/12/17/image-stitching-with-opencv-and-python/)
- [Instance Segmentation with OpenCV](https://www.pyimagesearch.com/2018/11/26/instance-segmentation-with-opencv/)
- [Face mask detector](https://www.pyimagesearch.com/2020/05/04/covid-19-face-mask-detector-with-opencv-keras-tensorflow-and-deep-learning/)

### Deep Learning:

- [Using Convolutional Neural Nets to Detect Facial Keypoints](http://danielnouri.org/notes/2014/12/17/using-convolutional-neural-nets-to-detect-facial-keypoints-tutorial/)
- [Generate an Average Face using Python and OpenCV](https://www.learnopencv.com/average-face-opencv-c-python-tutorial/)
- [Break A Captcha System using CNNs](https://medium.com/@ageitgey/how-to-break-a-captcha-system-in-15-minutes-with-machine-learning-dbebb035a710)
- [Use pre-trained Inception model to provide image predictions](https://medium.com/google-cloud/keras-inception-v3-on-google-compute-engine-a54918b0058)
- [Create your first CNN](https://hackernoon.com/deep-learning-cnns-in-tensorflow-with-gpus-cba6efe0acc2)
- [Build A Facial Recognition Pipeline](https://hackernoon.com/building-a-facial-recognition-pipeline-with-deep-learning-in-tensorflow-66e7645015b8)
- [Build An Image Caption Generator](https://medium.freecodecamp.org/building-an-image-caption-generator-with-deep-learning-in-tensorflow-a142722e9b1f)
- [Make your Own Face Recognition System](https://medium.freecodecamp.org/making-your-own-face-recognition-system-29a8e728107c)
- [Train a Language Detection AI in 20 minutes](https://towardsdatascience.com/how-i-trained-a-language-detection-ai-in-20-minutes-with-a-97-accuracy-fdeca0fb7724)
- [Object Detection With Neural Networks](https://towardsdatascience.com/object-detection-with-neural-networks-a4e2c46b4491)
- Learn Twitter Sentiment Analysis -
  - [Part I - Data Cleaning](https://towardsdatascience.com/another-twitter-sentiment-analysis-bb5b01ebad90)
  - [Part II - EDA, Data Visualisation](https://towardsdatascience.com/another-twitter-sentiment-analysis-with-python-part-2-333514854913)
  - [Part III - Zipf's Law, Data Visualisation](https://towardsdatascience.com/another-twitter-sentiment-analysis-with-python-part-3-zipfs-law-data-visualisation-fc9eadda71e7)
  - [Part IV - Feature Extraction(count vectoriser)](https://towardsdatascience.com/another-twitter-sentiment-analysis-with-python-part-4-count-vectorizer-b3f4944e51b5)
  - [Part V - Feature Extraction(Tfidf vectoriser)](https://towardsdatascience.com/another-twitter-sentiment-analysis-with-python-part-5-50b4e87d9bdd)
  - [Part VI - Doc2Vec](https://towardsdatascience.com/another-twitter-sentiment-analysis-with-python-part-6-doc2vec-603f11832504)
  - [Part VII - Phrase Modeling + Doc2Vec](https://towardsdatascience.com/another-twitter-sentiment-analysis-with-python-part-7-phrase-modeling-doc2vec-592a8a996867)
  - [Part VIII - Dimensionality Reduction](https://towardsdatascience.com/another-twitter-sentiment-analysis-with-python-part-8-dimensionality-reduction-chi2-pca-c6d06fb3fcf3)
  - [Part IX - Neural Nets with Tfdif vectors](https://towardsdatascience.com/another-twitter-sentiment-analysis-with-python-part-9-neural-networks-with-tfidf-vectors-using-d0b4af6be6d7)
  - [Part X - Neural Nets with word2vec/doc2vec](https://towardsdatascience.com/another-twitter-sentiment-analysis-with-python-part-10-neural-network-with-a6441269aa3c)
  - [Part XI - CNN with Word2Vec](https://towardsdatascience.com/another-twitter-sentiment-analysis-with-python-part-11-cnn-word2vec-41f5e28eda74)
- [Use Transfer Learning for custom image classification](https://becominghuman.ai/transfer-learning-retraining-inception-v3-for-custom-image-classification-2820f653c557)
- [Learn to Code a simple Neural Network in 11 lines of Python](https://iamtrask.github.io/2015/07/12/basic-python-network/)
- [Build a Neural Network using Gradient Descent Approach](https://iamtrask.github.io/2015/07/27/python-network-part2/)
- [Train a Keras Model To Generate Colors](https://heartbeat.fritz.ai/how-to-train-a-keras-model-to-generate-colors-3bc79e54971b)
- [Get Started with Keras on a Custom Dataset](https://www.pyimagesearch.com/2018/09/10/keras-tutorial-how-to-get-started-with-keras-deep-learning-and-python/)
- [Use EigenFaces and FisherFaces on Faces94 dataset](https://nicholastsmith.wordpress.com/2016/02/18/eigenfaces-versus-fisherfaces-on-the-faces94-database-with-scikit-learn/)
- [Kaggle MNIST Digit Recognizer Tutorial](https://medium.com/@lvarruda/how-to-get-top-2-position-on-kaggles-mnist-digit-recognizer-48185d80a2d4)
- [Fashion MNIST tutorial with tf.keras](https://medium.com/tensorflow/hello-deep-learning-fashion-mnist-with-keras-50fcff8cd74a)
- [CNN using Keras to automatically classify root health](https://www.pyimagesearch.com/2018/10/15/deep-learning-hydroponics-and-medical-marijuana/)
- [Keras vs Tensorflow](https://www.pyimagesearch.com/2018/10/08/keras-vs-tensorflow-which-one-is-better-and-which-one-should-i-learn/)
- [Deep Learning and Medical Image Analysis for Malaria Detection](https://www.pyimagesearch.com/2018/12/03/deep-learning-and-medical-image-analysis-with-keras/)
- [Transfer Learning for Image Classification using Keras](https://towardsdatascience.com/transfer-learning-for-image-classification-using-keras-c47ccf09c8c8)
- [Code a Smile Classifier using CNNS in Python](https://github.com/kylemcdonald/SmileCNN)
- [Natural Language Processing using scikit-learn](https://towardsdatascience.com/natural-language-processing-count-vectorization-with-scikit-learn-e7804269bb5e)
- [Code a Taylor Swift Lyrics Generator](https://towardsdatascience.com/ai-generates-taylor-swifts-song-lyrics-6fd92a03ef7e)

