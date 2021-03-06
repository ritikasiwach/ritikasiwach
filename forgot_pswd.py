#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.22
#  in conjunction with Tcl version 8.6
#    Apr 16, 2019 02:38:27 PM IST  platform: Windows NT

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

import forgot_pswd_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    forgot_pswd_support.set_Tk_var()
    top = Toplevel1 (root)
    forgot_pswd_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    forgot_pswd_support.set_Tk_var()
    top = Toplevel1 (w)
    forgot_pswd_support.init(w, top, *args, **kwargs)
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
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1356x689+-5+4")
        top.title("VERIFICATION")
        #top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

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
        self.Canvas1.create_text(190,50,text="Email/Username:",fill="white",font=('bold',25))

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.289, rely=0.050,height=40, relwidth=0.313)
        self.Entry1.configure(background="white")
        self.Entry1.configure(borderwidth="3")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(relief="groove")
        self.Entry1.configure(textvariable=forgot_pswd_support.ent1)
        self.Entry1.insert(0,'Email Id/Username')
        self.Entry1.bind("<FocusIn>",lambda args: self.Entry1.delete('0','end'))

        self.Button1 = tk.Button(self.Canvas1)
        self.Button1.place(x=950,y=35, height=40, width=140)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="red")
        self.Button1.configure(command=forgot_pswd_support.submit)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Segoe UI} -size 18 -weight bold -slant italic")
        self.Button1.configure(foreground="white")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''SUBMIT''')

        self.Button2 = tk.Button(self.Canvas1)
        self.Button2.place(x=350,y=550, height=40, width=140)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="red")
        self.Button2.configure(command=forgot_pswd_support.verify)
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font="-family {Segoe UI} -size 18 -weight bold -slant italic")
        self.Button2.configure(foreground="white")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''VERIFY''')

        self.Button3 = tk.Button(self.Canvas1)
        self.Button3.place(x=790,y=550, height=40, width=140)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="red")
        self.Button3.configure(command=forgot_pswd_support.back)
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(font="-family {Segoe UI} -size 18 -weight bold -slant italic")
        self.Button3.configure(foreground="white")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''BACK''')

        '''self.Labelframe1 = tk.LabelFrame(top)
        self.Labelframe1.place(relx=0.073, rely=0.198, relheight=0.60 , relwidth=0.865)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(font="-family {Segoe UI} -size 13 -weight bold")
        self.Labelframe1.configure(foreground="#ff0f1f")
        self.Labelframe1.configure(text="Security Questions")
        self.Labelframe1.configure(background="#ad63d8")
        self.Labelframe1.configure(width=590)

        self.Label2 = tk.Label(self.Labelframe1)
        self.Label2.place(relx=0.034, rely=0.196, height=21, width=114, bordermode='ignore')
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Label2.configure(foreground="#470fff")
        self.Label2.configure(text="Question # 1")
        self.Label2.configure(width=114)

        self.TCombobox1 = ttk.Combobox(self.Labelframe1)
        self.TCombobox1.place(relx=0.271, rely=0.157, relheight=0.122 , relwidth=0.666, bordermode='ignore')
        self.TCombobox1.configure(font="-family {Segoe UI} -size 12")
        self.TCombobox1.configure(textvariable=forgot_pswd_support.combobox)
        self.TCombobox1.configure(width=393)
        self.TCombobox1.configure(takefocus="")

        self.Label3 = tk.Label(self.Labelframe1)
        self.Label3.place(relx=0.034, rely=0.353, height=21, width=94, bordermode='ignore')
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Label3.configure(foreground="#2026e2")
        self.Label3.configure(text="Answer :")
        self.Label3.configure(width=94)

        self.Label4 = tk.Label(self.Labelframe1)
        self.Label4.place(relx=0.034, rely=0.588, height=21, width=104, bordermode='ignore')
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Label4.configure(foreground="#2026e2")
        self.Label4.configure(text="Question # 2")
        self.Label4.configure(width=104)

        self.TCombobox2 = ttk.Combobox(self.Labelframe1)
        self.TCombobox2.place(relx=0.271, rely=0.549, relheight=0.122, relwidth=0.666, bordermode='ignore')
        self.TCombobox2.configure(font="-family {Segoe UI} -size 12")
        self.TCombobox2.configure(textvariable=forgot_pswd_support.combobox1)
        self.TCombobox2.configure(width=393)
        self.TCombobox2.configure(takefocus="")

        self.Label5 = tk.Label(self.Labelframe1)
        self.Label5.place(relx=0.051, rely=0.745, height=21, width=84, bordermode='ignore')
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Label5.configure(foreground="#441be5")
        self.Label5.configure(text="Answer :")
        self.Label5.configure(width=84)

        self.Entry2 = tk.Entry(self.Labelframe1)
        self.Entry2.place(relx=0.271, rely=0.353, height=35, relwidth=0.668, bordermode='ignore')
        self.Entry2.configure(background="white")
        self.Entry2.configure(borderwidth="3")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(relief="groove")
        self.Entry2.configure(width=394)
        self.Entry2.configure(textvariable=forgot_pswd_support.ent2)
        self.Entry2.insert(0,'Answer')
        self.Entry2.bind("<FocusIn>",lambda args: self.Entry2.delete('0','end'))

        self.Entry3 = tk.Entry(self.Labelframe1)
        self.Entry3.place(relx=0.271, rely=0.745, height=35, relwidth=0.668 , bordermode='ignore')
        self.Entry3.configure(background="white")
        self.Entry3.configure(borderwidth="3")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(relief="groove")
        self.Entry3.configure(textvariable=forgot_pswd_support.ent3)
        self.Entry3.configure(width=394)
        self.Entry3.insert(0,'Answer')
        self.Entry3.bind("<FocusIn>",lambda args: self.Entry3.delete('0','end'))'''
        

if __name__ == '__main__':
    vp_start_gui()





