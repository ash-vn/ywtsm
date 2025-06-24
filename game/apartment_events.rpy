image balcony = 'gui/apartment/balcony.png'
image bed = 'gui/apartment/bed.png'
image desk = 'gui/apartment/desk.png'
image kitchen = 'gui/apartment/kitchen.png'
image lounge = 'gui/apartment/lounge.png'
image outside = 'gui/apartment/outside.png'

define daily_events = [
    [["", "Icarus decided to spook you!"], ["ICARUS", "Boo!"], ["", "You got scared!"]],
    [["", "Icarus hugged you from behind."], ["", "Your heart just melted!"]], 
[["", "Event 3"]],
[["", "Event 4"]],
[["", "Event 5"]],
[["", "Event 6"]],
[["", "Event 7"]],
[["", "Event 8"]],
]

define balcony_list = [
    "You decide to get some fresh air.",
]
define balcony_outcomes = [
    "Your neighbor is smoking, and you decide to head back.",
]

define bed_list = [
    "You decide to go to sleep.",
]
define bed_outcomes = [
    "You end up cuddling with Icarus.",
    "You have insomnia for the whole night :(:(:(:(.",
    "You get gay disese"
]

define desk_list = [
    "You decide to work on your laptop.",
]
define desk_outcomes = [
    "Icarus startles you, and you end up erasing your work for the last hour! Luckily, there's an undo button.",
    "Icarus looks at your screen with childlike curiosity.",
]

define kitchen_list = [
    "You attempted to cook something and Icarus is curious.",
    "You tried to invent some random new recipe.",
    "Today Icarus is excited about a recipe he saw on TV.",
    "Kitchen is a bit dirty and you decide to clean up.",
    "You decided to spend your time reading a recipe thread.",
    "You followed the guide of some cooking reels you saw."
]
define kitchen_outcomes = [
    "You give up, and Icarus handles it.",
    "You become lazy midway and leave it, Icarus shakes his head.",
    "And it turned good, Icarus' eyes sparkling.",
    "Turns out it was just fine. Icarus gives a nod.",
    "Sadly, it failed, but Icarus takes it with a smile.",
    "Icarus observe you the whole time with a light smile",
    "Icarus got clumsy, it became a disaster!"
]

define lounge_list = [
    "You decide to watch a movie that's been dusting forever on your watchlist.",
]
define lounge_outcomes = [
    "Icarus tries to cuddle with you, but ends up going right through your skin.",
]

label balcony:
    scene HUD_Homescreen
    scene balcony with dissolve
    python:
        from random import choice, randint
        renpy.say("", choice(balcony_list))
        renpy.say("", choice(balcony_outcomes))
    return

label bed:
    scene HUD_Homescreen
    scene bed with dissolve
    python:
        from random import choice, randint
        renpy.say("", choice(bed_list))
        renpy.say("", choice(bed_outcomes))
    return

label desk:
    scene HUD_Homescreen
    scene desk with dissolve
    python:
        from random import choice, randint
        renpy.say("", choice(desk_list))
        renpy.say("", choice(desk_outcomes))
    return

label kitchen:
    scene HUD_Homescreen
    scene kitchen with dissolve
    python:
        from random import choice, randint
        renpy.say("", choice(kitchen_list))
        renpy.say("", choice(kitchen_outcomes))
    return

label lounge:
    scene HUD_Homescreen
    scene lounge with dissolve
    python:
        from random import choice, randint
        renpy.say("", choice(lounge_list))
        renpy.say("", choice(lounge_outcomes))
    return

label outside:
    scene HUD_Homescreen
    
    show screen stripes_overlay
    scene black with easeoutbottom
    scene outside with easeintop
    menu:
        "Do you really want to go outside and leave Icarus alone at home?"
        "Yes.":
            "You leave Icarus alone for some time."
            if last_aff_level != max_aff_level:
                "Surely nothing will happen, right?"
        "No. Let me get back to the apartment.":
            "You decide to go out... some other day."
            scene black with dissolve
            python:
                renpy.transition(dissolve)
                renpy.call_screen('flat_navigation')
    return

transform chibi_art:
    zoom 0.3
    yalign 0.35
    xalign 0.5

transform paper:
    yalign 0.3
    xalign 0.5

label daily_event_chance:
    image base = "images/daily_event_art/base.png"
    image flat = "gui/HUD_Homescreen.png"
    image im0 = "images/daily_event_art/0.png"
    image im1 = "images/daily_event_art/1.png"
    image im2 = "images/daily_event_art/2.png"
    image im3 = "images/daily_event_art/3.png"
    image im4 = "images/daily_event_art/4.png"
    image im5 = "images/daily_event_art/5.png"
    image im6 = "images/daily_event_art/6.png"
    image im7 = "images/daily_event_art/7.png"
    # scene flat
    python:
        from random import choice, randint
        chance = randint(0, 8)
        if chance <= 7:
            renpy.show('base', layer='sprites', at_list=[paper])
            renpy.transition(easeinbottom, layer='sprites')
            renpy.show(f'im{chance}', layer='sprites', at_list=[chibi_art])
            renpy.transition(easeinbottom, layer='sprites')
            # renpy.show(f)
            renpy.say(daily_events[chance][0][0], daily_events[chance][0][1])
            for e in daily_events[chance]:
                renpy.say(e[0], e[1])
            renpy.hide('base', layer='sprites')
            renpy.hide(f'im{chance}', layer='sprites')
            renpy.transition(dissolve, layer='sprites')
            renpy.pause(0.6)
    return