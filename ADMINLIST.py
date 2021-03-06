#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.20
#  in conjunction with Tcl version 8.6
#    May 15, 2019 02:47:22 PM IST  platform: Windows NT

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

import ADMINLIST_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    ADMINLIST_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    ADMINLIST_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = 'red'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = 'red' # X11 color: 'gray85'
        _ana1color = 'red' # X11 color: 'gray85' 
        _ana2color = '#ececec' # Closest X11 color: 'gray92' 
        font9 = "-family Arial -size 9 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        font11 = "-family {Segoe UI Black} -size 13 -weight bold "  \
            "-slant italic -underline 0 -overstrike 0"


        top.geometry("1350x989-5+4")
        top.title("New Toplevel")
        top.configure(background="red")
        top.configure(highlightbackground="red")
        top.configure(highlightcolor="black")

        
        self.img = Image.open("pp.jpg")
        self.tkimage = ImageTk.PhotoImage(self.img)
        resized = self.img.resize((1474, 884),Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(resized) # Keep a reference, prevent GC
        '''self.Label = tk.Label(top)
        self.Label(top,image =self.image,height=750,width=1500,bg="purple").place(x=1,y=1)'''
        
        self.Label0=tk.Label(top)
        self.Label0.place(x=1,y=1)
        self.Label0.configure(background="purple")
        self.Label0.configure(height=884,width=1474)
        self.Label0.configure(image =self.image)


        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.017, rely=0.022, height=24, width=147)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="red")
        self.Button1.configure(command=ADMINLIST_support.questionview)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font11)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="red")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''QUESTION VIEW''')

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.15, rely=0.156, height=24, width=177)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="red")
        self.Button2.configure(command=ADMINLIST_support.questionupdate)
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font=font11)
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="red")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''QUESTION UPDATE''')

        self.Button3 = tk.Button(top)
        self.Button3.place(relx=0.317, rely=0.289, height=24, width=177)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="red")
        self.Button3.configure(command=ADMINLIST_support.questiondelete)
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(font=font11)
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="red")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''QUESTION DELETE''')

        self.Button4 = tk.Button(top)
        self.Button4.place(relx=0.467, rely=0.422, height=24, width=177)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="red")
        self.Button4.configure(command=ADMINLIST_support.questioninsert)
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(font=font11)
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="red")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''QUESTION INSERT''')

        self.Button5 = tk.Button(top)
        self.Button5.place(relx=0.633, rely=0.578, height=24, width=137)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="red")
        self.Button5.configure(command=ADMINLIST_support.login)
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(font=font11)
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="red")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''LOGIN''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Button6 = tk.Button(top)
        self.Button6.place(relx=0.8, rely=0.733, height=24, width=107)
        self.Button6.configure(activebackground="#ececec")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="red")
        self.Button6.configure(command=ADMINLIST_support.bacck)
        self.Button6.configure(disabledforeground="#a3a3a3")
        self.Button6.configure(font=font11)
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="red")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(text='''BACK''')

if __name__ == '__main__':
    vp_start_gui()





