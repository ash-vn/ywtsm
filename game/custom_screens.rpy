image gallery_bg = 'gui/gallery bg.png'
image HUD_Homescreen = "gui/HUD_Homescreen.png"

define cg_list = [
    {"name": 'MOMENT NAME MOMENT NAME', "date": None, 'file': 'test'},
    {"name": 'dos', "date": None, 'file': 'test'},
    {"name": 'tres', "date": None, 'file': 'test'},
    {"name": 'cuatro', "date": None, 'file': 'test'},
    {"name": 'cinco', "date": None, 'file': 'test'},
    {"name": 'seis', "date": None, 'file': 'test'},
    {"name": 'yks', "date": None, 'file': 'test'},
    {"name": 'kaks', "date": None, 'file': 'test'},
    {"name": 'kol', "date": None, 'file': 'test'},
    {"name": 'nel', "date": None, 'file': 'test'},
    {"name": 'None', "date": None, 'file': 'test'},
    {"name": 'None', "date": None, 'file': 'test'},
    {"name": 'None', "date": None, 'file': 'test'},
    {"name": 'None', "date": None, 'file': 'test'},
    {"name": 'None', "date": None, 'file': 'test'},
    {"name": 'None', "date": None, 'file': 'test'},
    {"name": 'None', "date": None, 'file': 'test'},
    {"name": 'None', "date": None, 'file': 'test'},
    {"name": 'None', "date": None, 'file': 'test'},
    {"name": 'None', "date": None, 'file': 'test'},
]

label gallery:
    show screen gallery_button
    scene gallery_bg with dissolve
    define resized = []
    python:
        renpy.transition(dissolve)
        renpy.call_screen('gallery_screen')
        renpy.transition(dissolve)
        renpy.call_screen('stripes_overlay')
    return

screen gallery_button:
    if renpy.get_screen('gallery_screen'):
        imagebutton auto "gui/gallery button %s.png" action Call("main_menu", load=False) at hover_enlarge_tilt yalign 0.83 xalign 0.07

screen gallery_screen:

    side "c r":
        area (500, 40, 1420, 1040)

        viewport id "custom_vp":
            draggable True
            mousewheel True
            vbox:
                spacing -100
                for i in range(20):
                    $ temp = [hover_enlarge,]
                    if i % 2 != 0:
                        $ temp.append(tilt)
                    $ name = cg_list[i]['name'].upper()
                    $ date = cg_list[i]['date'] or 'NOT UNLOCKED'
                    $ filename = f"images/{cg_list[i]['file']}.png"
                    imagebutton:
                        at temp + [hover_enlarge]
                        idle Fixed(
                            "gui/gallery_frame.png",
                            At(filename, gallery_cg_transform),
                            Text([name, ' ' * (46 - len(name) - len(date)), date, '{size=54}\n' + f"{i + 1:02d}"],
                                font=gui.text_font, xalign=0.2, yalign=0.85, size=32),
                            xsize=961, ysize=715,
                        )
                        action NullAction()
            

        vbar value YScrollValue("custom_vp")

transform tilt:
    rotate -5

transform gallery_cg_transform:
    fit "cover"
    xsize 842
    ysize 446
    yalign 0.13
    xalign 0.3

###################################

define ending_list = ["If only I can be honest with you", "To belong together forever", "What nobody can ever do", "Even so I still love you",
                    "Welcome home honey", "It's been so long", "I mourn you", "Goodbye", "Us no more", "Stuck in place", "And like everybody",
                    "Ghosting is a common", "Love letter in the drawer", "Rain eventually stops as well", "Can you wait until my time is up?"]

label endings:
    image ending = "gui/ending.png"
    image ending_bg = "gui/ending bg.png"
    scene menu_bg
    show ending_bg
    show ending at ending_pos
    with Dissolve(0.5)
    python:
        renpy.transition(dissolve)
        renpy.call_screen('ending_screen')
    return

transform ending_pos:
    yalign 0.05
    xalign 0.5

transform ending_go_back_pos:
    yalign 0.5
    linear 1.0 xalign 0.01
    linear 1.0 xalign 0.015
    repeat

screen ending_screen:
    imagebutton auto "gui/button/go back button %s.png" action Call("main_menu", load=False) at ending_go_back_pos, hover_enlarge_tilt

    vbox:
        yalign 0.7
        xalign 0.5
        spacing 15
        for i in range(len(ending_list)):
            if persistent.endings_seen[i]:
                text "{color=#DCE1E5}{size=24}{b}[ending_list[i]]{/b}" xalign 0.5
            else:
                text "{color=#425FFE}{size=24}[ending_list[i]]" xalign 0.5

###################################

screen flat_navigation():
    add "gui/HUD_Homescreen.png"

    imagebutton idle "gui/button/navigation button idle.png" xalign 0.95 yalign 0.5 at hover_enlarge action Call("outside")
    imagebutton idle "gui/button/nav arrow idle.png" at hover_enlarge, nav_arrow_pos
    # add "gui/button/apartment button idle.png" xalign 0.03 yalign 0.15 at appear_from_alpha

    imagebutton idle "gui/button/balcony button idle.png" at balcony_pos action Call('balcony')
    imagebutton idle "gui/button/bed button idle.png" at bed_pos action Call('bed')
    imagebutton idle "gui/button/desk button idle.png" at desk_pos action Call('desk')
    imagebutton idle "gui/button/kitchen button idle.png" at kitchen_pos action Call('kitchen')
    imagebutton idle "gui/button/lounge button idle.png" at lounge_pos action Call('lounge')

transform nav_arrow_pos:
    yalign 0.35
    xalign 0.9425
    linear 1.0 yalign 0.34
    linear 1.0 yalign 0.35
    repeat

transform appear_from_alpha:
    alpha 0.0
    linear 1.0 alpha 1.0

transform balcony_pos:
    xalign 0.2
    linear 1.0 yalign 0.84
    linear 1.0 yalign 0.85
    repeat

transform bed_pos:
    xalign 0.3
    linear 1.0 yalign 0.5
    linear 1.0 yalign 0.51
    repeat

transform desk_pos:
    xalign 0.36
    linear 1.0 yalign 0.68
    linear 1.0 yalign 0.69
    repeat

transform kitchen_pos:
    xpos 1010
    linear 1.0 yalign 0.17
    linear 1.0 yalign 0.18
    repeat

transform lounge_pos:
    xalign 0.65
    linear 1.0 yalign 0.7
    linear 1.0 yalign 0.71
    repeat

###################################

label preferences:
    image options_bg = "gui/options bg.png"
    image options_paper = "gui/options paper.png"
    define pref_tab = "audio"

    scene options_bg with dissolve
    hide screen blue_overlay onlayer sprites with dissolve
    python:
        renpy.transition(easeinbottom)
        renpy.show('options_paper')
        renpy.call_screen('preferences_screen', onlayer='ontop')
    scene -options_bg with dissolve
    return

transform prefs_go_back_pos:
    yalign 0.1
    linear 1.0 xalign 0.01
    linear 1.0 xalign 0.015
    repeat

style pref_buttons:
    font gui.text_font
    size 24
    # padding (150, 10)
    xsize 220
    ysize 48
    background "#0C2B43"
    hover_background "#425FFF"
    selected_background "#425FFF"
    activate_sound "assets/audio/click_hard.mp3"

label change_resolution(width=1920, height=1080):
    $ config.screen_width = width
    $ config.screen_height = height
    return

screen preferences_screen:
    tag menu
    if renpy.call_stack_depth():
        imagebutton auto "gui/button/go back button %s.png" action Call("main_menu", load=False) at prefs_go_back_pos, hover_enlarge_tilt
    else:
        imagebutton auto "gui/button/go back button %s.png" action [Hide("preferences_screen", transition=easeoutbottom), Return()] at prefs_go_back_pos, hover_enlarge_tilt

    vbox:
        yalign 0.37
        xalign 0.15
        spacing 20
        textbutton "AUDIO" text_align (0.5, 0.5) text_color "#DCE1E5" style "pref_buttons" action SelectedIf(SetVariable("pref_tab", "audio"))
        textbutton "GRAPHICS" text_align (0.5, 0.5) text_color "#DCE1E5" style "pref_buttons" action SetVariable("pref_tab", "graphics")
        textbutton "LANGUAGE" text_align (0.5, 0.5) text_color "#DCE1E5" style "pref_buttons" action SetVariable("pref_tab", "language")
        textbutton "CREDITS" text_align (0.5, 0.5) text_color "#DCE1E5" style "pref_buttons" action SetVariable("pref_tab", "credits")
    
    vbox:
        ypos 300
        xpos 600
        xsize 1200
        text pref_tab.upper() size 40 font gui.name_text_font
        text " "

        if pref_tab == "audio":
            hbox:
                spacing 20
                vbox:
                    spacing 14
                    text "Music Volume" font gui.text_font size 32
                    text "Sound Volume" font gui.text_font size 32
                    text "Voice Volume" font gui.text_font size 32
                    text " "
                    textbutton _("Mute All"):
                        action Preference("all mute", "toggle")
                        style "pref_buttons"
                        text_align (0.5, 0.5)
                        text_color "#DCE1E5"

                vbox:
                    spacing 14
                    bar value Preference("music volume")
                    bar value Preference("sound volume")
                    bar value Preference("voice volume")

        elif pref_tab == "graphics":
            hbox:
                spacing 20
                vbox:
                    spacing 14
                    text _("Display")  font gui.text_font size 32
                    text _("Resolution")  font gui.text_font size 32

                vbox:
                    spacing 14
                    xpos 50
                    hbox:
                        xsize 500
                        textbutton _("Window"):
                            action [Preference("display", "window"), SelectedIf(not preferences.fullscreen)]
                            style "pref_buttons"
                            text_align (0.5, 0.5)
                            text_color "#DCE1E5"
                        textbutton _("Fullscreen"):
                            action Preference("display", "fullscreen")
                            style "pref_buttons"
                            text_align (0.5, 0.5)
                            text_color "#DCE1E5"
                    hbox:
                        xsize 1000
                        for res in [(1280, 720), (1366, 768), (1600, 900), (1920, 1080)]:
                            textbutton "[res[0]]x[res[1]]":
                                action SelectedIf(Preference("display", res[0]/1920))
                                style "pref_buttons"
                                text_align (0.5, 0.5)
                                text_color "#DCE1E5"

        elif pref_tab == "language":
            hbox:
                vbox:
                    spacing 14
                    text "Text" font gui.text_font size 32
                    text "Voice Over" font gui.text_font size 32

                vbox:
                    xsize 900
                    xpos 50
                    spacing 14
                    hbox:
                        textbutton _("English"):
                            action Language(None)
                            style "pref_buttons"
                            text_align (0.5, 0.5)
                            text_color "#DCE1E5"
                        textbutton _("Korean"):
                            action Language('korean')
                            style "pref_buttons"
                            text_align (0.5, 0.5)
                            text_color "#DCE1E5"
                    hbox:
                        textbutton _("English"):
                            action SetVariable('vo_lang', "en")
                            style "pref_buttons"
                            text_align (0.5, 0.5)
                            text_color "#DCE1E5"
                        textbutton _("Korean"):
                            action SetVariable('vo_lang', "kr")
                            style "pref_buttons"
                            text_align (0.5, 0.5)
                            text_color "#DCE1E5"

        elif pref_tab == "credits":
            side "c r":
                viewport id "credit_vp":
                    area (-10, -10, 1200, 600)
                    mousewheel True
                    draggable True
                    grid 4 3:
                        spacing 30
                        top_margin 10
                        left_margin 10
                        for guy in creditors:
                            $ filename = f"gui/credits/{guy['picture']}.png"
                            vbox:
                                xsize 235
                                ysize 351
                                fixed:
                                    xsize 235
                                    ysize 235
                                    imagebutton idle filename at credit_pic action OpenURL(guy['link'])
                                text guy['name'] align (0.5, 0.5) size 32 font gui.name_text_font
                                for role in guy['role'].split('\n'):
                                    text role align (0.5, 0.5) size 20

                vbar value YScrollValue("credit_vp")


transform credit_pic:
    # fit "cover"
    xsize 235
    ysize 235
    on hover:
        linear 0.1:
            truecenter
            zoom 1.05
    on idle:
        linear 0.1:
            truecenter
            zoom 1.00

define creditors = [
    {'name': 'NKD', 'picture': 'test', 'role': 'Project Manager\nCG & sprite artist', 'link': None},
    {'name': 'Whilo', 'picture': 'test', 'role': 'Chibi Artist', 'link': None},
    {'name': 'Enim', 'picture': 'test', 'role': 'CG Artist', 'link': None},
    {'name': 'Nuria', 'picture': 'test', 'role': '3D Artist', 'link': None},
    {'name': 'Leny', 'picture': 'test', 'role': 'UI design', 'link': None},
    {'name': 'Tia_Faisa', 'picture': 'test', 'role': 'Live2D rigging', 'link': None},
    {'name': 'Eidolethe', 'picture': 'test', 'role': 'Writing', 'link': None},
    {'name': 'The Sloth', 'picture': 'test', 'role': 'Writing', 'link': None},
    {'name': 'Andry', 'picture': 'test', 'role': 'Composer', 'link': None},
    {'name': 'Haikeus', 'picture': 'test', 'role': 'Programmer', 'link': None},
    {'name': 'EPI', 'picture': 'EPI', 'role': 'Korean translator', 'link': 'https://epi-zh.itch.io/'},
]
