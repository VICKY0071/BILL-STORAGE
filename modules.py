import os
import sqlite3
import pandas as pd 
import numpy as np 
import time

def take_input():
    conn = sqlite3.connect('storage.db')
    item_name = input('Enter the name of the item : ')
    item_cost = input('Enter the cost of the item : ')
    date = input('Enter the date of purchase in format JAN 12 2019: ')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS expenses (Item text NOT NULL, Cost text, Date text NOT NULL)')
    c.execute('INSERT INTO expenses (Item, Cost, Date) VALUES (?, ?, ?)', [item_name, item_cost, date])
    conn.commit()
    conn.close()

def display():
    conn = sqlite3.connect('storage.db')
    c = conn.cursor()
    print('{:<10}{:<10}{:<10}'.format('Name', 'Cost', 'Date'))
    c.execute('SELECT * FROM expenses')
    list = c.fetchall()
    for i in list:
        print('{:<20}{:<10}{:<10}'.format(i[0], i[1], i[2]))
    conn.commit()
    conn.close()

def show_entry(name):
    conn = sqlite3.connect('storage.db')
    c = conn.cursor()
    c.execute('SELECT * FROM expenses WHERE Item == (?)', [name])
    print("SEARCH RESULTS")
    for i in c.fetchall():
        print('{:<20}{:<10}{:<10}'.format(i[0], i[1], i[2]))
    conn.commit()
    conn.close()
