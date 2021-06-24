#############################################################################
# Generated by PAGE version 4.20
#  in conjunction with Tcl version 8.6
#  Apr 20, 2019 02:34:23 PM IST  platform: Windows NT
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
    "-family {Segoe UI} -size 11 -weight bold -slant roman -underline 1 -overstrike 0" \
    user \
    vTcl:font10
vTcl:font:add_font \
    "-family {Segoe UI} -size 11 -weight bold -slant roman -underline 0 -overstrike 0" \
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
        -background {#d82906} -highlightbackground {#d9d9d9} \
        -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 600x450+188+246
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
    wm title $top "Newpage"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    button $top.but44 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d82906} -command remove1 -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font10,object) -foreground white \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text Remove 
    vTcl:DefineAlias "$top.but44" "Button1" vTcl:WidgetProc "Toplevel1" 1
    button $top.but45 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d82906} -command update1 -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font10,object) -foreground white \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text Update 
    vTcl:DefineAlias "$top.but45" "Button2" vTcl:WidgetProc "Toplevel1" 1
    button $top.but46 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d82906} -command view1 -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font10,object) -foreground white \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text View 
    vTcl:DefineAlias "$top.but46" "Button3" vTcl:WidgetProc "Toplevel1" 1
    button $top.but47 \
        -activebackground {#ececec} -activeforeground white \
        -background {#d82906} -command new1 -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font10,object) -foreground white \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text New 
    vTcl:DefineAlias "$top.but47" "Button4" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab48 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d82906} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font9,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Question No.} 
    vTcl:DefineAlias "$top.lab48" "Label1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab49 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d82906} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font9,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Question 
    vTcl:DefineAlias "$top.lab49" "Label2" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab50 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d82906} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font9,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text a) 
    vTcl:DefineAlias "$top.lab50" "Label3" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent51 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$top.ent51" "Entry1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab52 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d82906} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font9,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text b) 
    vTcl:DefineAlias "$top.lab52" "Label4" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab53 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d82906} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font9,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text c) 
    vTcl:DefineAlias "$top.lab53" "Label5" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab54 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d82906} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font9,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text d) 
    vTcl:DefineAlias "$top.lab54" "Label6" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent55 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$top.ent55" "Entry2" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent56 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$top.ent56" "Entry3" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent57 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$top.ent57" "Entry4" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab58 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d82906} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font9,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {correct answer} 
    vTcl:DefineAlias "$top.lab58" "Label7" vTcl:WidgetProc "Toplevel1" 1
    ttk::combobox $top.tCo61 \
        -values {{"a"} {"b"} {"c"} {"d"}} -font TkTextFont \
        -textvariable correct -foreground {} -background {} -takefocus {} 
    vTcl:DefineAlias "$top.tCo61" "TCombobox1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab62 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d82906} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font9,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Course Name} 
    vTcl:DefineAlias "$top.lab62" "Label8" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent63 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$top.ent63" "Entry5" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab64 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d82906} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font9,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Time 
    vTcl:DefineAlias "$top.lab64" "Label9" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent65 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$top.ent65" "Entry6" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent66 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$top.ent66" "Entry7" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent67 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$top.ent67" "Entry8" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab68 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d82906} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font9,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Each Marks} 
    vTcl:DefineAlias "$top.lab68" "Label10" vTcl:WidgetProc "Toplevel1" 1
    ttk::combobox $top.tCo69 \
        -values {1 2 3 4 5} -font TkTextFont -textvariable combobox \
        -foreground {} -background {} -takefocus {} 
    vTcl:DefineAlias "$top.tCo69" "TCombobox2" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab70 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d82906} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font9,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Total Question} 
    vTcl:DefineAlias "$top.lab70" "Label11" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent71 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$top.ent71" "Entry9" vTcl:WidgetProc "Toplevel1" 1
    button $top.but72 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background red -command saveQ -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font9,object) -foreground white \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text Save 
    vTcl:DefineAlias "$top.but72" "Button5" vTcl:WidgetProc "Toplevel1" 1
    button $top.but73 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background red -command nextQ -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font9,object) -foreground white \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text Next 
    vTcl:DefineAlias "$top.but73" "Button6" vTcl:WidgetProc "Toplevel1" 1
    ttk::combobox $top.tCo74 \
        \
        -values {{"AP1"} {"AP2"} {"AP3"} {"AP4"} {"AP5"} {"AP6"} {"AP7"} {"AP8"} {"AP9"} {"AP10"}} \
        -font TkTextFont -textvariable Qnumber -foreground {} -background {} \
        -takefocus {} 
    vTcl:DefineAlias "$top.tCo74" "TCombobox3" vTcl:WidgetProc "Toplevel1" 1
    vTcl::widgets::ttk::scrolledentry::CreateCmd $top.scr43 \
        -background {#d9d9d9} -height 106 -highlightbackground {#d9d9d9} \
        -highlightcolor black -width 384 
    vTcl:DefineAlias "$top.scr43" "Scrolledentry1" vTcl:WidgetProc "Toplevel1" 1

    $top.scr43.01 configure -background white \
        -disabledforeground #a3a3a3 \
        -foreground black \
        -highlightbackground #d9d9d9 \
        -highlightcolor black \
        -insertbackground black \
        -insertborderwidth 1 \
        -selectbackground #c4c4c4 \
        -selectforeground black \
        -textvariable questionwrite \
        -width 15
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.but44 \
        -in $top -x 371 -y 86 -width 67 -relwidth 0 -height 24 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but45 \
        -in $top -x 314 -y 87 -width 57 -relwidth 0 -height 24 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but46 \
        -in $top -x 267 -y 86 -width 47 -height 24 -anchor nw \
        -bordermode ignore 
    place $top.but47 \
        -in $top -x 210 -y 86 -width 57 -relwidth 0 -height 24 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab48 \
        -in $top -x 10 -y 20 -width 94 -relwidth 0 -height 21 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab49 \
        -in $top -x 26 -y 84 -width 114 -relwidth 0 -height 21 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab50 \
        -in $top -x 18 -y 240 -width 16 -height 21 -anchor nw \
        -bordermode ignore 
    place $top.ent51 \
        -in $top -x 50 -y 240 -width 384 -relwidth 0 -height 20 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab52 \
        -in $top -x 17 -y 280 -width 21 -height 26 -anchor nw \
        -bordermode ignore 
    place $top.lab53 \
        -in $top -x 18 -y 320 -width 19 -height 26 -anchor nw \
        -bordermode ignore 
    place $top.lab54 \
        -in $top -x 17 -y 370 -width 21 -height 26 -anchor nw \
        -bordermode ignore 
    place $top.ent55 \
        -in $top -x 50 -y 290 -width 384 -relwidth 0 -height 20 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent56 \
        -in $top -x 49 -y 330 -width 384 -relwidth 0 -height 20 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent57 \
        -in $top -x 50 -y 375 -width 384 -relwidth 0 -height 20 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab58 \
        -in $top -x 30 -y 410 -anchor nw -bordermode ignore 
    place $top.tCo61 \
        -in $top -x 140 -y 410 -width 53 -relwidth 0 -height 21 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab62 \
        -in $top -x 455 -y 28 -width 94 -relwidth 0 -height 21 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent63 \
        -in $top -x 450 -y 50 -width 134 -relwidth 0 -height 20 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab64 \
        -in $top -x 480 -y 95 -width 54 -relwidth 0 -height 21 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent65 \
        -in $top -x 456 -y 123 -width 24 -relwidth 0 -height 20 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent66 \
        -in $top -x 492 -y 123 -width 34 -relwidth 0 -height 20 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent67 \
        -in $top -x 539 -y 122 -width 24 -relwidth 0 -height 20 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab68 \
        -in $top -x 435 -y 170 -width 94 -relwidth 0 -height 21 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tCo69 \
        -in $top -x 534 -y 170 -width 53 -relwidth 0 -height 21 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab70 \
        -in $top -x 470 -y 210 -width 114 -relwidth 0 -height 21 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent71 \
        -in $top -x 467 -y 230 -width 114 -relwidth 0 -height 20 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but72 \
        -in $top -x 490 -y 290 -width 55 -relwidth 0 -height 24 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but73 \
        -in $top -x 530 -y 320 -width 55 -relwidth 0 -height 24 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tCo74 \
        -in $top -x 114 -y 18 -width 143 -height 21 -anchor nw \
        -bordermode ignore 
    place $top.scr43 \
        -in $top -x 54 -y 111 -width 384 -relwidth 0 -height 106 -relheight 0 \
        -anchor nw -bordermode ignore 

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
