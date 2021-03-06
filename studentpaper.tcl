#############################################################################
# Generated by PAGE version 4.20
#  in conjunction with Tcl version 8.6
#  May 02, 2019 12:20:17 PM IST  platform: Windows NT
set vTcl(timestamp) ""


if {!$vTcl(borrow)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(active_menu_fg) #000000
}

#############################################################################
# vTcl Code to Load User Fonts

vTcl:font:add_font \
    "-family {Segoe UI} -size 10 -weight bold -slant roman -underline 0 -overstrike 0" \
    user \
    vTcl:font9
#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top42
    global vTcl
    set base $vTcl(btop)
    if {$base == ""} {
        set base .top42
    }
    namespace eval ::widgets::$base {
        set dflt,origin 0
        set runvisible 1
    }
    namespace eval ::widgets_bindings {
        set tagslist _TopLevel
    }
    namespace eval ::vTcl::modules::main {
        set procs {
        }
        set compounds {
        }
        set projectType single
    }
}
}

#################################
# GENERATED GUI PROCEDURES
#

proc vTclWindow.top42 {base} {
    if {$base == ""} {
        set base .top42
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m43" -background {#122aff} -highlightbackground {#d9d9d9} \
        -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 764x492+330+152
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1362 741
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "New Toplevel"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set site_3_0 $top.m43
    menu $site_3_0 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -font TkMenuFont -foreground {#000000} \
        -tearoff 0 
    button $top.but45 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -command apptitute \
        -disabledforeground {#a3a3a3} -font $::vTcl(fonts,vTcl:font9,object) \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -text Apptitute 
    vTcl:DefineAlias "$top.but45" "Button2" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab49 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Label \
        -textvariable question 
    vTcl:DefineAlias "$top.lab49" "Label1" vTcl:WidgetProc "Toplevel1" 1
    radiobutton $top.rad50 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -command optiona -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text radio -textvariable option1 -variable {} 
    vTcl:DefineAlias "$top.rad50" "Radiobutton1" vTcl:WidgetProc "Toplevel1" 1
    radiobutton $top.rad51 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -command optionb -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text radio -textvariable option2 -variable {} 
    vTcl:DefineAlias "$top.rad51" "Radiobutton2" vTcl:WidgetProc "Toplevel1" 1
    radiobutton $top.rad52 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -command optionc -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text radio -textvariable option3 -variable {} 
    vTcl:DefineAlias "$top.rad52" "Radiobutton3" vTcl:WidgetProc "Toplevel1" 1
    radiobutton $top.rad53 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -command optiond -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text radio -textvariable option4 -variable {} 
    vTcl:DefineAlias "$top.rad53" "Radiobutton4" vTcl:WidgetProc "Toplevel1" 1
    button $top.but59 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -command previous -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font9,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text Previous 
    vTcl:DefineAlias "$top.but59" "Button4" vTcl:WidgetProc "Toplevel1" 1
    button $top.but60 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -command next -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font9,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text Next 
    vTcl:DefineAlias "$top.but60" "Button5" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab43 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font9,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Question No.} 
    vTcl:DefineAlias "$top.lab43" "Label2" vTcl:WidgetProc "Toplevel1" 1
    ttk::combobox $top.tCo44 \
        \
        -values {{"AP1"} {"AP2"} {"AP3"} {"AP4"} {"AP5"} {"AP6"} {"AP7"} {"AP8"} {"AP9"} {"AP10"} {}} \
        -font TkTextFont -textvariable questionumber -foreground {} \
        -background {} -takefocus {} 
    vTcl:DefineAlias "$top.tCo44" "TCombobox1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab44 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Label 
    vTcl:DefineAlias "$top.lab44" "Label3" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab45 \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} -text Email 
    vTcl:DefineAlias "$top.lab45" "Label4" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent46 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -insertbackground black 
    vTcl:DefineAlias "$top.ent46" "Entry1" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.but45 \
        -in $top -x 240 -y 430 -width 177 -relwidth 0 -height 24 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab49 \
        -in $top -x 22 -y 70 -width 610 -relwidth 0 -height 111 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.rad50 \
        -in $top -x 10 -y 212 -width 538 -relwidth 0 -height 25 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.rad51 \
        -in $top -x 10 -y 253 -width 539 -relwidth 0 -height 25 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.rad52 \
        -in $top -x 8 -y 295 -width 548 -relwidth 0 -height 25 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.rad53 \
        -in $top -x 9 -y 335 -width 548 -relwidth 0 -height 25 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but59 \
        -in $top -x 30 -y 420 -width 97 -relwidth 0 -height 24 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but60 \
        -in $top -x 530 -y 430 -width 97 -relwidth 0 -height 24 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab43 \
        -in $top -x 660 -y 80 -width 84 -relwidth 0 -height 41 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tCo44 \
        -in $top -x 671 -y 120 -width 63 -relwidth 0 -height 21 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab44 \
        -in $top -x 600 -y 250 -width 124 -relwidth 0 -height 21 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab45 \
        -in $top -x 20 -y 30 -width 84 -relwidth 0 -height 21 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent46 \
        -in $top -x 162 -y 30 -width 164 -height 20 -anchor nw \
        -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

#############################################################################
## Binding tag:  _TopLevel

bind "_TopLevel" <<Create>> {
    if {![info exists _topcount]} {set _topcount 0}; incr _topcount
}
bind "_TopLevel" <<DeleteWindow>> {
    if {[set ::%W::_modal]} {
                vTcl:Toplevel:WidgetProc %W endmodal
            } else {
                destroy %W; if {$_topcount == 0} {exit}
            }
}
bind "_TopLevel" <Destroy> {
    if {[winfo toplevel %W] == "%W"} {incr _topcount -1}
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top42 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

