
#backgrounds, images, and character definitions have been moved to definitions.rpy

# The game starts here.
label start:
    stop music
    scene bg black
    menu:
        "Demo":
            jump final
        "Skeleton":
            jump actI
    return

init:
    if persistent.first is None:
        $ persistent.first = True
    if persistent.ecchi is None:
        $ persistent.ecchi = False
label splashscreen:
    scene black
    if persistent.first:
        $renpy.transition(dissolve)
        call screen eula("Eula goes here")
        $renpy.transition(fade)
        call screen h_toggle
        $ persistent.ecchi = _return
        $ persistent.first = False
    return
screen eula(content):
    frame:
        style_group "eula"
        xmargin 30 ymargin 30
        xpadding 20 ypadding 20
        text "EULA"
        frame:
            style_group "eulacontent"
            xmargin 30 ymargin 60
            xpadding 20 ypadding 10
            xminimum 1.0 yminimum 1.0
            viewport:
                scrollbars "vertical"
                mousewheel True draggable True
                text content
        frame:
            style_group "eulabutton"
            yalign 1.0
            textbutton "I Agree" action Return()
        frame:
            style_group "eulabutton"
            xalign 1.0 yalign 1.0
            textbutton "Quit" action Quit(confirm=False) xalign 1.0

screen h_toggle:
    frame:
        xmargin 0.2 ymargin 0.3
        xpadding 20 ypadding 20
        text "This game contains optional sex scenes and nudity.\nIf you do not wish to experience this content, please disable it now.\nYou can also disable it at any time from the preferences menu."
        frame:
            style_group "eulabutton"
            xalign 0.5 yalign 1.0
            vbox:
                text "Sex scenes:"
                hbox:
                    textbutton "On" action Return(True)
                    textbutton "Off" action Return(False)

init -2 python:
    style.eulacontent_frame.background="#220000"
    style.eulabutton_frame.background=None
    style.eulabutton_button_text.size = 32

