#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.20
#  in conjunction with Tcl version 8.6
#    May 03, 2019 02:14:29 PM IST  platform: Windows NT

import sys
import pymysql
import loginpage
from tkinter import messagebox
from tkinter import *
from tkinter import filedialog
import os
import cv2 as cv

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
    global username
    username = tk.StringVar()
    global idd
    idd = tk.StringVar()
    
    global email
    email = tk.StringVar()
    global password
    password = tk.StringVar()
    global genderr
    genderr=tk.StringVar()
    global Malee
    Malee=tk.StringVar
    global Femalee
    Femalee=tk.StringVar
    
    global imagefield
    imagefield = tk.StringVar()
    global question1
    question1 = tk.StringVar()
    global answer1
    answer1 = tk.StringVar()
    global question2
    question2 = tk.StringVar()
    global answer2
    answer2 = tk.StringVar()
    
    
def backk():
    destroy_window()
    loginpage.vp_start_gui()
def selectt():
    global f
    f=filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    imagefield.set(f)
    filename_w_ext = os.path.basename(f)
    filename, file_extension = os.path.splitext(filename_w_ext)
    #print(filename+file_extension)
    #os.save(filename+file_extension)
    #import os
    #os.save(
    img = cv.imread(f)
    #cv.imshow('Image', img) 
    cv.imwrite(filename+file_extension,img)

def submitt():
    
    print(idd.get())
    print(email.get())
    print(username.get())
    print(password.get())
    print(genderr.get())
    print(imagefield.get())
    print(question1.get())
    print(answer1.get())
    print(question2.get())
    print(answer2.get())
    

    imagefield.set(f)
    filename_w_ext = os.path.basename(f)
    filename, file_extension = os.path.splitext(filename_w_ext)
    print(filename+file_extension)
    #try:
    db=pymysql.connect("localhost","root","1234","test",3307)
    c=db.cursor()
    sql="insert into students values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(username.get(), email.get(), idd.get(), password.get(), question1.get(), answer1.get(), question2.get(), answer2.get(), genderr.get(), imagefield.get())
    c.execute(sql)
    ##print(sql)
    db.commit()
    destroy_window()
    loginpage.vp_start_gui()
    
    #except:
        #messagebox.showinfo('Not Inserted','Opps some error occurr.....')
    

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
    import signupp
    signupp.vp_start_gui()





