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
            yalign 0.3
            xalign 0.96
            imagebutton auto "gui/new game %s.png" action Start() at hover_enlarge_tilt
        vbox:
            yalign 0.48
            xalign 0.96
            imagebutton auto "gui/load game %s.png" action ShowMenu("load") at hover_enlarge_tilt
        vbox:
            yalign 0.66
            xalign 0.96
            imagebutton auto "gui/options %s.png" action Call("preferences") at hover_enlarge_tilt
        vbox:
            yalign 0.84
            xalign 0.96
            imagebutton auto "gui/quit game %s.png" hovered Call('confirm_quit') unhovered Return() action NullAction() at hover_enlarge_tilt
        
        hbox:
            yalign 0.83
            xalign 0.07
            imagebutton auto "gui/gallery button %s.png" action Call("gallery") at hover_enlarge_tilt
        
        hbox:
            yalign 0.95
            xalign 0.23
            imagebutton auto "gui/ending button %s.png" action Call("endings") at hover_enlarge_tilt


screen quit_button:
    vbox:
        yalign 0.84
        xalign 0.96
        imagebutton auto "gui/quit game %s.png" unhovered Call('main_menu', load=False) action Jump('lmaooo') at hover_enlarge_tilt

label confirm_quit:
    # play music1 "assets/audio/music/bgm_dist.mp3" volume 1.0 fadeout 0.2
    $ renpy.music.set_volume(1.0, 0.0, channel='music1')
    $ renpy.music.set_volume(0.0, 0.0, channel='music')
    show main_menu_dist
    show logo_dist at logo_pos
    python:
        renpy.transition(Dissolve(.2))
        renpy.call_screen('quit_button')
    return

label lmaooo:
    show screen stripes_overlay onlayer ontop
    python:
        renpy.transition(Dissolve(.2))
        renpy.call_screen('custom_quit')
    return

style custom_quit_text:
    font gui.text_font
    size 24
    # padding (20, 10)
    xsize 175
    ysize 48
    hover_color "#425FFF"
    activate_sound "assets/audio/click_hard.mp3"

screen custom_quit:
    add "gui/quit.png"
    textbutton _("no"):
        action Call("main_menu", load=False)
        at no_pos
        background "gui/button/no.png"
        style 'custom_quit_text'
        text_color "#DCE1E5"
        text_align (0.5, 0.5)
    textbutton _("bye"):
        action Quit()
        at bye_pos
        background "gui/button/bye.png"
        style 'custom_quit_text'
        text_color "#DCE1E5"
        text_align (0.55, 0.8)

transform no_pos:
    xalign 0.62
    yalign 0.0
    ease 0.5 yalign 0.6
    on idle:
        linear .2 zoom 1.0
    on hover:
        linear .2 zoom 1.1

transform bye_pos:
    xalign 0.618
    yalign -1.0
    ease 1.0 yalign 0.7
    on idle:
        linear .2 zoom 1.0
    on hover:
        linear .2 zoom 1.1

label main_menu(load=True):
    # jump start  ###### DEBUGGGGG
    define config.developer = False
    # while True:
    #     call gallery
    if renpy.music.get_playing() != "assets/audio/music/bgm.mp3" or renpy.music.get_playing(channel="music1") != "assets/audio/music/bgm_dist.mp3":
        $ renpy.music.play("assets/audio/music/bgm.mp3", channel="music", synchro_start=True)
        $ renpy.music.play("assets/audio/music/bgm_dist.mp3", channel="music1", synchro_start=True)
    $ renpy.music.set_volume(1.0, 0.0, channel='music')
    $ renpy.music.set_volume(0.0, 0.0, channel='music1')
    hide blue_overlay
    hide screen stripes_overlay
    hide screen stripes_overlay onlayer ontop
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

    $ load = False
    python:
        renpy.transition(dissolve)
        renpy.call_screen('main_menu')
