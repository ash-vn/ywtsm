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
    # imagebutton auto "gui/button/go back button %s.png" action Call("main_menu", load=False) at ending_go_back_pos, hover_enlarge_tilt

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
    fit "contain"
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