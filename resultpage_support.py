#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.20
#  in conjunction with Tcl version 8.6
#    Apr 29, 2019 02:32:30 PM IST  platform: Windows NT

import sys
import pymysql

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
    global mailfield
    mailfield = tk.StringVar()
    global marksfield
    marksfield = tk.StringVar()
    global field
    field = tk.StringVar()
    
    
def Show():
    db=pymysql.connect("localhost","root","1234","test",3309)
    c=db.cursor()
    sql=("select * from testtime where student_id='%s'"%(mailfield.get()))
    c.execute(sql)
    result=c.fetchall()
    #print(result)

    correct=[]
    question_no=[]
    counter=0
    
    answer=[]
    question_id=[]
    
    for x in result:
        answer.append(x[2])
        question_id.append(x[1])
        db=pymysql.connect("localhost","root","1234","test",3309)
        c1=db.cursor()
        sql1="select * from question where question_number='"+x[1]+"'"
        c1.execute(sql1)
        result1=c1.fetchall()
        for x in result1:
            correct.append(x[6])
            question_no.append(x[0])
            print(correct,question_no)
            print(len(question_no))
        #field.set(len(question_number))
            
    
    
    
        print(answer,question_id)
    for x in range(0,len(question_no)):
        if answer[x]==correct[x]:
            counter=counter+1
        print(counter)
    marksfield.set(counter)

        


    db=pymysql.connect("localhost","root","1234","test",3309)
    c2=db.cursor()
    sql2="select * from question"
    c2.execute(sql2)
    result2=c2.fetchall()
    #print(result1)
    #correct=[]
    questionnumber=[]
    
    #counter=0
    
    for x in result2:
        #correct.append(x[6])
        questionnumber.append(x[0])
        print(len(questionnumber))
    field.set(len(questionnumber))



      
             #messagebox.showinfo('Result Error','RESULT NOT FOUND.....')
            
    
def logoutt():
    destroy_window()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    marksfield.set(0)
    for arg in args:
        mailfield.set(arg)
    

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import resultpage
    resultpage.vp_start_gui()





