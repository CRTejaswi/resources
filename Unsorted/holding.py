#! /usr/bin/env python3
# holding.py
import csv


class Holding:
    def __init__(self, name, date, price, shares):
        self.name = name
        self.date = date
        self.price = price
        self.shares = shares

    def cost(self):
        return self.shares * self.price

    def sell(self, n):
        self.shares -= n


def read_portfolio(filename):
    portfolio = []
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = Holding(row[0], row[1], float(row[2]), int(row[3]))
            portfolio.append(holding)
    return portfolio
