label mc_initialization:
    $ ILORA.name = renpy.input("(But before we start, what do you wish to be called?)") or "ILORA"
    define blue = 0
    define purple = 0
    define orange = 0
    define max_aff_level = 0
    define cur_aff_level = 0
    define color = 'green lol'

    #    - TnT - #4 variables
    # Week 3
    define fish_count = -1
    define fish_name = None
    define hugged = None

    # Week 4
    define li2 = None  # valid states: None, 'alive', 'dead'

    default persistent.endings_seen = [False] * 16