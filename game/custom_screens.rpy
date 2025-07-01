image gallery_bg = 'gui/gallery bg.png'
image HUD_Homescreen = "gui/HUD_Homescreen.png"

default persistent.cg_list = [
    # {"name": 'First Meeting', "date": None, 'file': 'placeholder'},
    {"name": 'Activity - Making Paper Cranes', "date": None, 'file': 'daily_event_art/0'},
    {"name": 'Activity - Scrolling Fun', "date": None, 'file': 'daily_event_art/1'},
    {"name": 'Activity - Cleaning Time', "date": None, 'file': 'daily_event_art/2'},
    {"name": 'Activity - Laundry Folding', "date": None, 'file': 'daily_event_art/3'},
    {"name": 'Activity - Working Late', "date": None, 'file': 'daily_event_art/4'},
    {"name": 'Activity - TV Coziness', "date": None, 'file': 'daily_event_art/5'},
    {"name": 'Activity - Dear Diary', "date": None, 'file': 'daily_event_art/6'},
    {"name": 'Activity - Cooking Together', "date": None, 'file': 'daily_event_art/7'},
    {"name": "It's Been So Long", "date": None, 'file': 'endings/END06'},
    {"name": "I mourn you", "date": None, 'file': 'endings/END07'},
    {"name": "Us no more", "date": None, 'file': 'endings/END09'},
    {"name": "Stuck in place", "date": None, 'file': 'endings/END10'},
    {"name": "And like everybody", "date": None, 'file': 'endings/END11'},
    {"name": "Ghosting is a common", "date": None, 'file': 'endings/END12'},
    {"name": "Love letter in the drawer", "date": None, 'file': 'endings/END13'},
    {"name": "Rain eventually stops as well", "date": None, 'file': 'endings/END14'},
    # {"name": "Marshmallows x Chocolate", "date": None, 'file': 'placeholder'},
    # {"name": "Toast x Toaster", "date": None, 'file': 'placeholder'},
    # {"name": "Chocolate x Valentines", "date": None, 'file': 'placeholder'},
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
                for i in range(len(persistent.cg_list)):
                    $ temp = [hover_enlarge,]
                    if i % 2 != 0:
                        $ temp.append(tilt)
                    $ name = persistent.cg_list[i]['name'].upper()
                    $ date = persistent.cg_list[i]['date'] or 'NOT UNLOCKED'
                    $ filename = f"images/{persistent.cg_list[i]['file']}.png"
                    if persistent.cg_list[i]['date']:
                        imagebutton:
                            at temp
                            idle Fixed(
                                "gui/gallery_frame.png",
                                At(filename, gallery_cg_transform),
                                Text([name, ' ' * (46 - len(name) - len(date)), date, '{size=54}\n' + f"{i + 1:02d}"],
                                    font=gui.text_font, xalign=0.2, yalign=0.85, size=32),
                                xsize=961, ysize=715,
                            )
                            action Show(screen="gallery_view", transition=dissolve, filename=filename)
                    elif i < 17:
                        imagebutton:
                            at temp
                            idle Fixed(
                                "gui/gallery_frame.png",
                                At(filename, gallery_cg_transform, gallery_cg_locked_transform),
                                Text([name, ' ' * (46 - len(name) - len(date)), date, '{size=54}\n' + f"{i + 1:02d}"],
                                    font=gui.text_font, xalign=0.2, yalign=0.85, size=32),
                                xsize=961, ysize=715,
                            )
                            action NullAction()

        vbar value YScrollValue("custom_vp")

screen gallery_view(filename):
    add filename xalign 0.5 yalign 0.5 xsize 1920 ysize 1080
    imagebutton auto "gui/button/go back button %s.png" action Hide(screen="gallery_view") at prefs_go_back_pos, hover_enlarge_tilt

transform tilt:
    rotate -5

transform gallery_cg_transform:
    fit "fill"
    xsize 842
    ysize 446
    yalign 0.13
    xalign 0.3

transform gallery_cg_locked_transform:
    blur 50

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

image options_bg = "gui/options bg.png"
image options_paper = "gui/options paper.png"
label preferences:
    define pref_tab = "audio"

    scene options_bg onlayer screens with dissolve
    hide screen blue_overlay onlayer sprites with dissolve
    python:
        renpy.transition(easeinbottom)
        renpy.show('options_paper', layer='screens')
        renpy.call_screen('preferences_screen')
    scene -options_bg onlayer screens with dissolve
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

default cur_name = None
screen preferences_screen:
    tag menu
    if renpy.call_stack_depth():
        imagebutton auto "gui/button/go back button %s.png" action [Function(renpy.hide, 'options_paper', layer='screens'),
                                                                    Function(renpy.hide, 'options_bg', layer='screens'), 
                                                                    Hide("preferences_screen", transition=easeoutbottom),
                                                                    Call("main_menu", load=False)
                                                                    ] at prefs_go_back_pos, hover_enlarge_tilt
    else:
        imagebutton auto "gui/button/go back button %s.png" action [Hide("preferences_screen", transition=easeoutbottom), Return()] at prefs_go_back_pos, hover_enlarge_tilt

    vbox:
        yalign 0.37
        xalign 0.15
        spacing 20
        textbutton "AUDIO" text_align (0.5, 0.5) text_color "#DCE1E5" style "pref_buttons" action SelectedIf(SetVariable("pref_tab", "audio"))
        textbutton "GRAPHICS" text_align (0.5, 0.5) text_color "#DCE1E5" style "pref_buttons" action SetVariable("pref_tab", "graphics")
        textbutton "LANGUAGE" text_align (0.5, 0.5) text_color "#DCE1E5" style "pref_buttons" action SetVariable("pref_tab", "language")
        textbutton "HELP" text_align (0.5, 0.5) text_color "#DCE1E5" style "pref_buttons" action SetVariable("pref_tab", "help")
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
                    text _("Text Speed")  font gui.text_font size 32
                    text _("Auto Speed")  font gui.text_font size 32

                vbox:
                    spacing 14
                    xpos 25
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
                    
                    bar value Preference("text speed")
                    bar value Preference("auto-forward time")

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

        elif pref_tab == "help":
            default device = "keyboard"
            hbox:
                textbutton _("Keyboard"):
                    action SetScreenVariable("device", "keyboard")
                    style "pref_buttons"
                    text_align (0.5, 0.5)
                    text_color "#DCE1E5"
                textbutton _("Mouse"):
                    action SetScreenVariable("device", "mouse")
                    style "pref_buttons"
                    text_align (0.5, 0.5)
                    text_color "#DCE1E5"

                if GamepadExists():
                    textbutton _("Gamepad"):
                        action SetScreenVariable("device", "gamepad")
                        style "pref_buttons"
                        text_align (0.5, 0.5)
                        text_color "#DCE1E5"
            side "c r":
                viewport id "help vp":
                    mousewheel True
                    draggable True
                    area (0, 0, 1200, 600)
                    vbox:
                        text " "
                        if device == "keyboard":
                            use keyboard_help
                        elif device == "mouse":
                            use mouse_help
                        elif device == "gamepad":
                            use gamepad_help
                vbar value YScrollValue("help vp")

        elif pref_tab == "credits":
            side "c r":
                viewport id "credit_vp":
                    area (-10, -10, 1200, 600)
                    mousewheel True
                    draggable True
                    grid 4 4:
                        spacing 30
                        top_margin 10
                        left_margin 10
                        for guy in creditors:
                            $ filename = f"gui/credits/{guy['picture']}.png"
                            vbox:
                                xsize 250
                                ysize 351
                                fixed:
                                    xsize 235
                                    ysize 235
                                    imagebutton idle filename at credit_pic hovered SetVariable('cur_name', guy['name'] + "'s") action OpenURL(guy['link'])
                                text guy['name'] align (0.5, 0.5) size 32 font gui.name_text_font
                                for role in guy['role'].split('\n'):
                                    text role align (0.5, 0.5) size 20

                vbar value YScrollValue("credit_vp")
            
            if cur_name:
                text "Click to go to [cur_name] website!"


transform credit_pic:
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
    {'name': 'NKD', 'picture': 'NKD', 'role': 'Game Director\nCG & sprite artist', 'link': 'https://x.com/enkadenka'},
    {'name': 'Whilo', 'picture': 'Whilo', 'role': 'Chibi Artist', 'link': 'https://x.com/Whilo_art'},
    {'name': 'Enim', 'picture': 'Enim', 'role': 'Chibi Artist', 'link': 'https://www.instagram.com/lorddarkness12600bcxviii/'},
    {'name': 'nuriatheartist', 'picture': 'Nuria', 'role': '3D Artist', 'link': 'https://nuriatheartist.carrd.co/'},
    {'name': 'Leny', 'picture': 'Leny', 'role': 'UI designer', 'link': 'https://www.instagram.com/rann51_/'},
    {'name': 'Tia', 'picture': 'Tia', 'role': 'Live2D rigging', 'link': 'https://www.instagram.com/tia_faisa'},
    {'name': 'Eidolethe', 'picture': 'Eidolethe', 'role': 'Writing', 'link': 'https://eidolethe.itch.io/'},
    {'name': 'A. Villarroel', 'picture': 'A. Villarroel', 'role': 'Writing', 'link': 'https://a-villarroel.itch.io/'},
    {'name': 'Aluwite', 'picture': 'Aluwite', 'role': 'Writing', 'link': 'https://aluwite.carrd.co/'},
    {'name': 'Ica', 'picture': 'Ica', 'role': 'Writing', 'link': 'https://littleicarus7.carrd.co/'},
    {'name': 'AndryStudio', 'picture': 'AndryStudio', 'role': 'Composer', 'link': 'https://andrystudio.carrd.co/'},
    {'name': 'Haikeus', 'picture': 'haikeus', 'role': 'Programmer', 'link': 'https://haikeus.neocities.org'},
    {'name': 'EPI', 'picture': 'EPI', 'role': 'Korean translator', 'link': 'https://epi-zh.itch.io/'},
]
