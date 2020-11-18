    Copyright(c) 2020-
    Author: Chaitanya Tejaswi (github.com/CRTejaswi)    License: GPL v3.0+

# Databases
> Personal notes.

# Index

- [Setup](#setup)
- [Templates](#templates)
- [Challenges](#challenges)
- [SQLite](#sqlite)

## Setup

__SQLite__ <br>

__SQLServer__ <br>

__MySQL__ <br>

__PostGreSQL__ <br>

__MongoDB__ <br>

## Templates

- __TASK__: Write classes to CRUD SQL databases. (Entries are from [this dataset](https://crtejaswi.github.io/API/latex1.json).)

[__SQLite__](resources/SQLite.py) <br>

- [ ] Implement `outCsv` method.
- [ ] Modify methods to automate CRUDing using a CSV file.

## Challenges

Refer: [[1]](https://www.hackerrank.com/domains/sql) [[2]](https://www.w3resource.com/sql-exercises/)


## SQLite

| Task | Command |
| :-- | :-- |
| Open file | `sqlite3 file.db` |
|  | `.open file.db` |
| Exit | `.exit` |
| List all commands | `.help` |
| List all databases | `.database` |
| List tables from current database | `.table [PATTERN]` |
| Show structure of all tables | `.fullschema` |
| Show structure of a table | `.schema TABLENAME` |
| Save query-results (one/more) to file | `.once FILENAME` |
|  | `.output FILENAME` |
| Execute SQL queries from file | `.read FILENAME` |
