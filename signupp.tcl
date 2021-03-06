#############################################################################
# Generated by PAGE version 4.20
#  in conjunction with Tcl version 8.6
#  May 04, 2019 01:36:22 PM IST  platform: Windows NT
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
        -menu "$top.m74" -background {#d9d9d9} -highlightbackground {#d9d9d9} \
        -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 764x536+238+132
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
    entry $top.ent43 \
        -background green -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$top.ent43" "Entry1" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent44 \
        -background green -disabledforeground {#528ba3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$top.ent44" "Entry2" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent45 \
        -background green -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$top.ent45" "Entry3" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent46 \
        -background green -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$top.ent46" "Entry4" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab47 \
        -activebackground {#f9f9f9} -activeforeground black -background green \
        -disabledforeground {#a3a3a3} -font $::vTcl(fonts,vTcl:font9,object) \
        -foreground {#f7f7f7} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text Gender 
    vTcl:DefineAlias "$top.lab47" "Label1" vTcl:WidgetProc "Toplevel1" 1
    radiobutton $top.rad48 \
        -activebackground {#ececec} -activeforeground white -background green \
        -command Male -disabledforeground white \
        -font $::vTcl(fonts,vTcl:font9,object) -foreground {#f7f7f7} \
        -highlightbackground {#ffffff} -highlightcolor white -justify left \
        -text Male -value Male -variable Malee 
    vTcl:DefineAlias "$top.rad48" "Radiobutton1" vTcl:WidgetProc "Toplevel1" 1
    radiobutton $top.rad49 \
        -activebackground {#ececec} -activeforeground white -background green \
        -command female -disabledforeground white \
        -font $::vTcl(fonts,vTcl:font9,object) -foreground {#f7f7f7} \
        -highlightbackground {#ffffff} -highlightcolor white -justify left \
        -text Female -variable Femalee 
    vTcl:DefineAlias "$top.rad49" "Radiobutton2" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab50 \
        -activebackground {#f9f9f9} -activeforeground black -background green \
        -disabledforeground {#a3a3a3} -font $::vTcl(fonts,vTcl:font9,object) \
        -foreground {#f7f7f7} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text Image 
    vTcl:DefineAlias "$top.lab50" "Label2" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent51 \
        -background green -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$top.ent51" "Entry5" vTcl:WidgetProc "Toplevel1" 1
    button $top.but52 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background red -command selectt -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font9,object) -foreground {#f7f7f7} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text Select 
    vTcl:DefineAlias "$top.but52" "Button1" vTcl:WidgetProc "Toplevel1" 1
    labelframe $top.lab61 \
        -font $::vTcl(fonts,vTcl:font9,object) -foreground {#f7f7f7} \
        -text Question -background green -height 235 \
        -highlightbackground {#d9d9d9} -highlightcolor black -width 720 
    vTcl:DefineAlias "$top.lab61" "Labelframe1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.lab61
    label $site_3_0.lab64 \
        -activebackground {#f9f9f9} -activeforeground black -background green \
        -disabledforeground {#a3a3a3} -font $::vTcl(fonts,vTcl:font9,object) \
        -foreground {#f7f7f7} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text Q.1 
    vTcl:DefineAlias "$site_3_0.lab64" "Label3" vTcl:WidgetProc "Toplevel1" 1
    ttk::combobox $site_3_0.tCo66 \
        \
        -values {{"What was your childhood nickname?" } {"In what city did you meet your spouse/significant other?"} {"What is the name of your favorite childhood friend?"} {"What street did you live on in third grade?"} {"What is your oldest sibling?s birthday month and year? (e.g., January 1900)" } {}} \
        -font TkTextFont -textvariable question1 -foreground {} \
        -background {#3bbeff} -takefocus {} 
    vTcl:DefineAlias "$site_3_0.tCo66" "TCombobox1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab68 \
        -activebackground {#f9f9f9} -activeforeground black -background green \
        -disabledforeground {#a3a3a3} -font $::vTcl(fonts,vTcl:font9,object) \
        -foreground {#f7f7f7} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text Ans 
    vTcl:DefineAlias "$site_3_0.lab68" "Label4" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent69 \
        -background green -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent69" "Entry6" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab70 \
        -activebackground {#f9f9f9} -activeforeground black -background green \
        -disabledforeground {#a3a3a3} -font $::vTcl(fonts,vTcl:font9,object) \
        -foreground {#f7f7f7} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text Q.2 
    vTcl:DefineAlias "$site_3_0.lab70" "Label5" vTcl:WidgetProc "Toplevel1" 1
    ttk::combobox $site_3_0.tCo71 \
        \
        -values {{"What is the middle name of your youngest child?"} {"What is your oldest sibling's middle name?"} {"What school did you attend for sixth grade?"} {"What was your childhood phone number including area code?"} {"What is your oldest cousin's first and last name?"} {}} \
        -font TkTextFont -textvariable question2 -foreground {} \
        -background {} -takefocus {} 
    vTcl:DefineAlias "$site_3_0.tCo71" "TCombobox2" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab72 \
        -activebackground {#f9f9f9} -activeforeground black -background green \
        -disabledforeground {#a3a3a3} -font $::vTcl(fonts,vTcl:font9,object) \
        -foreground {#f7f7f7} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text Ans 
    vTcl:DefineAlias "$site_3_0.lab72" "Label6" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent73 \
        -background green -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent73" "Entry7" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.lab64 \
        -in $site_3_0 -x 10 -y 40 -anchor nw -bordermode ignore 
    place $site_3_0.tCo66 \
        -in $site_3_0 -x 80 -y 33 -width 533 -relwidth 0 -height 31 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab68 \
        -in $site_3_0 -x 10 -y 90 -anchor nw -bordermode ignore 
    place $site_3_0.ent69 \
        -in $site_3_0 -x 80 -y 87 -width 534 -relwidth 0 -height 30 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab70 \
        -in $site_3_0 -x 7 -y 147 -width 34 -relwidth 0 -height 21 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tCo71 \
        -in $site_3_0 -x 80 -y 140 -width 533 -relwidth 0 -height 31 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab72 \
        -in $site_3_0 -x 10 -y 200 -anchor nw -bordermode ignore 
    place $site_3_0.ent73 \
        -in $site_3_0 -x 80 -y 190 -width 534 -relwidth 0 -height 30 \
        -relheight 0 -anchor nw -bordermode ignore 
    button $top.but62 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background red -command submitt -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font9,object) -foreground {#f7f7f7} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text Submit 
    vTcl:DefineAlias "$top.but62" "Button2" vTcl:WidgetProc "Toplevel1" 1
    button $top.but63 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background red -command backk -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font9,object) -foreground {#f7f7f7} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text Back 
    vTcl:DefineAlias "$top.but63" "Button3" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.m74
    menu $site_3_0 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -font TkMenuFont -foreground {#000000} \
        -tearoff 0 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.ent43 \
        -in $top -x 18 -y 31 -width 244 -relwidth 0 -height 20 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent44 \
        -in $top -x 519 -y 30 -width 224 -relwidth 0 -height 20 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent45 \
        -in $top -x 20 -y 90 -width 234 -relwidth 0 -height 20 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent46 \
        -in $top -x 519 -y 93 -width 224 -relwidth 0 -height 20 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab47 \
        -in $top -x 340 -y 30 -width 94 -relwidth 0 -height 21 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.rad48 \
        -in $top -x 286 -y 70 -width 88 -relwidth 0 -height 25 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.rad49 \
        -in $top -x 400 -y 70 -width 88 -relwidth 0 -height 25 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab50 \
        -in $top -x 30 -y 160 -width 84 -relwidth 0 -height 21 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent51 \
        -in $top -x 149 -y 152 -width 284 -relwidth 0 -height 30 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but52 \
        -in $top -x 500 -y 160 -width 127 -relwidth 0 -height 24 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab61 \
        -in $top -x 20 -y 213 -width 720 -relwidth 0 -height 235 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but62 \
        -in $top -x 40 -y 460 -width 117 -relwidth 0 -height 24 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but63 \
        -in $top -x 600 -y 465 -width 117 -relwidth 0 -height 24 -relheight 0 \
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

