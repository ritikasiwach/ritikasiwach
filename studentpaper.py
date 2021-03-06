#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.20
#  in conjunction with Tcl version 8.6
#    May 02, 2019 12:19:43 PM IST  platform: Windows NT

import sys
from PIL import Image,ImageTk
#import admin_user_option
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

import studentpaper_support

def vp_start_gui(*args):
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    studentpaper_support.set_Tk_var()
    top = Toplevel1 (root)
    studentpaper_support.init(root, top,*args)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    studentpaper_support.set_Tk_var()
    top = Toplevel1 (w)
    studentpaper_support.init(w, top, *args, **kwargs)
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
                 
        font10 = "-family {Showcard Gothic} -size 10 -weight bold "  \

        font9 = "-family {Segoe UI} -size 10 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1350x689-5+4")
        top.title("New Toplevel")
        top.configure(background="#122aff")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=0.0, rely=0.0,relheight=1.500,relwidth=2.0, height=41, width=454)
        self.Canvas1.configure(selectbackground="#fca367")
        self.Canvas1.configure(selectforeground="#3617ff")
        self.Canvas1.configure(relief="raised")
        self.Canvas1.configure(width=864)
        self.Canvas1.configure(borderwidth="2")
        
        self.img = Image.open("bbk.jpg")
        self.tkimage = ImageTk.PhotoImage(self.img)
        resized = self.img.resize((1500, 750),Image.ANTIALIAS)
        self.imagee = ImageTk.PhotoImage(resized)

        self.Canvas1.create_image(0,0,image=self.imagee,anchor="nw")


        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.314, rely=0.874, height=24, width=177)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="red")
        self.Button2.configure(command=studentpaper_support.Submit)
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font=font11)
        self.Button2.configure(foreground="white")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Submit''')

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.046, rely=0.182, height=111, width=910)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="brown")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="white")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Label''')
        self.Label1.configure(font=font11)
        self.Label1.configure(textvariable=studentpaper_support.question)
        self.Label1.configure(wraplength=660)
        

        

        self.Radiobutton1 = tk.Radiobutton(top)
        self.Radiobutton1.place(relx=0.097, rely=0.427, relheight=0.051
                , relwidth=0.505)
        self.Radiobutton1.configure(activebackground="#ececec")
        self.Radiobutton1.configure(activeforeground="#000000")
        self.Radiobutton1.configure(background="brown")
        
        self.Radiobutton1.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1.configure(foreground="black")
        self.Radiobutton1.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1.configure(highlightcolor="black")
        self.Radiobutton1.configure(anchor='w')
        self.Radiobutton1.configure(text='''radio''')
        self.Radiobutton1.configure(font=font11)
        self.Radiobutton1.configure(textvariable=studentpaper_support.option1)
        self.Radiobutton1.configure(studentpaper_support.option1.set(0))
        self.Radiobutton1.configure(value='a')
        self.Radiobutton1.configure(var=studentpaper_support.option)

        self.Radiobutton2 = tk.Radiobutton(top)
        self.Radiobutton2.place(relx=0.097, rely=0.508, relheight=0.051
                , relwidth=0.505)
        self.Radiobutton2.configure(activebackground="#ececec")
        self.Radiobutton2.configure(activeforeground="#000000")
        self.Radiobutton2.configure(background="brown")
        self.Radiobutton2.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2.configure(anchor='w')
        self.Radiobutton2.configure(foreground="black")
        self.Radiobutton2.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2.configure(highlightcolor="black")
        self.Radiobutton2.configure(justify='left')
        self.Radiobutton2.configure(text='''radio''')
        self.Radiobutton2.configure(font=font11)
        self.Radiobutton2.configure(textvariable=studentpaper_support.option2)
        self.Radiobutton2.configure(studentpaper_support.option2.set(0))
        self.Radiobutton2.configure(var=studentpaper_support.option)
        self.Radiobutton2.configure(value='b')

        self.Radiobutton3 = tk.Radiobutton(top)
        self.Radiobutton3.place(relx=0.097, rely=0.6, relheight=0.051
                , relwidth=0.505)
        self.Radiobutton3.configure(activebackground="#ececec")
        self.Radiobutton3.configure(activeforeground="#000000")
        self.Radiobutton3.configure(background="brown")
        self.Radiobutton3.configure(disabledforeground="#a3a3a3")
        self.Radiobutton3.configure(foreground="black")
        self.Radiobutton3.configure(highlightbackground="#d9d9d9")
        self.Radiobutton3.configure(highlightcolor="black")
        self.Radiobutton3.configure(justify='left')
        self.Radiobutton3.configure(anchor='w')
        self.Radiobutton3.configure(font=font11)
        self.Radiobutton3.configure(text='''radio''')
        self.Radiobutton3.configure(textvariable=studentpaper_support.option3)
        self.Radiobutton3.configure(studentpaper_support.option3.set(0))
        self.Radiobutton3.configure(var=studentpaper_support.option)
        self.Radiobutton3.configure(value='c')

        self.Radiobutton4 = tk.Radiobutton(top)
        self.Radiobutton4.place(relx=0.097, rely=0.681, relheight=0.051
                , relwidth=0.505)
        self.Radiobutton4.configure(activebackground="#ececec")
        self.Radiobutton4.configure(activeforeground="#000000")
        self.Radiobutton4.configure(background="brown")
        self.Radiobutton4.configure(disabledforeground="#a3a3a3")
        self.Radiobutton4.configure(foreground="black")
        self.Radiobutton4.configure(highlightbackground="#d9d9d9")
        self.Radiobutton4.configure(highlightcolor="black")
        self.Radiobutton4.configure(justify='left')
        self.Radiobutton4.configure(text='''radio''')
        self.Radiobutton4.configure(anchor='w')
        self.Radiobutton4.configure(font=font11)
        self.Radiobutton4.configure(textvariable=studentpaper_support.option4)
        self.Radiobutton4.configure(studentpaper_support.option4.set(0))

        self.Radiobutton4.configure(var=studentpaper_support.option)
        self.Radiobutton4.configure(value='d')

        self.Button4 = tk.Button(top)
        self.Button4.place(relx=0.097, rely=0.854, height=24, width=97)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="red")
        self.Button4.configure(command=studentpaper_support.previous)
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(font=font11)
        self.Button4.configure(foreground="white")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Previous''')

        self.Button5 = tk.Button(top)
        self.Button5.place(relx=0.694, rely=0.854, height=24, width=97)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="red")
        self.Button5.configure(command=studentpaper_support.next)
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(font=font11)
        self.Button5.configure(foreground="white")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''Next''')

        
        self.Canvas1.create_text(1090,290,text="Question No.",fill="red",font=('bold',25))


                

        '''self.TCombobox1 = ttk.Combobox(top)
        self.TCombobox1.place(relx=0.877, rely=0.244, relheight=0.043
                , relwidth=0.082)
        self.value_list = ["AP1","AP2","AP3","AP4","AP5","AP6","AP7","AP8","AP9","AP10",]
        self.TCombobox1.configure(values=self.value_list)
        self.TCombobox1.configure(textvariable=studentpaper_support.questionumber)
        self.TCombobox1.configure(takefocus="")'''

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.785, rely=0.508, height=21, width=124)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="brown")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''''')
        self.Label3.configure(font=font11)
        self.Label3.configure(textvariable=studentpaper_support.ok)

        self.Canvas1.create_text(100,50,text="Email",fill="red",font=('bold',25))

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.209, rely=0.061,height=30, relwidth=0.215)
        self.Entry1.configure(background="brown")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="font9")
        self.Entry1.configure(foreground="white")
        self.Entry1.configure(font=font11)
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(textvariable=studentpaper_support.emailentry)

        self.Button6 = tk.Button(top)
        self.Button6.place(relx=0.494, rely=0.874, height=24, width=177)
        self.Button6.configure(activebackground="#ececec")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="red")
        self.Button6.configure(command=studentpaper_support.finish)
        self.Button6.configure(disabledforeground="#a3a3a3")
        self.Button6.configure(font=font11)
        self.Button6.configure(foreground="white")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(text='''Finish''')  #(relx=0.314, rely=0.874, height=24, width=177)


if __name__ == '__main__':
    vp_start_gui()





