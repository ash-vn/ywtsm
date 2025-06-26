label your_hard_work():
    "\[This is just a placeholder for the event that's going to happen right after week one ends.]"
    "\[Sorry for being like this! But if you want to make a choice that much, be my guest...]"
    menu:
        "Make affinity 0!":
            $ cur_aff_level = 0
        "Make affinity 1!":
            $ cur_aff_level = 1
            $ max_aff_level = max([cur_aff_level, max_aff_level])
        "Make affinity 2!":
            $ cur_aff_level = 2
            $ max_aff_level = 2
    "I see."
    "Your wish is my command. Just don't regret your choice."
    return

label pet_goldfish_1():
    scene kitchen with dissolve
    'Sunlight slants across the counter. A couple of half-folded paper cranes lay strewn next to your glass of water.'

    show icarus at icarus_transform with dissolve
    'Icarus is crouched on the floor near the table leg, focused on his latest crane, brows furrowed in adorable concentration.'

    hide icarus with dissolve
    """
    You’re lying on the couch lazily scrolling through some social media reels. 

    But then, you freeze at a particularly cute thumbnail of a fish. 

    A lazy goldfish swimming in a giant tank. 
    """

    ILORA "(It’s been quiet lately. Maybe it’s time for something to spice things up a bit.)"

    ILORA "“I’m thinking of getting a goldfish.”"

    show icarus at icarus_transform with dissolve
    ICARUS "“Gold…fish?”"

    "You glance up. He’s peeking over the table now, slowly blinking as if you just spoke in riddles."

    ICARUS "“But why?”"

    ILORA "“I don’t know, could be fun. Plus, fishes are so low-maintenance.”"
        
    ILORA "“It won’t try to talk to me while I’m brushing my teeth. Or hover behind me while I sleep.”"

    "You give him a wink as he holds his hands up, mock-innocent."

    ICARUS "“I was not pointlessly hovering. I was…guarding you, clearly.”"

    ILORA "“Plus, goldfishes are so cute! They’re little orange blimps with no concept of consequences. You feed them. They do a little spin. That’s it.”"

    'You jump off the couch and begin pacing around, faster and faster.'


    ILORA "“And the bowl—yeah, the bowl can go on the table, maybe. Or the window. Near the light!”" 

    ILORA "“It’ll reflect on the walls in the morning. That’s nice. That’s peaceful.”"

    'Without missing a beat, you grab the keys on the table and head towards the door. '

    ILORA "“See you soon! I’m going to go pet-shopping.”"

    ICARUS "“Whoa, whoa. Hold on, right now?”"

    ILORA "“Yes, bye!”" 

    'And before he could say more, you’re out the door.'


    scene black with dissolve
    pause(1.0)
    scene bg with dissolve
    scene kitchen with dissolve

    'You enter, balancing a plastic bag with a sloshing clear cup and a little orange blur swimming tight, frantic circles inside.'

    show icarus at icarus_transform with dissolve
    ICARUS "“Wow, you really did it.”" 

    'He tilts his head, studying the bag in your hands intensely. '



    if cur_aff_level == 2:
        $ fish_count = 2

        ICARUS "“And you got two, at that.”" 

        ILORA "“Mhmm! I thought one might get too lonely.”" 

        ILORA "“Look at them. Aren’t they adorable together?”" 

        'You coo as you bring them closer to his face. '

        ILORA "“What shall I name them~?”"

        'He takes them out of your hands, gently helping to pour the two into the little bowl.' 

        ICARUS "“How about Icarus and [ILORA.name.capitalize()]?”" 

        ICARUS "“After all, you did say they looked good together.”"

        'You feel your cheeks redden and out of instinct, burst into laughter.' 



    else:
        $ fish_count = 1

        'It’s hard to tell how he feels about your spontaneous domestic purchase. '

        ILORA "“Okay, so please tell me this was the best decision I’ve ever made.”" 

        ICARUS "“Uhh, well, best is a strong word.”" 

        ICARUS "“But it might be a good decision. Depending on how this pans out.”"

        'You carefully pour the fish into the prepared little bowl. '

        ILORA "“Hmm, what shall we name him?”" 

        'Icarus leans closer, squinting.' 

        ICARUS "“How about ‘Tragic’?”"

        ILORA "“...What.”"

        ICARUS "“He looks like he’s regretting his life decisions. Deeply.”" 

        ILORA "“The fish was literally born three days ago.”"

        'Icarus shrugs offhandedly. '

        ICARUS "“Some souls age fast.”"

        "You look at the fish."

        while not fish_name:
            $ fish_name = renpy.input("What do you name it..?")

    if fish_name and fish_name.lower() == 'tragic':

        'Icarus smirks. You’re not sure why, but he seems extremely pleased with the name.' 

        'Perhaps he feels sorry for the fish? '

    ILORA "“Welcome home, [fish_name].”"

    "Icarus sighs dramatically."

    ICARUS "“Poor guy.”"
    return

label pet_goldfish_2():
    # if fish_count == 1 and cur_aff_level == 1:
    scene kitchen with dissolve
    show icarus at icarus_transform with dissolve
    ILORA "“Hey, so I might need you to feed [fish_name].”"

    'Icarus raises an eyebrow, remaining silent otherwise.'

    ILORA '“I’m working a little overtime today so I can’t babysit.”'

    ILORA '“Please?”'

    ICARUS '“You’re…working overtime? Why would they make you do that?” '

    'He frowns, visibly concerned.'

    ICARUS '“I feel like I’ve been seeing you less and less lately…Can I get a hug?”'

    menu:
        "Oblige.":
            $ hugged = True
            'You sigh and open your arms. '

            'He moves in without hesitation, arms wrapping around your waist a little tighter than you expected.'

            ICARUS "{size=20}{color=#99B}{cps=*0.2}“{i}I missed this…{/i}”"

            ICARUS '“I’ll feed [fish_name]. I promise. Even if he doesn’t blink back.”'
        "Don't.":
            $ hugged = False
            'You shift back, subtly avoiding the hug.' 

            ILORA '“I’m really in a rush. Raincheck?”'

            'He lowers his arms, smile thinning.'

            ICARUS '“Right. Sure. Of course.”'

            ICARUS '{cps=*0.2}“I’ll feed [fish_name].”'

    scene black with dissolve
    pause(1.0)
    
    scene kitchen with dissolve

    if hugged:
        """
        You stumble back into the house at 9PM, feeling like you’re about to pass out. 

        The lights are on, warm and low. A folded blanket sits neatly on the couch. You catch the faint scent of black tea and candle wax.

        [fish_name] swims slow, tranquil loops, totally unbothered by the chaos of your life. 

        The water is clean, food flakes mostly gone.
        """

        show icarus at icarus_transform with dissolve
        ICARUS '“You’re back!”'

        "Before you can react, you're swept up in a full-body tackle-hug."

        with vpunch

        ILORA '“Whoa!”'

        'Icarus wraps himself around you like a clingy koala, head buried into your shoulder. '

        ICARUS '“Are you proud of me? I’ve been getting along so well with [fish_name].”'

        ICARUS '“I’m basically his other parent now.” '

        ILORA '“...Oh. I see, that’s good.” '

        'You blink at his sudden enthusiasm, which was entirely unexpected, given how he nearly named your pet “Tragic” when they were first introduced. '

        'He spins to face the bowl, dramatically placing a hand on the rim like a proud coach. '

        ICARUS '“I gave him pep talks while you were gone. Told him not to give up on swimming in circles.”'

        ILORA '“Truly inspirational.”'

        ILORA '“...You did good. Thank you.” '

        'His ears perk up. It’s almost embarrassing how quickly his face lights up.'

    else:
        $ fish_count = 0
        """
        You stumble back into the house at 9PM, feeling like you’re about to pass out. 

        The thud of your suitcase subtly echoes in the quietness of your apartment. 

        There is no hum of music. No scent of tea. No scattered cranes in progress.

        You frown slightly, scanning the space. 

        And then you see [fish_name] –– {w}{cps=*0.2}floating at the top of the fishbowl, belly-up, motionless. 

        Food flakes are strewn around the body, untouched. 

        You stare, gaping at the scene for a long time. 
        """

        ILORA '{cps=*0.6}“You’ve got to be kidding me.” '

        show icarus at icarus_transform with dissolve
        ICARUS '“You’re back~!”'

        'Icarus enters from the hallway, drying his hands with a towel. His smile is as bright as anything. '

        ICARUS '“I was just cleaning the dishes. The pan was being kinda aggressive, but I won.”'

        ICARUS '“Like I always do.”'

        'You don’t say anything. You just look at him.' 

        ICARUS '“What’s wrong? Why do you look upset?”'

        ICARUS '“Was the work really that stressful? Let me give you a hug…”'

        'But as he walks closer you shove him back a little.' 

        ILORA '“You had one job and you failed in the worst way possible!”'

        'He follows your gaze towards [fish_name].' 

        ICARUS '“Ohh.”'

        # smile sprite
        ICARUS '“Huh. That was sudden.” '

        ILORA '“You promised to take good care of [fish_name].”'

        ICARUS '“I did.”' 

        ICARUS '“But doesn’t some fish just don’t fit it? Haha. Perhaps ‘Tragic’ was truly a suitable name.”'

        'He shrugs as if discussing the weather.'

        ICARUS '“Oh well, you can just buy another one. And you’re back now. That’s what matters, right?”'

        'He walks past you into the kitchen, humming softly. The kettle clicks on.'
    return

label just_a_friend:
    "Week 4 - Just a Friend event"
    pass
    return