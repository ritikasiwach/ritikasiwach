#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.20
#  in conjunction with Tcl version 8.6
#    Apr 10, 2019 02:37:56 PM IST  platform: Windows NT

import sys
from PIL import Image,ImageTk
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

import forget_password_support

def vp_start_gui(*args):
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    forget_password_support.set_Tk_var()
    top = Toplevel1 (root)
    forget_password_support.init(root, top,*args)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    forget_password_support.set_Tk_var(*args)
    top = Toplevel1 (w)
    forget_password_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font11 = "-family {Segoe UI Black} -size 13 -weight bold "  \
            "-slant italic -underline 0 -overstrike 0"
        font10 = "-family {Showcard Gothic} -size 20 -weight bold "  \
            "-slant italic -underline 1 -overstrike 0"
        


        top.geometry("1350x689-5+4")
        top.title("forgetpge")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        '''self.img=Image.open("wel.jpg")
        self.tkimage=ImageTk.PhotoImage(self.img)
        resized=self.img.resize((1500,750),Image.ANTIALIAS)
        self.image=ImageTk.PhotoImage(resized)

        self.Label=tk.Label(top)
        self.Label.place(x=1,y=1)
        self.Label.configure(background="purple")
        self.Label.configure(height=750,width=1500)
        self.Label.configure(image=self.image)'''

        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=0.0, rely=0.0,relheight=1.500,relwidth=2.0, height=41, width=454)
        self.Canvas1.configure(selectbackground="#fca367")
        self.Canvas1.configure(selectforeground="#3617ff")
        self.Canvas1.configure(relief="raised")
        self.Canvas1.configure(width=864)
        self.Canvas1.configure(borderwidth="2")
        
        self.img = Image.open("pp.jpg")
        self.tkimage = ImageTk.PhotoImage(self.img)
        resized = self.img.resize((1500, 750),Image.ANTIALIAS)
        self.imagee = ImageTk.PhotoImage(resized)

        self.Canvas1.create_image(0,0,image=self.imagee,anchor="nw")
        self.Canvas1.create_text(290,120,text="Password:",fill="white",font=('bold',25))
        self.Canvas1.create_text(290,420,text=" Email:",fill="white",font=('bold',25))


        '''self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.044, rely=0.178, height=31, width=104)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="brown")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="white")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text=Password)'''


        
        self.Entry0 = tk.Entry(top)
        self.Entry0.place(relx=0.45, rely=0.578,height=50, relwidth=0.495)
        self.Entry0.configure(background="black")
        self.Entry0.configure(disabledforeground="#a3a3a3")
        self.Entry0.configure(font="TkFixedFont")
        self.Entry0.configure(foreground="white")
        self.Entry0.configure(highlightbackground="#d9d9d9")
        self.Entry0.configure(highlightcolor="black")
        self.Entry0.configure(insertbackground="black")
        self.Entry0.configure(selectbackground="#c4c4c4")
        self.Entry0.configure(font=font11)
        self.Entry0.configure(selectforeground="black")
        self.Entry0.configure(textvariable=forget_password_support.ent0)


        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.45, rely=0.156,height=50, relwidth=0.495)
        self.Entry1.configure(background="black")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="white")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")
        self.Entry1.configure(font=font11)
        self.Entry1.configure(textvariable=forget_password_support.ent1)

        '''self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.054, rely=0.578, height=31, width=104)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="black")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="white")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text=Confirm Password)'''

        '''self.Entry2 = tk.Entry(top)
        self.Entry2.place(relx=0.45, rely=0.578,height=50, relwidth=0.495)
        self.Entry2.configure(background="brown")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="#c4c4c4")
        self.Entry2.configure(selectforeground="black")
        self.Entry2.configure(textvariable=forget_password_support.ent2)'''

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.400 ,rely=0.821, height=44, width=297)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="red")
        self.Button1.configure(command=forget_password_support.submit)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="white")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(font=font10)
        self.Button1.configure(text='''SUBMIT''')

if __name__ == '__main__':
    vp_start_gui()





