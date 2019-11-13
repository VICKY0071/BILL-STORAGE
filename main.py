import os
from modules import take_input, display, show_entry
import sys
import sqlite3

if os.path.isfile('storage.db') == False:
    file= open('storage.db', 'w')

choice = 'y'


while choice.lower() == 'y':
    x = int(input('1)insert\n2)display\n3)search entry\n4)clear all data\n5)exit\n'))
    if x == 1:
        take_input()
    elif x == 2:
        display()
    elif x == 3:
        name = input('item name for the search : ')
        show_entry(name = name)
    elif x == 4:
        conn = sqlite3.connect('storage.db')
        c = conn.cursor()
        c.execute('TRUNCATE TABLE expenses')
        conn.commit()
        conn.close()
    elif x ==5:
        sys.exit()
    choice = input('Continue[y/n] : ')

try:
    file.close()
except:
    pass
    