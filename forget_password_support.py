#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.20
#  in conjunction with Tcl version 8.6
#    Apr 08, 2019 10:28:09 AM IST  platform: Windows NT
#    Apr 10, 2019 02:12:46 PM IST  platform: Windows NT
#    Apr 10, 2019 02:37:47 PM IST  platform: Windows NT

import sys
import pymysql
import forgot_pswd
import loginpage
from tkinter import messagebox
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def set_Tk_var():
    global ent1
    ent1 = tk.StringVar()
    global ent2
    ent2 = tk.StringVar()
    global ent0
    ent0=tk.StringVar()
    
def submit():
    print("hello")
    password=ent1.get()
    print(password)
    new=ent2.get()
    print(new)
    print(ent0.get())
    
    try:
        db=pymysql.connect("localhost","root","1234","test",3307)
        c=db.cursor()
        sql=("UPDATE students SET password = '%s' WHERE email = '%s'"%(password,ent0.get()))
        c.execute(sql)
        destroy_window()
        loginpage.vp_start_gui()
        db.commit()
    except:
        messagebox.showinfo('field not update')
        #print("error")
        
def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    for arg in args:
        ent0.set(arg)

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import forget_password
    forget_password.vp_start_gui()




