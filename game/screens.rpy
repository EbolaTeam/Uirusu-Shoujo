# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say:

    fixed:
    #style "say_two_window_vbox"
        
        if what:
            window:
                id "window"
                    
                has vbox:
                    style "say_vbox"
                text what id "what"
                    
            window:
                style "say_who_window"

                text who:
                    id "who"


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice:

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input:

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl:

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu:

    window:
        style "mm_root"

    # This ensures that any other menu screen is replaced.
    tag menu

    imagemap:
        ground "images/menus/main/mm_idle.png"
        hover "images/menus/main/mm_hover.png"

        hotspot (1704,769,199,70) action Start()
        hotspot (1717,839,186,73) action ShowMenu("load")
        hotspot (1658,912,245,80) action ShowMenu("preferences")
        hotspot (1756,992,147,60) action Quit(confirm=False)

##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation:

    # The background of the game menu.
#    window:
#        style "gm_root"

    # The various buttons.
    imagemap:
        ground "images/menus/nav/nav_ground.png"
        idle "images/menus/nav/nav_idle.png"
        hover "images/menus/nav/nav_hover.png"
        selected_idle "images/menus/nav/nav_selected_idle.png"
        selected_hover "images/menus/nav/nav_selected_hover.png"

        hotspot (1665,552,235,69) action Return()
        hotspot (1503,621,397,75) action ShowMenu("preferences")
        hotspot (1503,696,397,68) action ShowMenu("save")
        hotspot (1503,764,397,77) action ShowMenu("load")
        hotspot (1539,841,361,71) action MainMenu()
        hotspot (1743,912,157,78) action Help()
        hotspot (1743,990,157,60) action Quit()


##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen file_picker:

    frame:
        style "file_picker_frame"

        has vbox

        # The buttons at the top allow the user to pick a
        # page of files.
        hbox:
            style_group "file_picker_nav"

            textbutton _("Previous"):
                action FilePagePrevious()

            textbutton _("Auto"):
                action FilePage("auto")

            textbutton _("Quick"):
                action FilePage("quick")

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)

            textbutton _("Next"):
                action FilePageNext()

        $ columns = 2
        $ rows = 5

        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"

            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                button:
                    action FileAction(i)
                    xfill True

                    has hbox

                    # Add the screenshot.
                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Empty Slot."))
                    $ save_name = FileSaveName(i)

                    text "[file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)


screen save:

    tag menu

    window:
        style "gm_root"

    use navigation

    imagemap:
        ground "images/menus/loadsave/loadsave_save_ground.png"
        idle "images/menus/loadsave/loadsave_idle.png"
        hover "images/menus/loadsave/loadsave_hover.png"
        selected_idle "images/menus/loadsave/loadsave_selected.png"

        alpha False
        cache False

        hotspot (257, 960, 61,95) clicked FilePage(1)
        hotspot (347, 960, 81,95) clicked FilePage(2)
        hotspot (454, 960, 88,95) clicked FilePage(3)
        hotspot (572, 960, 79,95) clicked FilePage(4)
        hotspot (677, 960, 85,95) clicked FilePage(5)
        hotspot (785, 960, 85,95) clicked FilePage(6)
        hotspot (896, 960, 80,95) clicked FilePage(7)
        hotspot (1006, 960, 76,95) clicked FilePage(8)
        hotspot (1117, 960, 77,95) clicked FilePage(9)
        hotspot (1224, 960, 108,95) clicked FilePage(10)

        hotspot (153, 186, 319, 242) clicked FileSave(1):
            use load_save_slot(number=1)
        hotspot (472, 186, 319, 242) clicked FileSave(2):
            use load_save_slot(number=2)
        hotspot (791, 186, 319, 242) clicked FileSave(3):
            use load_save_slot(number=3)
        hotspot (1110, 186, 319, 242) clicked FileSave(4):
            use load_save_slot(number=4)
        hotspot (153, 428, 319, 242) clicked FileSave(5):
            use load_save_slot(number=5)
        hotspot (472, 428, 319, 242) clicked FileSave(6):
            use load_save_slot(number=6)
        hotspot (791, 428, 319, 242) clicked FileSave(7):
            use load_save_slot(number=7)
        hotspot (1110, 428, 319, 242) clicked FileSave(8):
            use load_save_slot(number=8)
        hotspot (153, 670, 319, 242) clicked FileSave(9):
            use load_save_slot(number=9)
        hotspot (472, 670, 319, 242) clicked FileSave(10):
            use load_save_slot(number=10)
        hotspot (791, 670, 319, 242) clicked FileSave(11):
            use load_save_slot(number=11)
        hotspot (1110, 670, 319, 242) clicked FileSave(12):
            use load_save_slot(number=12)


    
screen load:

    tag menu

    window:
        style "gm_root"

    use navigation

    imagemap:
        ground "images/menus/loadsave/loadsave_load_ground.png"
        idle "images/menus/loadsave/loadsave_idle.png"
        hover "images/menus/loadsave/loadsave_hover.png"
        selected_idle "images/menus/loadsave/loadsave_selected.png"

        alpha False

        cache False

        hotspot (257, 960, 61,95) clicked FilePage(1)
        hotspot (347, 960, 81,95) clicked FilePage(2)
        hotspot (454, 960, 88,95) clicked FilePage(3)
        hotspot (572, 960, 79,95) clicked FilePage(4)
        hotspot (677, 960, 85,95) clicked FilePage(5)
        hotspot (785, 960, 85,95) clicked FilePage(6)
        hotspot (896, 960, 80,95) clicked FilePage(7)
        hotspot (1006, 960, 76,95) clicked FilePage(8)
        hotspot (1117, 960, 77,95) clicked FilePage(9)
        hotspot (1224, 960, 108,95) clicked FilePage(10)

        hotspot (153, 186, 319, 242) clicked FileLoad(1):
            use load_save_slot(number=1)
        hotspot (472, 186, 319, 242) clicked FileLoad(2):
            use load_save_slot(number=2)
        hotspot (791, 186, 319, 242) clicked FileLoad(3):
            use load_save_slot(number=3)
        hotspot (1110, 186, 319, 242) clicked FileLoad(4):
            use load_save_slot(number=4)
        hotspot (153, 428, 319, 242) clicked FileLoad(5):
            use load_save_slot(number=5)
        hotspot (472, 428, 319, 242) clicked FileLoad(6):
            use load_save_slot(number=6)
        hotspot (791, 428, 319, 242) clicked FileLoad(7):
            use load_save_slot(number=7)
        hotspot (1110, 428, 319, 242) clicked FileLoad(8):
            use load_save_slot(number=8)
        hotspot (153, 670, 319, 242) clicked FileLoad(9):
            use load_save_slot(number=9)
        hotspot (472, 670, 319, 242) clicked FileLoad(10):
            use load_save_slot(number=10)
        hotspot (791, 670, 319, 242) clicked FileLoad(11):
            use load_save_slot(number=11)
        hotspot (1110, 670, 319, 242) clicked FileLoad(12):
            use load_save_slot(number=12)
    

    
screen load_save_slot:

    $ slot_text = FileSlotName(number, 12)
    $ time_text = FileTime(number, empty=("Infection Free"))

    add FileScreenshot(number) xpos 78 ypos 64

    text slot_text xcenter 160 ycenter 115 size 60 color "#ff000088" outlines [ (2,"#000000ff") ] font "Evil Bunny.ttf"
    text time_text xcenter 160 ycenter 165 size 24 color "#ffffffff" outlines [ (2,"#000000ff") ] font "BAARS__.TTF"

    key "save_delete" action FileDelete(number)
    
init -2 python:
    
    config.thumbnail_width = 160
    config.thumbnail_height = 110


##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences:

    tag menu

    window:
        style "gm_root"

    use navigation

    imagemap:
        ground "images/menus/pref/pref_ground.png"
        idle "images/menus/pref/pref_idle.png"
        hover "images/menus/pref/pref_hover.png"
        selected_idle "images/menus/pref/pref_selected_idle.png"
        selected_hover "images/menus/pref/pref_selected_hover.png"

        hotspot (158, 200, 310, 60) action Preference("display", "fullscreen") 
        hotspot (189, 260, 279, 56) action Preference("display", "window") 
        hotspot (224, 421, 244, 63) action Preference("transitions", "all")
        hotspot (310, 484, 158, 54) action Preference("transitions", "none")
        hotspot (189, 663, 279, 56) action Preference("skip", "seen")
        hotspot (242, 720, 226, 63) action Preference("skip", "all")
        hotspot (121, 892, 347, 64) action Preference("after choices", "stop")
        hotspot (124, 956, 344, 60) action Preference("after choices", "skip")

        bar pos (736, 156) value Preference("music volume") style "pref_slider"
        bar pos (736, 360) value Preference("sound volume") style "pref_slider"
        bar pos (736, 553) value Preference("voice volume") style "pref_slider"
        bar pos (736, 764) value Preference("text speed") style "pref_slider"
        bar pos (736, 975) value Preference("auto-forward time") style "pref_slider"

init -2 python:
    style.pref_slider.right_bar = "images/menus/pref/pref_bar_empty.png"
    style.pref_slider.left_bar = "images/menus/pref/pref_bar_full.png"

    style.pref_slider.xmaximum = 615
    style.pref_slider.ymaximum = 101
    style.pref_slider.thumb = "images/menus/pref/pref_bar_thumb_null.png"
    style.pref_slider.thumb_offset = 16
    style.pref_slider.thumb_shadow = None

##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt:

    modal True

    window:
        style "gm_root"

    imagemap:
        ground 'images/menus/yesno/yesno_ground.png'
        idle 'images/menus/yesno/yesno_idle.png' 
        hover 'images/menus/yesno/yesno_hover.png'
        
        hotspot (699, 512, 199, 101) action yes_action
        hotspot (1089, 512, 163, 101) action no_action
    add "images/menus/yesno/yesno_overlay.png"
    
    if message == layout.ARE_YOU_SURE:
        add "images/menus/yesno/yesno_are_you_sure.png"
 
    elif message == layout.DELETE_SAVE:
        add "images/menus/yesno/yesno_delete_save.png"
        
    elif message == layout.OVERWRITE_SAVE:
        add "images/menus/yesno/yesno_overwrite_save.png"
        
    elif message == layout.LOADING:
        add "images/menus/yesno/yesno_load_save.png"
        
    elif message == layout.QUIT:
        add "images/menus/yesno/yesno_are_you_sure.png"
        
    elif message == layout.MAIN_MENU:
        add "images/menus/yesno/yesno_main_menu.png"


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu:

    # Add an in-game quick menu.
    hbox:
        style_group "quick"

        xalign 1.0
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("Save") action ShowMenu('save')
        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Skip") action Skip()
        textbutton _("F.Skip") action Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Prefs") action ShowMenu('preferences')

init -2:
    style quick_button:
        is default
        background None
        xpadding 5

    style quick_button_text:
        is default
        size 12
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"

