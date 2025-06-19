label ConfirmQuit:
    pass
    
screen navigation():
    vbox:
        yalign 0.65
        xalign 0.96
        spacing 20
        imagebutton auto "gui/new game %s.png" action Start()
        imagebutton auto "gui/load game %s.png" action ShowMenu("load")
        imagebutton auto "gui/options %s.png" action ShowMenu("preferences")
        imagebutton auto "gui/quit game %s.png" action Quit()  # ConfirmQuit()
    
    hbox:
        yalign 0.83
        xalign 0.07
        imagebutton auto "gui/gallery button %s.png" action Start()
    
    hbox:
        yalign 0.95
        xalign 0.23
        imagebutton auto "gui/ending button %s.png" action Start()
    
    hbox:
        yalign 0.98
        xalign 0.02
        imagebutton auto "gui/x select %s.png" action Start()

transform menu_art_pos:
    yalign 0.0
    xalign 0.2

transform logo_pos:
    yalign 0.1
    xalign 0.1

label main_menu:
    image menu_bg = "gui/main_menu.png"
    image menu_art = "gui/menu_art.png"

    scene black
    pause(0.5)
    show menu_bg with dissolve
    pause(0.5)
    show menu_art at menu_art_pos with dissolve
    show logo at logo_pos with Dissolve(1.0)
    show 'above layer'

    call main_menu_screen