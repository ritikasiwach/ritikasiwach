#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.20
#  in conjunction with Tcl version 8.6
#    May 08, 2019 02:23:02 PM IST  platform: Windows NT

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

import admin_user_option_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    admin_user_option_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    admin_user_option_support.init(w, top, *args, **kwargs)
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
        font9 = "-family {Segoe UI} -size 12 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"

        top.geometry("1350x689-5+4")
        top.title("admin_user_option")
        top.configure(background="#d9d9d9")

        self.img=Image.open("bbk.jpg")
        self.tkimage=ImageTk.PhotoImage(self.img)
        resized=self.img.resize((1500,750),Image.ANTIALIAS)
        self.image=ImageTk.PhotoImage(resized)

        self.Label=tk.Label(top)
        self.Label.place(x=1,y=1)
        self.Label.configure(background="purple")
        self.Label.configure(height=750,width=1500)
        self.Label.configure(image=self.image)

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.05, rely=0.422, height=34, width=207)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(command=admin_user_option_support.adminn)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font9)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''ADMIN''')
        self.Button1.configure(width=207)

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.567, rely=0.422, height=34, width=227)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(command=admin_user_option_support.userr)
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font=font9)
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''STUDENT''')
        self.Button2.configure(width=227)

if __name__ == '__main__':
    vp_start_gui()





