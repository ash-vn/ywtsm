label mc_initialization:
    $ ILORA.name = renpy.input("(But before we start, what do you wish to be called?)") or "ILORA"
    define points = {'blue': 0, 'purple': 0, 'orange': 0}
    define max_aff_level = 0
    define cur_aff_level = 0
    define player_color = 'green lol'

    #    - TnT - #4 variables
    # Week 3
    define fish_count = -1
    define fish_name = None
    define hugged = None

    # Week 4
    define li2 = None  # valid states: None, 'alive', 'dead'

    #    - #5
    define stay = False
    define low_affinity = False
    define high_affinity = False

    #    - #7
    define yearn = False

    default persistent.endings_seen = [False] * 16
    return


label aff_0:
    $ cur_aff_level = 0
    return

label aff_1:
    $ cur_aff_level = 1
    $ max_aff_level = max([cur_aff_level, max_aff_level])
    $ points[player_color] += 1
    return

label aff_2:
    $ cur_aff_level = 2
    $ max_aff_level = 2
    $ points[player_color] += 2
    return

label unlock_cg(cg_name):
    python:
        for i in range(len(persistent.cg_list)):
            if "images/" + persistent.cg_list[i]['file'] + ".png" == cg_name:
                if not persistent.cg_list[i]['date']:
                    from datetime import datetime
                    today = datetime.now().date()
                    persistent.cg_list[i]['date'] = today.strftime('%m/%d/%Y')
                    renpy.play("assets/audio/new_ping.mp3", audio)
                    renpy.say("", "Unlocked a new CG!")
    return

label ending(number):
    call unlock_cg("endings/END[number]") from _call_unlock_cg_1

    scene Image("images/endings/END[number].png") with Dissolve(5.0)

    "{b}END.{/b}"
    pause

    scene black with Dissolve(5.0)

    jump main_menu