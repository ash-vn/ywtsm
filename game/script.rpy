# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
define e = Character("EILEEN")
# image hiyori = Live2D("sprites/hiyori", base=.8, loop=True)
# show hiyori m01 onlayer sprites

label start:  # main game logic loop lives here
    show screen blue_overlay onlayer sprites
    show screen stripes_overlay

    stop music

    call mc_initialization from _call_mc_initialization
    call meet_cute from _call_meet_cute
    call rejection_of_relationship from _call_rejection_of_relationship
    call giving_the_relationship_a_chance from _call_giving_the_relationship_a_chance
    
    # TnT

    if (blue > purple and blue > orange) or (blue == purple and blue > orange and color == 'blue') or (blue == orange and blue > purple and color == 'blue'):
        $ player_color = 'blue'
    elif (purple > blue and purple > orange) or (purple == blue and purple > orange and color == 'purple') or (purple == orange and purple > blue and color == 'purple'):
        $ player_color = 'purple'
    elif (orange > blue and orange > purple) or (orange == blue and orange > purple and color == 'orange') or (orange == purple and orange > blue and color == 'orange'):
        $ player_color = 'orange'
    
    define day = 0
    while day < 4 * 7:
        $ day += 1
        $ week = (day - 1) // 7 + 1
        $ week_day  = (day - 1) % 7 + 1
        hide screen quick_menu
        scene black
        hide screen blue_overlay onlayer sprites
        with dissolve
        pause(0.5)

        python:
            renpy.transition(dissolve)
            renpy.show_screen('day', day)
            renpy.play("assets/audio/rising_ping.mp3")
            renpy.pause(2.3)
            renpy.hide_screen('day')
            renpy.transition(dissolve)
            renpy.pause(0.8)

        if week == 2 and week_day == 1:
            call your_hard_work from _call_your_hard_work
        elif week == 3 and week_day == 1:
            call pet_goldfish_1 from _call_pet_goldfish_1
        elif week == 3 and week_day == 5 and fish_count == 1 and cur_aff_level == 1:
            call pet_goldfish_2 from _call_pet_goldfish_2
        elif week == 4:
            call just_a_friend from _call_just_a_friend
        else:
            python:
                renpy.call_screen('flat_navigation')
                renpy.transition(dissolve)

screen day(day):
    text "week [(day - 1) // 7 + 1] - day [(day - 1) % 7 + 1]" font "assets/fonts/KyivTypeSans-Light3.ttf" color "#DCE1E5" size 72 xalign 0.55 yalign 0.42
    add "gui/window_icon.png" xalign 0.3 yalign 0.4 zoom 0.25 at crane_movement

transform crane_movement:
    rotate 0.0
    pause(0.5)
    rotate -6.0
    pause(0.5)
    rotate 0.0
    pause(0.5)
    rotate 6.0
    pause(0.5)
    repeat