#!/usr/bin/env python3
# tabulate.py


class TableFormatter:
    '''
    Design Specification for making tables.
    Use inheritance to customize behavior.
    '''

    def headings(self, headers):
        raise NotImplementedError

    def row(self, rowdata):
        raise NotImplementedError


class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        for header in headers:
            print(f'{header:>10s}', end=' ')
        print()

    def row(self, rowdata):
        for item in rowdata:
            print(f'{item:>10s}', end=' ')
        print()


class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(', '.join(headers))

    def row(self, rowdata):
        print(', '.join(rowdata))


class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr>', end='')
        for header in headers:
            print(f'<th>{header}</th>', end='')
        print('</tr>', end='')

    def row(self, rowdata):
        print('<tr>', end='')
        for item in rowdata:
            print(f'<td>{item}</td>', end='')
        print('</tr>', end='')


def print_table(objects, colnames, formatter):
    '''
    Print a formatted table with attributes from a list of objects.
    '''
    formatter.headings(colnames)
    for obj in objects:
        rowdata = [str(getattr(obj, colname)) for colname in colnames]
        formatter.row(rowdata)
