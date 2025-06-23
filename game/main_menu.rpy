image menu_bg = "gui/main_menu.png"
image main_menu = "gui/main menu.png"
image logo = "gui/logo.png"
image logo_dist = "gui/logo dist.png"
image main_menu_dist = "gui/main menu_distort.png"

transform logo_pos:
    on hover:
        zoom 1.0
        linear 1.0 zoom 2.0
    on idle:
        linear 1.0 zoom 1.0
    # linear 1.0 zoom 1.0

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
            imagebutton auto "gui/gallery button %s.png" action Call("gallery")
        
        hbox:
            yalign 0.95
            xalign 0.23
            imagebutton auto "gui/ending button %s.png" action Call("endings")
        
        # hbox:
        #     yalign 0.98
        #     xalign 0.02
        #     imagebutton auto "gui/x select %s.png" action Start()


label confirm_quit:
    show main_menu_dist
    show logo_dist at logo_pos
    with Dissolve(.5)
    pause(1.0)
    python:
        renpy.transition(dissolve)
        renpy.call_screen('confirm', "Are you really sure you want to quit?", Quit(), Jump("main_menu"))

label main_menu(load=True):
    # jump start  ###### DEBUGGGGG
    define config.developer = False
    while True:
        call screen flat_navigation

    hide blue_overlay
    scene black
    if load:
        pause(0.5)
    show menu_bg
    if load:
        with dissolve
        pause(0.5)
    show main_menu
    if load:
        with dissolve
    show logo at logo_pos
    if load:
        with Dissolve(1.0)

    python:
        renpy.transition(dissolve)
        renpy.call_screen('main_menu')
