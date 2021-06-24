#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.20
#  in conjunction with Tcl version 8.6
#    May 08, 2019 02:52:01 PM IST  platform: Windows NT
#    May 15, 2019 01:51:30 PM IST  platform: Windows NT
#    May 15, 2019 02:34:34 PM IST  platform: Windows NT

import sys
import admin
import admin_user_option
import loginpage
import loginpage_support
import newpage_support
import newpage
import viewpage_support
import viewpage
import updatepage_support
import updatepage
import removepage_support
import removepage
import admin_user_option_support
import admin_user_option
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

def login():
    print('ADMINLIST_support.login')
    sys.stdout.flush()

def bacck():
    destroy_window()
    admin_user_option.vp_start_gui()

def questiondelete():
    destroy_window()
    removepage.vp_start_gui()

def questioninsert():
    destroy_window()
    newpage.vp_start_gui()

def questionupdate():
    destroy_window()
    updatepage.vp_start_gui()

def questionview():
    destroy_window()
    viewpage.vp_start_gui()
def loginn():
    destroy_window()
    admin.vp_start_gui()
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
    import ADMINLIST
    ADMINLIST.vp_start_gui()




