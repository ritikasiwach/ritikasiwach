#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.20
#  in conjunction with Tcl version 8.6
#    Apr 19, 2019 01:07:54 PM IST  platform: Windows NT
#    Apr 20, 2019 02:04:09 PM IST  platform: Windows NT

import sys
import removepage
import removepage_support
import viewpage
import viewpage_support
import updatepage
import updatepage_support
import newpage
import newpage_support
import pymysql
import ADMINLIST
import ADMINLIST_support
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
    global optionA
    optionA = tk.StringVar()
    global optionB
    optionB = tk.StringVar()
    global optionC
    optionC = tk.StringVar()
    global optionD
    optionD = tk.StringVar()
    global correct
    correct = tk.StringVar()
    global coursename
    coursename = tk.StringVar()
    global hours
    hours = tk.StringVar()
    global mintues
    mintues = tk.StringVar()
    global seconds
    seconds = tk.StringVar()
    global combobox
    combobox = tk.StringVar()
    global totalquestion
    totalquestion = tk.StringVar()
    global Qnumber
    Qnumber = tk.StringVar()
    global questionwrite
    questionwrite = tk.StringVar()

def new1():
    destroy_window()
    newpage.vp_start_gui()

def nextQ():
    destroy_window()
    ADMINLIST.vp_start_gui()

def remove1():
    destroy_window()
    removepage.vp_start_gui()

def saveQ():
    numbers=Qnumber.get()
    writeq=questionwrite.get()
    a=optionA.get()
    b=optionB.get()
    cp=optionC.get()
    d=optionD.get()
    cor=correct.get()
    course=coursename.get()
    h=hours.get()
    m=mintues.get()
    s=seconds.get()
    comb=combobox.get()
    total=totalquestion.get()
    
    
    
    print(numbers,writeq,a,b,cp,d,cor,course,h,m,s,comb,total)
    db=pymysql.connect("localhost","root","1234","test",3307)
    c=db.cursor()
    sql="insert into question values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(numbers,writeq,a,b,cp,d,cor,course,h,m,s,comb,total)
    c.execute(sql)
    db.commit()
    
def update1():
    destroy_window()
    updatepage.vp_start_gui()

def view1():
    destroy_window()
    viewpage.vp_start_gui()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import newpage
    newpage.vp_start_gui()





