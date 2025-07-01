image balcony = 'gui/apartment/balcony.png'
image bed = 'gui/apartment/bed.png'
image desk = 'gui/apartment/desk.png'
image kitchen = 'gui/apartment/kitchen.png'
image lounge = 'gui/apartment/lounge.png'
image outside = 'gui/apartment/outside.png'
image door = 'gui/apartment/door.png'
image flat = "gui/HUD_Homescreen.png"

image base = "images/daily_event_art/base.png"
image clean_art = "images/daily_event_art/2.png"
image desk_art = "images/daily_event_art/0.png"
image desk_art_work = "images/daily_event_art/4.png"
image bed_art = "images/daily_event_art/1.png"
image bed_art_book = "images/daily_event_art/6.png"
image balcony_art = "images/daily_event_art/3.png"
image lounge_art = "images/daily_event_art/5.png"
image kitchen_art = "images/daily_event_art/7.png"

define balcony_list = [
    "You decide to get some fresh air.",
    "You look at the people, trying to figure out their lives from their appearance.",
    "You fold the laundry that has been drying on the balcony.",
    "You put the laundry on the balcony to dry."
]
define balcony_outcomes = [
    "Your neighbor is smoking, though, and Icarus wants to head back, worried for your health.",
    "Icarus joins you with a melancholic look in his eyes.",
    "Icarus keeps telling you how he would spook the people outside if he could leave the flat.",
    "Icarus insists on keeping you company.",
]

define bed_list = [
    "You found something interesting while browsing the net on your phone.",
    "You found something funny while reading a book about cats.",
    "You are tired and just want to sleep all the day... {w=0.5}you still end up doomscrolling on your phone.",
    "You are tired and just want to sleep all the day... {w=0.5}and that's what you do, drifting off to sleep.",
    "You remember to write your journal entry for the day.",
    "While you are reading, you find a note slipped inside.",
]
define bed_outcomes = [
    "You end up falling asleep and Icarus shrugs it off.",
    "You end up falling asleep and Icarus also fell asleep nearby.",
    "Having Icarus around makes you happy.",
    "You found that Icarus doodled there.",
    "Icarus shrugged off your behavior.",
    "Icarus approved your behavior, nodding his head.",
    "You are reminded of Icarus.",
]

define desk_list = [
    "You decide to work on your laptop.",
    "You check out what movies have been released recently.",
    "You decide to study for a bit.",
    "You start your favorite game. As soon as you hear the familiar soundtrack, you feel right at home. {w}Which, technically, you are.",
    "You start your favorite multiplayer game and invite your friends.",
    "You fold a paper crane.",
]
define desk_outcomes = [
    "Icarus startles you, and you end up erasing your work for the last hour! {w}Luckily, there's an undo button.",
    "Icarus looks at your screen with childlike curiosity.",
    "Icarus keeps distracting you, but you still manage to not lose focus!",
    "Icarus keeps distracting you. You don't have the strength to refuse such a cutiepie and close your laptop.",
    "Icarus joins you.",
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
    "You just chill on your couch, resting after a hard day of work.",
    "You notice a patch of dirt on the floor and end up cleaning the whole flat...",
]
define lounge_outcomes = [
    "Icarus looks at what you do with puppy eyes",
    "Icarus tries to scoot closer to you.",
    "Icarus is excited to see you having fun.",
    "Icarus is glad to see you not working.",
    "Icarus does not leave your side.",
]

label balcony:
    scene HUD_Homescreen
    scene balcony with dissolve
    python:
        from random import choice, randint
        
        start = choice(balcony_list)
        end = choice(balcony_outcomes)
        location = 'balcony'

        renpy.show('base', layer='sprites', at_list=[paper])
        renpy.transition(easeinbottom, layer='sprites')
        if "clean" not in start:
            cur_img = f'{location}_art'
        else:
            cur_img = 'clean_art'
            
        renpy.show(f'{cur_img}', layer='sprites', at_list=[chibi_art])
        renpy.transition(easeinbottom, layer='sprites')
        renpy.say("", start)
        renpy.say("", end)
        renpy.hide('base', layer='sprites')
        renpy.hide(f'{cur_img}', layer='sprites')
        renpy.transition(dissolve, layer='sprites')
        renpy.pause(0.6)
    return

label bed:
    scene HUD_Homescreen
    scene bed with dissolve
    python:
        from random import choice, randint
        
        start = choice(bed_list)
        end = choice(bed_outcomes)
        location = 'bed'

        renpy.show('base', layer='sprites', at_list=[paper])
        renpy.transition(easeinbottom, layer='sprites')
        if "clean" in start:
            cur_img = 'clean_art'
        elif any(act in start for act in ["book", "journal", 'phone']):
            cur_img = 'bed_art_book'
        else:
            cur_img = f'{location}_art'

        renpy.show(f'{cur_img}', layer='sprites', at_list=[chibi_art])
        renpy.transition(easeinbottom, layer='sprites')
        renpy.say("", start)
        renpy.say("", end)
        renpy.hide('base', layer='sprites')
        renpy.hide(f'{cur_img}', layer='sprites')
        renpy.transition(dissolve, layer='sprites')
        renpy.pause(0.6)
    return

label desk:
    scene HUD_Homescreen
    scene desk with dissolve
    python:
        from random import choice, randint
        
        start = choice(desk_list)
        end = choice(desk_outcomes)
        location = 'desk'

        renpy.show('base', layer='sprites', at_list=[paper])
        renpy.transition(easeinbottom, layer='sprites')
        if "clean" in start:
            cur_img = 'clean_art'
        elif any(act in start for act in ["work", "study", "screen"]):
            cur_img = 'desk_art_work'
        else:
            cur_img = f'{location}_art'

        renpy.show(f'{cur_img}', layer='sprites', at_list=[chibi_art])
        renpy.transition(easeinbottom, layer='sprites')
        renpy.say("", start)
        renpy.say("", end)
        renpy.hide('base', layer='sprites')
        renpy.hide(f'{cur_img}', layer='sprites')
        renpy.transition(dissolve, layer='sprites')
        renpy.pause(0.6)
    return

label kitchen:
    scene HUD_Homescreen
    scene kitchen with dissolve
    python:
        from random import choice, randint
        
        start = choice(kitchen_list)
        end = choice(kitchen_outcomes)
        location = 'kitchen'

        renpy.show('base', layer='sprites', at_list=[paper])
        renpy.transition(easeinbottom, layer='sprites')
        if "clean" in start:
            cur_img = 'clean_art'
        else:
            cur_img = f'{location}_art'

        renpy.show(f'{cur_img}', layer='sprites', at_list=[chibi_art])
        renpy.transition(easeinbottom, layer='sprites')
        renpy.say("", start)
        renpy.say("", end)
        renpy.hide('base', layer='sprites')
        renpy.hide(f'{cur_img}', layer='sprites')
        renpy.transition(dissolve, layer='sprites')
        renpy.pause(0.6)
    return

label lounge:
    scene HUD_Homescreen
    scene lounge with dissolve
    python:
        from random import choice, randint
        
        start = choice(lounge_list)
        end = choice(lounge_outcomes)
        location = 'lounge'

        renpy.show('base', layer='sprites', at_list=[paper])
        renpy.transition(easeinbottom, layer='sprites')
        if "clean" in start:
            cur_img = 'clean_art'
        else:
            cur_img = f'{location}_art'

        renpy.show(f'{cur_img}', layer='sprites', at_list=[chibi_art])
        renpy.transition(easeinbottom, layer='sprites')
        renpy.say("", start)
        renpy.say("", end)
        renpy.hide('base', layer='sprites')
        renpy.hide(f'{cur_img}', layer='sprites')
        renpy.transition(dissolve, layer='sprites')
        renpy.pause(0.6)
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
            if cur_aff_level != max_aff_level:
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
