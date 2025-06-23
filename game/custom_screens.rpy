image gallery_bg = 'gui/gallery bg.png'
image HUD_Homescreen = "gui/HUD_Homescreen.png"

label gallery:
    scene gallery_bg
    call screen navigation

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

transform ending_pos:
    yalign 0.05
    xalign 0.5

transform ending_go_back_pos:
    yalign 0.5
    linear 1.0 xalign 0.01
    linear 1.0 xalign 0.015
    repeat

screen ending_screen:
    imagebutton auto "gui/button/go back button %s.png" action Call("main_menu", load=False) at ending_go_back_pos

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
    # add "gui/button/apartment button idle.png" xalign 0.03 yalign 0.15 at appear_from_alpha

    imagebutton idle "gui/button/balcony button idle.png" at balcony_pos action Call('balcony')
    imagebutton idle "gui/button/bed button idle.png" at bed_pos action Call('bed')
    imagebutton idle "gui/button/desk button idle.png" at desk_pos action Call('desk')
    imagebutton idle "gui/button/kitchen button idle.png" at kitchen_pos action Call('kitchen')
    imagebutton idle "gui/button/lounge button idle.png" at lounge_pos action Call('lounge')


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