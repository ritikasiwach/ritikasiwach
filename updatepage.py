#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.20
#  in conjunction with Tcl version 8.6
#    Apr 19, 2019 01:07:50 PM IST  platform: Windows NT

import sys
import newpage
import viewpage
import removepage
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

import updatepage_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    updatepage_support.set_Tk_var()
    top = Toplevel1 (root)
    updatepage_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    updatepage_support.set_Tk_var()
    top = Toplevel1 (w)
    updatepage_support.init(w, top, *args, **kwargs)
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
        font10 = "-family {Segoe UI} -size 11 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI} -size 11 -weight bold -slant "  \
            "roman -underline 1 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1350x689-5+4")
        top.title("updatepage")
        top.configure(background="#77d8d8")

        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=0.0, rely=0.0,relheight=1.500,relwidth=2.0, height=41, width=454)
        self.Canvas1.configure(selectbackground="#fca367")
        self.Canvas1.configure(selectforeground="#3617ff")
        self.Canvas1.configure(relief="raised")
        self.Canvas1.configure(width=864)
        self.Canvas1.configure(borderwidth="2")
        
        self.img = Image.open("p.jpg")
        self.tkimage = ImageTk.PhotoImage(self.img)
        resized = self.img.resize((1500, 750),Image.ANTIALIAS)
        self.imagee = ImageTk.PhotoImage(resized)

        self.Canvas1.create_image(0,0,image=self.imagee,anchor="nw")
        

        
        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.617, rely=0.189, height=24, width=67)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="red")
        self.Button1.configure(command=updatepage_support.remove1)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font11)
        self.Button1.configure(foreground="white")
        self.Button1.configure(highlightbackground="#d82560")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Remove''')
        self.Button1.configure(width=67)

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.517, rely=0.189, height=24, width=57)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="red")
        self.Button2.configure(command=updatepage_support.update1)
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font=font11)
        self.Button2.configure(foreground="white")
        self.Button2.configure(highlightbackground="#d82560")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Update''')
        self.Button2.configure(width=57)

        self.Button3 = tk.Button(top)
        self.Button3.place(relx=0.442, rely=0.189, height=24, width=47)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="red")
        self.Button3.configure(command=updatepage_support.view1)
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(font=font11)
        self.Button3.configure(foreground="white")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''View''')

        self.Button4 = tk.Button(top)
        self.Button4.place(relx=0.35, rely=0.189, height=24, width=57)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="white")
        self.Button4.configure(background="red")
        self.Button4.configure(command=updatepage_support.new1)
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(font=font11)
        self.Button4.configure(foreground="white")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''New''')
        self.Button4.configure(width=57)

        self.Canvas1.create_text(100,50,text="Question No:",fill="white",font=('bold',15))
        
        

        self.Canvas1.create_text(100,150,text="Question:",fill="white",font=('bold',15))

        

        self.Canvas1.create_text(40,380,text="a)",fill="white",font=('bold',15))


        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.083, rely=0.533,height=20, relwidth=0.64)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(textvariable=updatepage_support.optionA)
        self.Entry1.configure(width=384)

        self.Canvas1.create_text(40,460,text="b)",fill="white",font=('bold',15))

        self.Canvas1.create_text(40,510,text="c)",fill="white",font=('bold',15))

        self.Canvas1.create_text(40,580,text="d)",fill="white",font=('bold',15))

        self.Entry2 = tk.Entry(top)
        self.Entry2.place(relx=0.083, rely=0.644,height=20, relwidth=0.64)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(textvariable=updatepage_support.optionB)
        self.Entry2.configure(width=384)

        self.Entry3 = tk.Entry(top)
        self.Entry3.place(relx=0.075, rely=0.733,height=20, relwidth=0.64)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(textvariable=updatepage_support.optionC)
        self.Entry3.configure(width=384)

        self.Entry4 = tk.Entry(top)
        self.Entry4.place(relx=0.083, rely=0.833,height=20, relwidth=0.64)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(textvariable=updatepage_support.optionD)
        self.Entry4.configure(width=384)

        self.Canvas1.create_text(150,630,text="correct answer",fill="white",font=('bold',15))
        
        self.TCombobox1 = ttk.Combobox(top)
        self.TCombobox1.place(relx=0.233, rely=0.911, relheight=0.047
                , relwidth=0.088)
        self.value_list = ["a","b","c","d",]
        self.TCombobox1.configure(values=self.value_list)
        self.TCombobox1.configure(textvariable=updatepage_support.correct)
        self.TCombobox1.configure(width=53)
        self.TCombobox1.configure(takefocus="")

        self.Canvas1.create_text(1000,50,text="Course Name:",fill="white",font=('bold',15))


        self.Entry5 = tk.Entry(top)
        self.Entry5.place(relx=0.75, rely=0.111,height=20, relwidth=0.223)
        self.Entry5.configure(background="white")
        self.Entry5.configure(disabledforeground="#a3a3a3")
        self.Entry5.configure(font="TkFixedFont")
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(insertbackground="black")
        self.Entry5.configure(textvariable=updatepage_support.coursename)
        self.Entry5.configure(width=134)

        self.Canvas1.create_text(1100,150,text="Time:",fill="white",font=('bold',15))


        self.Entry6 = tk.Entry(top)
        self.Entry6.place(relx=0.758, rely=0.267,height=20, relwidth=0.04)
        self.Entry6.configure(background="white")
        self.Entry6.configure(disabledforeground="#a3a3a3")
        self.Entry6.configure(font="TkFixedFont")
        self.Entry6.configure(foreground="#000000")
        self.Entry6.configure(insertbackground="black")
        self.Entry6.configure(textvariable=updatepage_support.hours)
        self.Entry6.configure(width=24)

        self.Entry7 = tk.Entry(top)
        self.Entry7.place(relx=0.817, rely=0.267,height=20, relwidth=0.057)
        self.Entry7.configure(background="white")
        self.Entry7.configure(disabledforeground="#a3a3a3")
        self.Entry7.configure(font="TkFixedFont")
        self.Entry7.configure(foreground="#000000")
        self.Entry7.configure(insertbackground="black")
        self.Entry7.configure(textvariable=updatepage_support.mintues)
        self.Entry7.configure(width=34)

        self.Entry8 = tk.Entry(top)
        self.Entry8.place(relx=0.892, rely=0.267,height=20, relwidth=0.04)
        self.Entry8.configure(background="white")
        self.Entry8.configure(disabledforeground="#a3a3a3")
        self.Entry8.configure(font="TkFixedFont")
        self.Entry8.configure(foreground="#000000")
        self.Entry8.configure(insertbackground="black")
        self.Entry8.configure(textvariable=updatepage_support.seconds)
        self.Entry8.configure(width=24)

        self.Canvas1.create_text(1100,250,text="Each Marks:",fill="white",font=('bold',15))
    


        self.TCombobox2 = ttk.Combobox(top)
        self.TCombobox2.place(relx=0.883, rely=0.378, relheight=0.047
                , relwidth=0.088)
        self.value_list = [1,2,3,4,5,]
        self.TCombobox2.configure(values=self.value_list)
        self.TCombobox2.configure(textvariable=updatepage_support.combobox)
        self.TCombobox2.configure(width=53)
        self.TCombobox2.configure(takefocus="")

        self.Canvas1.create_text(1100,330,text="Total Question:",fill="white",font=('bold',15))
    

        self.Entry9 = tk.Entry(top)
        self.Entry9.place(relx=0.775, rely=0.511,height=20, relwidth=0.19)
        self.Entry9.configure(background="white")
        self.Entry9.configure(disabledforeground="#a3a3a3")
        self.Entry9.configure(font="TkFixedFont")
        self.Entry9.configure(foreground="#000000")
        self.Entry9.configure(insertbackground="black")
        self.Entry9.configure(textvariable=updatepage_support.totalquestion)
        self.Entry9.configure(width=114)

        self.Button5 = tk.Button(top)
        self.Button5.place(relx=0.817, rely=0.644, height=24, width=55)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="red")
        self.Button5.configure(command=updatepage_support.saveQ)
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(font=font10)
        self.Button5.configure(foreground="white")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''Save''')
        self.Button5.configure(width=55)

        self.Button6 = tk.Button(top)
        self.Button6.place(relx=0.883, rely=0.711, height=24, width=55)
        self.Button6.configure(activebackground="#ececec")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="red")
        self.Button6.configure(command=updatepage_support.nextQ)
        self.Button6.configure(disabledforeground="#a3a3a3")
        self.Button6.configure(font=font10)
        self.Button6.configure(foreground="white")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(text='''Back''')
        self.Button6.configure(width=55)

        self.TCombobox3 = ttk.Combobox(top)
        self.TCombobox3.place(relx=0.183, rely=0.033, relheight=0.047
                , relwidth=0.238)
        self.value_list = ["1","2","3","4","5","6","7","8","9","10",]
        self.TCombobox3.configure(values=self.value_list)
        self.TCombobox3.configure(textvariable=updatepage_support.Qnumber)
        self.TCombobox3.configure(takefocus="")
        self.TCombobox3.bind("<<ComboboxSelected>>", updatepage_support.callback)


        

        self.Scrolledentry1 = ScrolledEntry(top)
        self.Scrolledentry1.place(relx=0.083, rely=0.244, height=106
                , relwidth=0.64)
        self.Scrolledentry1.configure(background="white")
        self.Scrolledentry1.configure(disabledforeground="#a3a3a3")
        self.Scrolledentry1.configure(foreground="black")
        self.Scrolledentry1.configure(highlightbackground="#d9d9d9")
        self.Scrolledentry1.configure(highlightcolor="black")
        self.Scrolledentry1.configure(insertbackground="black")
        self.Scrolledentry1.configure(insertborderwidth="1")
        self.Scrolledentry1.configure(selectbackground="#c4c4c4")
        self.Scrolledentry1.configure(selectforeground="black")
        self.Scrolledentry1.configure(textvariable=updatepage_support.questionwrite)
        self.Scrolledentry1.configure(width=15)

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                  + tk.Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledEntry(AutoScroll, tk.Entry):
    '''A standard Tkinter Entry widget with a horizontal scrollbar
    that will automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Entry.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == '__main__':
    vp_start_gui()






