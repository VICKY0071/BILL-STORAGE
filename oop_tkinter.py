'''
LOGS:
1)Login_page needs to be completed and connecticity should be established : FININSHED
2)Trying to add multiple billing accounts for different accounts basicallly by 
adding tables for each new user in the storage database : PENDING
'''
import os
import tkinter as tk 
import wx
import sqlite3
from modules import take_input
from tkinter import messagebox
from tkinter.messagebox import askyesno


admin = 'admin123'

app = wx.App()
Window_size = wx.GetDisplaySize()

Width = Window_size[0]
Height = Window_size[1]

if os.path.isfile('storage.db'):
    pass
else:
    file = open('storage.db', 'w+')
    conn = sqlite3.connect('storage.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS expenses (Item text NOT NULL, Cost text, Date text NOT NULL)')
    conn.commit()
    conn.close()

if os.path.isfile('passwords.db'):
    pass
else:
    pass_file = open('passwords.db', 'w+')
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS user_pass (username text NOT NULL, password text NOT NULL)')
    conn.commit()
    conn.close()

class MyApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self, height = Height, width = Width)
        container.pack(fill = 'both', expand = True, side= 'top')

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for F in (Input_page, Login_page, Display_page, First_page, New_user):

            frame = F(self, container)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = 'nsew' )
        
        self.show_frame(First_page)
        
    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


import cv2

class Input_page(tk.Frame):

    def __init__(self, controller, parent):
        tk.Frame.__init__(self, parent, bg = '#897B94')

        main_label = tk.Label(self, text = 'BILL STORAGE', bg = '#897B94', fg= 'black', font = (cv2.FONT_HERSHEY_SIMPLEX, 50, ('bold underline')))
        main_label.pack(pady = 15)

        name_label = tk.Label(self, text = 'Item Name', bg = '#897B94', fg = 'black', font = (cv2.FONT_HERSHEY_SIMPLEX, 30, ('bold')))
        name_label.pack(pady = 30)

        name_input = tk.Entry(self, width = 40, bg= 'white', font = (cv2.FONT_HERSHEY_DUPLEX, 15, ('italic')))
        name_input.pack(pady = 6)

        date_label = tk.Label(self, text = 'Date of Purchase', bg = '#897B94', fg = 'black', font = (cv2.FONT_HERSHEY_SIMPLEX, 30, ('bold')))
        date_label.pack(pady = 30)

        date_format_label = tk.Label(self, text = 'format : JAN 12 2019', bg = '#897B94', fg = 'white', font = (cv2.FONT_HERSHEY_SIMPLEX, 10, ('bold')))
        date_format_label.pack()

        date_input = tk.Entry(self, width = 40, bg= 'white', font = (cv2.FONT_HERSHEY_DUPLEX, 15, ('italic')))
        date_input.pack(pady = 6)

        cost_label = tk.Label(self, text = 'Item Cost', bg = '#897B94', fg = 'black', font = (cv2.FONT_HERSHEY_SIMPLEX, 30, ('bold')))
        cost_label.pack(pady = 30)

        cost_input = tk.Entry(self, width = 15, bg= 'white', font = (cv2.FONT_HERSHEY_DUPLEX, 15, ('italic')))
        cost_input.pack(pady = 6)
    
        def take_input():
            conn = sqlite3.connect('storage.db')
            item_name = name_input.get()
            item_cost=  cost_input.get()
            date = date_input.get()   
            c = conn.cursor()
            c.execute('CREATE TABLE IF NOT EXISTS expenses (Item text NOT NULL, Cost text, Date text NOT NULL)')
            if item_name != '' and item_cost != '':
                c.execute('INSERT INTO expenses (Item, Cost, Date) VALUES (?, ?, ?)', [item_name, item_cost, date])
            else:
                messagebox.showinfo('Warning', 'Please enter the information properly')
            conn.commit()
            conn.close()
        
        submit_button = tk.Button(self, text =  'SUBMIT', command = take_input,  activebackground = 'darkgray', font = (cv2.FONT_HERSHEY_SIMPLEX, 12, ('bold')))
        submit_button.pack(pady = 50)
        
        display_button = tk.Button(self, text = 'Display >>', command = lambda :controller.show_frame(Display_page), activebackground = 'darkgray', font = (cv2.FONT_HERSHEY_SIMPLEX, 12, ('bold')))
        display_button.pack(side = 'right', padx = 10, pady = 10, anchor = 's')

        copy = tk.Text(self,  bg= '#897B94', height = 2, width = 30, fg= 'black', font = (cv2.FONT_HERSHEY_SIMPLEX, 12, ('bold')))
        copy.tag_config('superscript', offset = 3)
        copy.insert('insert', "Designed by Vikas Thapliyal")
        copy.config(state = 'disabled', bg = '#897B94')
        copy.pack(side= 'left', padx = 10, pady = 10, anchor = 's')

        def clear_func():
            conn = sqlite3.connect('storage.db')
            c = conn.cursor()
            c.execute('DELETE FROM expenses')
            conn.commit()
            conn.close()
        clear_button = tk.Button(self, text = 'CLEAR', activebackground = 'darkgray', command = clear_func, font = (cv2.FONT_HERSHEY_SIMPLEX, 12, ('bold')))
        clear_button.pack(pady = 10, side = 'left', anchor = 's')

class New_user(tk.Frame):
    def __init__(self, controller, parent):

        tk.Frame.__init__(self, parent, bg = '#897B94')

        main_label = tk.Label(self, text = 'BILL STORAGE', bg = '#897B94', fg= 'black', font = (cv2.FONT_HERSHEY_SIMPLEX, 50, ('bold underline')))
        main_label.pack(pady = 30)

        label = tk.Label(self, text=  'REGISTRATION', bg = '#897B94', font = (cv2.FONT_HERSHEY_SIMPLEX, 20, 'bold'))
        label.pack(pady = 40)

        user_label = tk.Label(self, text=  'Username', bg = '#897B94', font = (cv2.FONT_HERSHEY_SIMPLEX, 15, 'bold'))
        user_label.pack(pady = 10)

        user = tk.Entry(self, width = 30, bg= 'white', font = (cv2.FONT_HERSHEY_DUPLEX, 15, ('italic')))
        user.pack(pady = 6)

        pass_label = tk.Label(self, text=  'Password', bg = '#897B94', font = (cv2.FONT_HERSHEY_SIMPLEX, 15, 'bold'))
        pass_label.pack(pady = 10)

        password = tk.Entry(self, width = 30, show = '*', bg= 'white', font = (cv2.FONT_HERSHEY_DUPLEX, 15, ('italic')))
        password.pack(pady = 6)

        admin_label = tk.Label(self, text=  'Admin password', bg = '#897B94', font = (cv2.FONT_HERSHEY_SIMPLEX, 15, 'bold'))
        admin_label.pack(pady = 10)

        admin_entry = tk.Entry(self, width = 30, show = '*', bg= 'white', font = (cv2.FONT_HERSHEY_DUPLEX, 15, ('italic')))
        admin_entry.pack(pady = 6)

        def maker():
            username = user.get()
            passs = password.get()
            administrator = admin_entry.get()
            conn = sqlite3.connect('passwords.db')
            c = conn.cursor()
            c.execute('SELECT username FROM user_pass WHERE username == ?', [username])
            rec_user = c.fetchall()
            if rec_user != []:
                messagebox.showinfo('Error', 'Username already exists')
            if administrator != admin:
                messagebox.showinfo('Error', 'Wrong admin password')
            if rec_user == [] and administrator == admin and username != '' and passs != '' and administrator != '':
                conn = sqlite3.connect('passwords.db')
                c = conn.cursor()
                c.execute('CREATE TABLE IF NOT EXISTS user_pass (username text NOT NULL, password text NOT NULL)')
                c.execute('INSERT INTO user_pass (username, password) VALUES (?,?)', [username, passs])
                conn.commit()
                conn.close()

                controller.show_frame(Input_page)
            else:
                pass

        back = tk.Button(self, text = '<< BACK', command = lambda :controller.show_frame(First_page), font= (cv2.FONT_HERSHEY_SIMPLEX, 12, 'bold'))
        back.pack(side = 'bottom', anchor = 'w', padx = 10, pady = 10)

        submit = tk.Button(self, text ='SUBMIT', command = maker, activebackground = 'darkgray', bg = 'white', font =(cv2.FONT_HERSHEY_SIMPLEX, 12, 'bold'))
        submit.pack(pady = 20)

class First_page(tk.Frame):
    def __init__(self, controller, parent):

        tk.Frame.__init__(self, parent, bg = '#897B94')

        main_label = tk.Label(self, text = 'BILL STORAGE', bg = '#897B94', fg= 'black', font = (cv2.FONT_HERSHEY_SIMPLEX, 50, ('bold underline')))
        main_label.pack(pady = 30)

        new_btn = tk.Button(self, text = 'NEW USER',command = lambda : controller.show_frame(New_user), activebackground = 'darkgray', font = (cv2.FONT_HERSHEY_SIMPLEX, 12, 'bold'))
        new_btn.pack(pady = 20)

        return_btn = tk.Button(self, text = 'RETURNING USER',command = lambda :controller.show_frame(Login_page), activebackground = 'darkgray', font = (cv2.FONT_HERSHEY_SIMPLEX, 12, 'bold'))
        return_btn.pack()

      


class Login_page(tk.Frame):

    def __init__(self, controller, parent):

        tk.Frame.__init__(self, parent, bg = '#897B94')
        
        main_label = tk.Label(self, text = 'LOGIN PAGE', bg = '#897B94', font = (cv2.FONT_HERSHEY_SIMPLEX, 30, 'bold underline'))
        main_label.pack(padx =30, pady = 30)

        user_label = tk.Label(self, text=  'Username', bg = '#897B94', font = (cv2.FONT_HERSHEY_SIMPLEX, 15, 'bold'))
        user_label.pack(pady = 10)

        user = tk.Entry(self, width = 30, bg= 'white', font = (cv2.FONT_HERSHEY_DUPLEX, 15, ('italic')))
        user.pack(pady = 6)

        pass_label = tk.Label(self, text=  'Password', bg = '#897B94', font = (cv2.FONT_HERSHEY_SIMPLEX, 15, 'bold'))
        pass_label.pack(pady = 10)

        password = tk.Entry(self, width = 30, show = '*', bg= 'white', font = (cv2.FONT_HERSHEY_DUPLEX, 15, ('italic')))
        password.pack(pady = 6)

        def checker():
            username = user.get()
            passs = password.get()
            conn = sqlite3.connect('passwords.db')
            c = conn.cursor()
            c.execute('SELECT password FROM user_pass WHERE username == ?', [username])
            pass_word = c.fetchone()
            if pass_word == None or pass_word[0] != passs:
                messagebox.showinfo('Error', 'Wrong username or password ')
            try:
                if pass_word != [] and passs == pass_word[0]:
                    controller.show_frame(Input_page)
            except:
                pass

        submit = tk.Button(self, text ='SUBMIT',command = checker, activebackground = 'darkgray', bg = 'white', font =(cv2.FONT_HERSHEY_SIMPLEX, 12, 'bold'))
        submit.pack(pady = 20)

        back = tk.Button(self, text = '<< BACK', command = lambda :controller.show_frame(First_page), font= (cv2.FONT_HERSHEY_SIMPLEX, 12, 'bold'))
        back.pack(side = 'left', padx = 10, pady = 10, anchor = 's')

class Display_page(tk.Frame):

    def __init__(self, controller, parent):
        tk.Frame.__init__(self, parent, bg = '#897B94')

        main_label = tk.Label(self, bg = '#897B94', text = 'EXPENSES', font= (cv2.FONT_HERSHEY_COMPLEX, 30, ('bold')))
        main_label.pack(pady = 15)
        
        canvas = tk.Canvas(self, height = 900, width = 800)
        canvas.pack(pady = 10)

        conn = sqlite3.connect('storage.db')
        c = conn.cursor()
        c.execute('SELECT * FROM expenses')
        details = c.fetchall()
        scroll = tk.Scrollbar(canvas)
        scroll.pack(side = 'right', fill = tk.Y)
        text= tk.Text(canvas, font = (cv2.FONT_HERSHEY_COMPLEX, 20, ('italic')))

        string = '{:<50}{:<20}{:>20}\n\n'.format('Item Name', 'Item Cost', 'Purchase Date')
        for i in details:
            string += '{:<50}{:<20}{:>20}'.format(i[0], i[1], i[2])+'\n'

        text.insert('insert', string)
        scroll.config(command = text.yview)
        text.config(state = 'disabled')
        text.pack(pady =30)

        back = tk.Button(self, text = '<< BACK', command = lambda :controller.show_frame(Input_page), font= (cv2.FONT_HERSHEY_SIMPLEX, 12, 'bold'))
        back.place(x =10, y= 800)






app = MyApp()

def callback():
    if askyesno('Confirm', 'Do you want to quit'):
        app.destroy()

app.title('Windows')
app.protocol('WM_DELETE_WINDOW', callback)

app.mainloop()


