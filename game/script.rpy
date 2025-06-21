# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
define e = Character("EILEEN")
# image hiyori = Live2D("sprites/hiyori", base=.8, loop=True)
# show hiyori m01 onlayer sprites

label start:  # main game logic loop lives here
    show screen blue_overlay onlayer sprites
    show screen stripes_overlay

    scene menu_art

    # e "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

    # e "Once you add a story, pictures, and music, you can release it to the world!"

    call mc_initialization
    call meet_cute
    
