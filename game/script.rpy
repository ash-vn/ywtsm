# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
define e = Character("EILEEN")
# image hiyori = Live2D("sprites/hiyori", base=.8, loop=True)
# show hiyori m01 onlayer sprites

label start:  # main game logic loop lives here
    show screen blue_overlay onlayer sprites
    show screen stripes_overlay

    call mc_initialization
    call meet_cute
    call rejection_of_relationship
    call giving_the_relationship_a_chance
    
    # TnT

    if (blue > purple and blue > orange) or (blue == purple and blue > orange and color == 'blue') or (blue == orange and blue > purple and color == 'blue'):
        $ player_color = 'blue'
    elif (purple > blue and purple > orange) or (purple == blue and purple > orange and color == 'purple') or (purple == orange and purple > blue and color == 'purple'):
        $ player_color = 'purple'
    elif (orange > blue and orange > purple) or (orange == blue and orange > purple and color == 'orange') or (orange == purple and orange > blue and color == 'orange'):
        $ player_color = 'orange'
    