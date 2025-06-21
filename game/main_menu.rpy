image menu_bg = "gui/main_menu.png"
image menu_art = "gui/menu_art.png"
image logo = "gui/logo.png"
image above_layer = "gui/menu/above layer.png"
image menu_art_dist = "gui/menu_art dist.png"
image logo_dist = "gui/logo dist.png"
image above_layer_dist = "gui/menu/above layer dist.png"

transform menu_art_pos:
    yalign 0.0
    xalign 0.2

transform logo_pos:
    yalign 0.1
    xalign 0.1

transform above_layer_pos:
    alpha .5
    # xpos -900
    # ypos -52

transform show_hide_dissolve:
    on show:
        alpha .0
        linear .5 alpha 1.0
    on hide:
        alpha 1.0
        linear .5 alpha .0

screen navigation():
    if renpy.get_screen("main_menu"):
        vbox:
            yalign 0.65
            xalign 0.96
            spacing 20
            imagebutton auto "gui/new game %s.png" action Start()
            imagebutton auto "gui/load game %s.png" action ShowMenu("load")
            imagebutton auto "gui/options %s.png" action ShowMenu("preferences")
            imagebutton auto "gui/quit game %s.png" action Jump("confirm_quit")  # ConfirmQuit()
        
        hbox:
            yalign 0.83
            xalign 0.07
            imagebutton auto "gui/gallery button %s.png" action Start()
        
        hbox:
            yalign 0.95
            xalign 0.23
            imagebutton auto "gui/ending button %s.png" action Start()
        
        # hbox:
        #     yalign 0.98
        #     xalign 0.02
        #     imagebutton auto "gui/x select %s.png" action Start()

        
label main_menu:
    # jump start  ###### DEBUGGGGG

    hide blue_overlay
    scene black
    pause(0.5)
    show menu_bg with dissolve
    pause(0.5)
    show menu_art at menu_art_pos with dissolve
    show logo at logo_pos with Dissolve(1.0)
    show above_layer

    python:
        renpy.transition(dissolve)
        renpy.call_screen('main_menu')

label confirm_quit:
    hide menu_art
    hide logo
    hide above_layer
    show menu_art_dist at menu_art_pos
    show logo_dist at logo_pos
    show above_layer_dist at above_layer_pos
    call screen confirm("Are you really sure you want to quit?", Quit(), Jump("main_menu"))
