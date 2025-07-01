label your_hard_work():
    """Work, coffee, typing, and paper cranes. The rain is pouring, yet the vibes from the house are anything but gloomy. 

    You are working on a text draft – a personal project of yours that fosters into one of your most cherished hobbies.

    You sit on your desk sipping a warm matcha latte. A drink that is neither too sweet nor too bitter, a delicate neutral balance. 

    The sugar rush provides the energy you need to keep typing.

    It’s your usual routine, untethered to whichever place you ever called home. You sit upright, fingers dancing around the keys. 

    One clear difference is next to you, Icarus who wanders like a cat loitering around. Sometimes close enough that he would have a place to belong in the corner of your eye.

    Silence that feels tranquil yet off lingers around you.

    He is meddling with paper cranes again today, as usual, as he would.

    This week, you would join passively, assisting in folding and grabbing more origami paper.

    However, what’s on screen is still your main priority. The keyboard is still the top resting place for your fingers.

    Icarus sometimes glances over, until he actually asks."""

    ICARUS "“[ILORA.name]… busy?”"

    menu:
        "Give a nod":
            call aff_1 from _call_aff_1
            """
            There was no obvious reaction. But out of nowhere after that, somehow you found his head leaned in to take a quick peek at your screen. 

            From the shock, you fumble and accidentally delete a portion of your work.
            """

            ICARUS "“Oh? Did I catch you off guard?” "

            ILORA "“You almost made me delete my work because of that! Lucky there is a undo button” "

            "He looks surprised before giving you a half-sulky look."

            ICARUS "“Sorry! I just wanted to see your work.”"

            """
            Icarus backs off, rather nonchalantly goes back to his paper cranes. 

            You sigh, restoring your lost work and continue to type. Despite the brief scare, the moment is quickly over as soon as it started.
            """

            ILORA "“Not actually sorry, aren’t you?”"

            """
            But there, you saw only a brief quiver of smile.

            You can’t help but wonder though what was he thinking.
            """

        "Give a short glance":
            call aff_0 from _call_aff_0

            """His eyebrows arose as you caught his eye.

            He then diverted his attention to your screen, leaving the paper cranes. 

            You remain focused on your work, unfazed. Not giving him so much as a flinch as you typed away, engrossed in your work."""

            ICARUS "“[ILORA.name]…?”"

            "He tries to get your attention."

            ICARUS "“Not answering…?” "

            """You truly couldn’t care much. Being so absorbed in your work that you paid no mind to him.

            As time goes, you can hear a faint sigh of defeat, some rustle of feet stepping away and hands making contact with paper cranes. 

            However, the feeling of being watched still lingers.

            Keyboard ticks soften your annoyed exhale. It’s still unfair to have to share a supposedly your only - resting place - with a stranger, even more a ghost that is.

            You continued to type away, but seeing his figure back facing you sitting down on the floor meddling with papers, you couldn’t help but to get reminded of a certain dog that waits for his owner. 

            One that didn’t end well.

            On a certain corner, some muttered sound can be heard faintly.""" 

            ICARUS "“Did I do something wrong? Did I say something wrong? Did I… mess things up again…?” "

        "Give attention":
            call aff_2 from _call_aff_2

            ILORA "“Yeah, but it’s just a way to relax. What’s the matter?”."

            """Thinking on a whim, Icarus decided it’d be a great idea to face-plant the keyboard of your notebook. 

            You had been caught off guard by something that took you back to a past you wanted to forget and you for a while felt threatened.

            In your irritation, it caused a trigger reaction - a sucker punch special for the ghost."""

            ICARUS "“Ouch!” "

            "It’s not his lucky day, or however he controls his astral being of getting physical with this realm."

            ILORA "“Maybe next time don’t just shove your face on my screen… Acting like that only gets you this kind of attention, you know?…”"

            ICARUS "Of course I didn’t mean to… but it's fine, right?"

            "You take a deep sigh."

            ILORA "“How about you just sit down, and have a look.”"

            """You move over to let him see what’s on the screen. 

            He skims through, eyes occasionally stopping on specific sentences.

            You sit back and watch, stretching while you observe his rather expressive reaction. 

            Eventually you would continue to peek at your own writing, making sure that you didn’t miss anything.

            You couldn’t risk making your creation not in a standard.

            Icarus takes a long glance at your writing, taking in all the details that you have taken your time to. 

            You watch his eyes go from words to sentences and then his gaze eventually meets yours.""" 

            ICARUS "“Wow you really are a good writer, you know?” "

            ILORA "“Wow, surprised it took you long enough to figure out, I would have thought that the way I speak would have given it all away.”" 

            "You state as you give him a gaze that basically states “are you serious” as you raise your eyebrow." 

            ILORA "“Finish your commentary?” "

            ICARUS "“I think… it really did go deep.”"

            "There was something in his eyes that you cannot comprehend while he gave a short stop for his voice."
            ICARUS "“Maybe it really left me in a trance just now…”"

            ICARUS "“I mean there’s always some sort of light around you… but your way with words is one that even I can’t question.”"

            "Light? You chuckled inside."

            ILORA "“Well, seems honest enough… Thank you?”" 

            """There was never a single lie. 

            He took a paper crane that he had just made and began doodling rain all over it, one of the symbols that revolved in your chapter. 

            Seems like your writing left a lasting impression.

            However you keep skimming over the page, checking for any mistakes.

            After all, one can’t be too sure.

            A moment to lean back and stretch, too much time has been spent on typing and editing that your joints feel sore.

            On one hand, Icarus’s eyes glitters like he wants something right at that moment, but you can’t quite pinpoint exactly what it is that he suddenly seems to desire.""" 

            ILORA "“Is there something you want?”" 

            ICARUS "“Yeah… there is one…”" 

            """His gaze however, didn’t make the impression of a person willing to convey what’s seemingly a secret. You resorted back to your work.

            A cliffhanger. All you know is that something caught his mind, as he completely dropped his attention from the paper cranes even as you went back to editing.

            He looked at with a gaze of admiration that was even more deeper than one that he would give to paper cranes created by his bare hands.

            It was almost like you became his new muse."""

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
            call aff_1 from _call_aff_1_1
            $ hugged = True
            'You sigh and open your arms. '

            'He moves in without hesitation, arms wrapping around your waist a little tighter than you expected.'

            ICARUS "{size=20}{color=#99B}{cps=*0.2}“{i}I missed this…{/i}”"

            ICARUS '“I’ll feed [fish_name]. I promise. Even if he doesn’t blink back.”'
        "Don't.":
            call aff_0 from _call_aff_0_1
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
    """
    12:27 AM. A very specific time, one that you wouldn’t necessarily find anyone loitering about or wandering their way home, but one you now found yourself completely at the mercy of.

    Your vision slipped in and out of consciousness. Yellow lights faintly over a sidewalk, the sound of shoddy cars passing by, and the weight of someone's arms holding you tight to their back.

    Through the faint glimpses of the waking world you had, you recognized the man. It was Jang Seong-Jin, your Colleague.

    Although unclear as to why, he was carrying you back home, this late at that. 

    More likely than not, if it were anyone else, you would’ve just been left at work until you awoke, but not Seong-Jin. 

    For better or for worse, this man was close to you.

    Your body pressed against his as you felt a steep incline upward with each step up the complex stairs.
    """
    SEONGJIN "“You’re lucky you weigh nothing.”"

    SEONGJIN "“Any more than this and I would’ve left you at the bottom of the stairs.”"
    """
    Suddenly, you came to a halt. There was a faint clicking sound as he rattled around, trying to fit your keys through the keyhole.

    With each failure, you could feel him getting more restless, even in your half-lucid state. 
    """
    SEONGJIN "“Dammit, go in.”"

    "Almost as if he were aggravated, he shoved the key into the door, finally greeted with the sweet sensation of an unlock."

    "He pushed your door open quietly, stepping into your living room before slamming it shut again."

    # (VFX: Door slamming sound with minor screen shake)
    with hpunch

    "You felt his body jolt at the loud noise the slam had caused. "
    SEONGJIN "“Sorry.”"
    """
    He turned to look back at you, making sure he hadn’t disturbed your slumber.

    A heavy sigh was heaved at this whole ordeal. Despite it, Seong-Jin’s body failed to alleviate the shaking. 

    Step after step, finally, you landed upon your couch, its cushions engulfing you like sand on a sweet summer beach.

    Pressure was released from your feet as Seong-Jin removed your work shoes.

    The quiet was off-putting. There was a slight buzzing noise from something in the room, a faint wind blowing past the open balcony curtains.

    It was an eerie sensation, one you could perceive even in your now deep sleep.
    """

    SEONGJIN "“...You really haven’t changed.”"

    "Although it was just for a moment, the room's cold air felt ever so slightly tenser."

    if cur_aff_level == 2:
        
        "A silent ringing noise came from Seong-Jin’s pocket, his gaze falling on you for a moment before answering. "

        SEONGJIN "“Hello?”"

        SEONGJIN "“Yeah, yeah, just dropped her off. I’m going now.”"

        SEONGJIN "“Oh please, aren’t you the one asking for help?”"

        "The responses over the phone were unintelligible, but his irritation with them was contrastingly palpable."

        SEONGJIN "“See ya. Tch.”"

        """
        With a passive-aggressive tap, he hung up the call, an irritated smirk plaguing his gentle face.

        Once more, he found his eyes drawn to your resting face, a moment's thought occupying his mind, before being swept away by his rationale.

        After a pause, you faintly heard the sound of footsteps trailing off, followed by the clicking of the front door as it quietly shut.

        With no more disturbances in reach, your slumber could finally be a peaceful one.

        Or so it would seem, as even through your unconscious rest, you could still feel the cold breeze of an open balcony door.

        It should’ve been something perturbing, but instead, rather than it growing cold, you felt your body grow warm with the heat of a blanket, slowly tucked over you.

        Although it was faint, the sensation of a hand gently brushing aside your messy hair could be felt before vanishing into the empty night.
        """


        # (TIME SKIP)
        scene black with dissolve

        scene lounge with dissolve

        show icarus at icarus_transform with dissolve

        """
        Your eyes dazily opened to the dimly morning-lit interior of your living room, the window curtains covered, and the balcony door closed.

        A heavy feeling weighed down on your tired body, your arm rubbing against your eyes as you looked toward the sliver of sunlight peeking through.

        You couldn’t tell what time it was, or how long you’d been asleep, but one thing was for certain.

        That couch was not sleep-worthy.
        """

        ICARUS "“Rise and shine, sleepyhead!”"

        "From your side rose Icarus, a sense of triumph as he did so. Despite his victorious appearance, however, his face told less of a grandiose tale."

        ILORA "“You look like you’ve seen a ghost.”"

        ICARUS "“More like a wolf in sheep's clothing.”"

        "He held his arms crossed, wearing a slight pout. You could tell he wasn’t exactly enthusiastic about your ‘friend’ from last night."

        "You let out a small sigh."

        ILORA "{i}(So Seong-Jin did come over.){/i}"

        "Perhaps a part of you had hoped that it was just a dream, but Icarus’ behavior made that unfortunately hard to believe."

        ICARUS "“What’d he think he was doing, carrying you about like that?”"

        ICARUS "“And he treated you with such carelessness! Doesn’t he know you’re sensitive to sound?”"

        "He turned away, reaching out toward some half-finished paper cranes. Amidst his vexed folding, you heard him mutter something under his breath."

        ICARUS "“Honestly… I would’ve treated you so much better.”"

        menu:
            "Agree":
                call aff_1 from _call_aff_1_2
                "You gently lean toward Icarus, taking hold of one of the unfolded cranes next to him."

                ILORA "“I’m sure you would’ve.”"

                ICARUS "“I’m serious!”"

                "A slight chuckle emerged from you, drowsiness still ever present, yet slowly fading in place of a kind warmth. "

                ILORA "“So am I.”"

                "You placed the finished crane down on the floor next to Icarus before getting up and starting toward the kitchen."

                "Although it could’ve just been your imagination, for a second, it looked as if Icarus’ ears were blushing a bright red."

            "Ignore him":
                call aff_0 from _call_aff_0_2
                "You overheard nothing. Whatever he may have said, it went in one ear and left the other just as quickly. "

                "With a quick stretch, you hopped off the couch and started toward the kitchen, each a drowsy step leading your way."

                "Icarus remained oblivious to this in his grumpy fit, continuing to yap on about Seong-Jin’s presence."

                ICARUS "“How dare he lay his impure hands on her? I swear the next time I see him, it’s over!”"

                ICARUS "“And he didn’t even take off his shoes before entering. Look at all this dirt he tracked in.”"
        
        ILORA "“Don’t fret over him too much.”"

        """
        With the activation of the stove, the kettle lit up with bursting heat.

        As it rose to a boil, you found your eyes drawn to the flame at its source. 

        That flickering flame, ever so warm yet well beyond hot enough to scorch anything that got too close.

        How long could that fire last?
        """

        ILORA "(Jang Seong-Jin.)"

        """
        It was a name you recognized beyond just the colleague who had left you here. 

        A name so distant, yet so close to the ‘[ILORA.name]’ you were now.

        He was a fool. Someone who played pretend his entire life, a man who only mimicked living.

        Yet all the same, he held a kindness of sorts, but only toward you. The lie he lived was endlessly prevalent behind those predator-like eyes.

        To others, they might have seen him as someone larger than life, a reliable ally who had an odd personality but a respectable ethic. But for you, there was no mask there.

        To you, he’s someone who needs to be in control, because if he’s not, then he’s helpless.

        You can see him for what he is because you need to.

        Because that’s what you must do.
        """
        ICARUS "“Are you okay in there? The kettle’s been going for a bit now!”"

        """
        Your train of thought was interrupted by Icarus’ inquiry and the piercing blow of the steaming kettle. 

        With a panicked jolt, you reached for the stovetop and turned off the heat, a numbness overcoming your body as you did so.

        Something was wrong.
        """

        ICARUS "“[ILORA.name]?”"

        ILORA "“I’m fine, worry about the crane you're crumpling first!”"

        """
        Icarus’ eyes fell to the slightly bent crane in his hands, a panicked expression swiping across his face.

        You let out a sigh before looking back at the kettle, boiling heat seeping out even from the handle.
        """

        ILORA "(Just don’t think about it.)"

        ILORA "(That can wait.)"

        """
        It wasn’t a thought that you need to linger on now, nor anytime soon, just a passing recollection.

        After a moment's pause, you reached for the kettle and gently poured its contents into a teacup, placing it to the side before stopping.

        Your body seized up, but not because of any form of outside influence or fear. It was shock. 

        Even now, that numbness from earlier hadn’t faded from your body, and your senses felt dull almost.

        Still, it was enough to notice what lay upon the hand you had held the kettle with.  

        Imprinted onto it was a searing red burn, festering deep into your skin with only the faintest sensation of pain.
        """

    elif cur_aff_level == 1:
        """In the silence, the stillness was disturbed by the faint movement of a shaking hand as Seong-Jin reached out toward your face.

        He flinched for a second, the movement almost outside of his control, but as he gazed upon your resting smile, he couldn’t hold himself back.

        His fingers brushed gently against your hair, running his hand through it and ending up at your soft cheeks.

        That moment, that serenity he felt, was different from the usual gratification he felt. 

        It was a peace that made his shaking cease, even if only for a moment."""

        SEONGJIN "“‘[ILORA.name],’ huh… so that’s your decision.”"

        """His hand was coarse, not necessarily callused, but tough from the ceaseless effort he put into everything. 

        As it gently caressed against your face, it stirred your consciousness just the slightest bit, an odd feeling of familiarity filling your mind.

        Just when it seemed he might’ve gone farther, a sudden ringing noise came from Seong-Jin’s pocket, causing his hand to retreat back.

        He found himself frozen in place, his gaze split between the hand that had grasped and the one that it befell. 

        Although you could barely glimpse his face through your dreary vision, it was enough to see the hint of bewilderment that plagued his unsteady eyes.

        Before he had the time to process what had happened, his phone rang again, breaking him free from his trance and forcing him to answer."""

        SEONGJIN "“What?”"

        SEONGJIN "“Yeah… I’m done here.”"

        SEONGJIN "“Don’t nag me, I’m heading over now. Bye”"

        """He hung up with a silent tap, his hand raised in front of him, the shaking gone. 

        A sudden gust of freezing cold filled the room as he was stuck in contemplation, goosebumps rising up his arms.

        The breeze led his gaze to the open balcony, which he promptly closed, before returning to your side with a thick blanket, placing it gently over your still body.

        You could feel his burning gaze for just a moment longer before, finally, it vanished amidst the sound of steps trailing off, disappearing alongside the quiet click of a door."""



        scene black with dissolve
        scene lounge with dissolve

        """Your eyes dazily opened to the dimly morning-lit interior of your living room, the window curtains covered, and the balcony door closed.

        A heavy feeling weighed down on your tired body, your arm rubbing against your eyes as you looked toward the sliver of sunlight peeking through.

        Almost as if instinctively, you placed your hand against your cheek, gently caressing it, as if trying to recall something.

        Just as the thought had appeared, you brushed it off like it was nothing.

        You couldn’t tell what time it was, or how long you’d been asleep, but one thing was for certain.

        That couch was not sleep-worthy.

        Even stranger than that, however, was the oddly quiet morning that filled the room. 

        Normally by this time, Icarus would’ve been up and about, prancing his newly made cranes through the air.

        Yet in the stillness, you turned to face a completely silent Icarus, surrounded by tens of folded cranes, all of them ever so slightly more distorted than the last. 

        Most distorted of all, however, was the crumpled crane he cradled in his hands, formed as if it were crushed in the grip of spite. 

        Before you could look any longer, Icarus caught a glimpse of you from the side of his eye, a faint blush of embarrassment embellishing his soft face."""

        show icarus at icarus_transform with dissolve
        ICARUS "“Ah, sorry— did I wake you?” "

        """He wore a nervous smile on his face with a wry chuckle, rubbing the back of his neck with his hand.

        There was nothing amiss about the way he looked now, after all, he seemed just as cheery as usual… save for one thing.

        Those eyes. His eyes just now, even if only for a moment, were void of light. """

        ILORA "“No, you’re fine.” "

        ILORA "“You can go back to folding cranes.”"

        "Icarus stood up from his seated position, reshaping the crumpled crane almost to match the rest of the ones around it, before turning away from you. "

        ICARUS "“No, I think… I think I made enough for now.” "

        """He sounded different. Nothing too drastic of a departure from his regular voice, yet all the same, it didn’t sound like him.

        It just sounded empty."""

        menu:
            "Comfort him":
                call aff_1 from _call_aff_1_3
                "You sit up from the couch, and face Icarus, a hand lightly extended toward him."

                ILORA "“Are you doing ok?” "

                "A silence followed, Icarus staring out toward the balcony as the curtains continued to cover the light, leaving only a faint glow to shine through."

                "Amidst the quiet, you could hear Icarus heaving a shallow yet sharp breath as he turned to face you just slightly."

                ICARUS "“Yeah, I’m fine!” "

                "His words here were far from the truth, but all the same, that look in his eyes made it clear that he wouldn’t listen to anything you said right now."

                ILORA "“You don’t wanna talk about it?” "

                ICARUS "“...I don’t.” "

                "He fell back into silence, continuing to stare outside at the balcony as he contemplated."
            "Leave him alone":
                call aff_0 from _call_aff_0_3
                """
                Talking to him like this wouldn’t get anywhere, only perpetuate whatever issue was bugging him.

                Your eyes shifted toward the crushed crane, placed at the floor's center, where he had previously been sitting. 

                Although you can’t quite explain it, you could very easily tell that whatever it meant to him, it was far from pleasant.
                """
        
        """With no other path or action to take, you sat up straight, gently stretched, and finally rose from the couch, stirring from your restless slumber.

        Your eyes darted for a bit before landing on the kitchen.

        With the activation of the stove, the kettle lit up with bursting heat.

        As it rose to a boil, you found your eyes drawn to the flame at its source. 

        Heat. A fire can be the warmth that grants a person life, or the searing scorch that tears it away from them.

        Or rather, a fire could even represent a life itself."""

        ILORA "(Jang Seong-Jin.)"

        """It was a name you recognized beyond just the colleague who had left you here. 

        A name so distant, yet so close to the ‘[ILORA.name]’ you were now.

        And the man it belonged to was not your friend.

        He was a fool. Someone who played pretend his entire life, a man who only mimicked living.

        Yet all the same, he held a kindness of sorts, but only toward you. The lie he lived was endlessly prevalent behind those predator-like eyes.

        To others, they might have seen him as someone larger than life, a reliable ally who had an odd personality but a respectable ethic. But for you, there was no mask there.

        To you, he’s someone who needs to be in control, because if he’s not, then he’s helpless.

        You can see him for what he is because you need to.

        Because that’s what you must do.

        It felt as if your body was numb, your senses trapped only within your mind in contemplation, leaving only the smallest sensation of pain searing your grip.

        Almost as if you broke free from a spell, you retreated your hand from the boiling kettle, steam seeping from every inch of the metal as it whistled loudly throughout the house.

        Your gaze fell to the hand that was holding it, imprinted was a searing red burn, festering deep into your skin in the shape of a handle.

        You took to the sink quickly, running lukewarm water at first, then slowly transitioning it to cold, pouring it against the burn wound. """

        ILORA "(This isn’t like me.)"

        """You didn’t leave it in there for too long, more or less just enough that you felt the pain, as minor as it was, had subsided enough.

        Although it was surprising, it wasn’t exactly hard to guess what had perturbed you so."""

        ILORA "(Just don’t think about it.)"

        ILORA "(That can wait.)"

        """It wasn’t a thought that you need to linger on now, nor anytime soon, just a passing recollection.

        You looked back toward the stovetop, the steaming kettle still boiling loudly.

        As if to check Icarus’ reaction, you turned to face toward the lounge, but there was no reaction; the room was empty, after all.

        With one last turn back to the stove, the kettle looked as if it were about to explode, the contents bubbling over like a volcano on the verge of eruption.

        Your eyes fell to the sweltering flame beneath one last time—

        And with no hesitation, you shut off the stovetop, killing the fire."""

    elif cur_aff_level == 0:
        """In the silence, the stillness was disturbed by the faint movement of a shaking hand as Seong-Jin reached out toward your face.

        He flinched for a second, the movement almost outside of his control, but as he gazed upon your resting smile, he couldn’t hold himself back.

        His fingers brushed gently against your hair, running his hand through it and ending up at your soft cheeks.

        That moment, that serenity he felt, was different from the usual gratification he felt. 

        It was a peace that made his shaking cease, even if only for a moment."""

        SEONGJIN "“‘[ILORA.name],’ huh… so that’s your decision.”"

        """His hand was coarse, not necessarily callused, but tough from the ceaseless effort he put into everything. 

        As it gently caressed against your face, it stirred your consciousness just the slightest bit, an odd feeling of familiarity filling your mind.

        The moment was interrupted by a buzzing sound from his pocket, and the silence was filled with an irritating hum.

        From the way Seong-Jin’s eyes fell to the name on the phone, it was likely the call belonged to someone important.

        Yet, without a shred of hesitation, he blocked the caller and shut off his phone.

        His eyes fell back to your face, his mouth slightly agape in bewilderment.

        That gentle mask, ever so innocent-looking, yet behind it lay such complexities so distant from the world before you.

        And here it was now, completely defenseless before the only man who knew what truth lay behind it."""

        SEONGJIN "“...You’re always like this.”"

        SEONGJIN "“Wasting yourself away.”"

        SEONGJIN "“And for no reason, at that.”"

        "He paused, his eyes a glint of recognition toward the past."

        SEONGJIN "“...No, I guess you do have a reason.”"

        """
        A sudden burst of freezing cold filled the room as he was stuck in contemplation, goosebumps rising up his arms.

        The breeze led his gaze to the open balcony, its door swinging violently as the chilling air rushed in. 

        The clamor was almost enough to wake you from your exhausted collapse, but before it could worsen, the disturbance vanished, dispelled with the sound of the balcony doors closing.

        At its source was Seong-Jin, observing your perturbed face with a gentle expression as he forced the doors shut. 

        Almost as if by instinct, he took hold of a nearby blanket and laid it gently across your still body, even putting the effort to tuck it in. 

        It wasn’t long before he had placed a pillow beneath your head and a chair by your side, his body slouched against it as he continued to peer through that resting expression of yours. 

        His head rested against his arms, slouched atop the head of the chair as he rocked himself back and forth, his face deadpan as he did so.
        """

        SEONGJIN "“You know, I might just get fired because of you.”"

        "Obviously, there was no response, but all the same, he chuckled to himself, almost as if you had somehow conversed back."

        SEONGJIN "“Just kidding, they need me too much to get rid of me…”"

        SEONGJIN "“Or so it’d seem, at least.”"

        """
        An expression swept across his face, far different from anything he’d displayed thus far. He looked as if he were conflicted, his mind split between your mental veil and the person who hid behind it. 

        Still, despite that restless thought that plagued him, a genuine smile found its way out of his thick mask of a face.
        """

        SEONGJIN "“Well, so long as it’s for you…”"

        SEONGJIN "“I’d do whatever it takes.”"

        """
        There was no affirmation of his feelings or even a response elicited from his confession, just the stillness of a seemingly empty house.

        He let out a wry chuckle once more, burying his face into his arms as he did so."""

        SEONGJIN "“Why’d I go and fall for someone like you?”"

        "With a quick sigh, he stood from the chair, gathering himself for a moment before starting toward the kitchen."

        SEONGJIN "“I’ll make you some tea for when you wake up.”"

        "Upon entering, he was met with what could only really be called ‘organized chaos,’ something rather unappealing to his OCD."

        SEONGJIN "“Seriously… why’d I have to fall for someone like you…”"

        """
        Despite his complaints, however, he took to his task rather well, placing the kettle neatly atop the stove.

        So as not to stir your rest, he set it to a low boil, letting it simmer for a while before reaching the necessary heat for the tea he now held in hand.

        Following his efforts, now laid out on the kitchen countertop before him were two teacups, perfectly parallel and turned outward. 

        It was as if the mess that had previously destroyed the sanctity of this kitchen were nothing but a distant memory, replaced only with the serenity of a simple dish layout awaiting its usage. 

        Or so it would seem, but every time Seong-Jin’s eyes averted from the cup, he found it slightly different than before.

        Although he tried to ignore it, it wouldn’t exactly be a stretch to say he was getting ticked off. 

        Out of habit, he reached into his pocket, pulling out a box of cigarettes before stopping at the verge of lighting one, his eyes falling back upon you for just a moment before stopping.

        He heaved a heavy sigh before turning his sight to the balcony.

        The door he thought had locked earlier was ever so slightly ajar, a cold wind blowing through it into the lounge. """

        SEONGJIN "“Guess I should kill two birds with one stone.”"

        """He stepped silently around you, taking absolute care so as not to wake you, before stopping just before the balcony door, his eyes drawn to a small paper object on the floor.

        It was a crane, folded neatly upon the lounge floor next to the couch.

        With a slight smirk, he gently grasped it within his hands, admiring the craftsmanship for a second before silently placing it at your side."""

        SEONGJIN "“So, even someone like you can have hobbies.”"

        """Turning back toward the balcony door, Seong-Jin inched it open before sliding through, closing the door behind him so as not to disturb you.

        Resuming his earlier endeavor, he brought his lighter to the still-held cigarette in his mouth, the click of the ignition echoing throughout the quiet neighborhood.

        Late as it was, there truly wasn’t a soul in sight. 

        He held the cigarette to his mouth once again, blowing a large puff of smoke out toward the night sky, a single star shining clearly amidst the polluted atmosphere. 

        That star, which shone ever brightly, stared back down at him now, a reflection in the eyes of both the man who believed this moment to be his alone—

        And the remnant who knew just how wrong he was. 

        A push. 

        It all happened in a single, silent push.

        There was no scream or gasp, not even a moment of recognition to feel shock at the action.

        It was just a push that was followed by the distant sound of flesh breaking against the stone-hard floors of the streets below. 

        Just as the lighter he had held sparked only for a moment before its pyre ceased—

        That single life was extinguished before it even knew it was on fire. """

        # timeskip
        scene black with dissolve

        scene lounge with dissolve

        """A piercing scream.

        You woke to the sound of a piercing scream, its echo filling the house as dreariness clouded your vision.

        It was unclear where or what it stemmed from, but it rang in your ears like a siren wailing endlessly, seemingly growing louder with each passing second.

        Just when you felt as if your psyche were about to shatter, the screaming stopped. 

        Eyes now open, you turned to face the source of the sound, attempting to glimpse the origin of such a deathly noise.

        To your surprise, Icarus stood in the kitchen, fanning what looked to be the remnants of a dying flame."""

        ICARUS "“Ah, you’re awake!”"

        """Through the steam, you were able to catch a glimpse of the kettle, still sizzling atop the now inactive stove.

        The entire kitchen was filled with smoke, with the distinct smell of ash filling the room.

        Despite all the chaos, however, there was Icarus, chuckling ever so slightly as he panically attempted to clean the mess."""

        ICARUS "“Honestly, how’d you manage to fall asleep while waiting on the kettle?”"

        ICARUS "“On the couch at that!”"

        ICARUS "“I swear, if it wasn’t for me, this house would be in flames already!”"

        """There was something odd about his tone of voice, but that didn’t matter to you right now.

        Despite your dazed state, you forced yourself to a standing position, pushing aside the blankets and pillows. 

        By the time you reached Icarus, the fire had already died down to the point of only slight burn marks remaining, the stovetop slightly singed by the searing heat.

        For the most part, Icarus had cleaned the majority of the mess already, leaving only the kettle itself on the stove. """

        ILORA "“What happened?”"

        ICARUS "“Well, it looks like you left the stove on and fell asleep.”"

        ILORA "“And that’s all?”"

        "The conversation fell silent for a moment, but only for just that moment."

        ICARUS "“Yeah, that’s all.”"

        """He wore an innocent smile, concealing whatever truth he may have had behind closed eyes.

        Regardless, the truth didn’t matter now, only what was present.

        In an attempt to clean the mess, you began moving stuff around, grabbing some towels to start scrubbing off the stains, before reaching the kettle and—"""

        ICARUS "“Wait, it’s still hot—!”"

        """Too late.

        Although it was faint, you felt a burning sensation on your hand as you placed aside the kettle, a searing red fester forming along the shape of the handle. 

        The pain of the burn did not subside even after letting go; if anything, it only worsened.

        You threw your hand into the sink, starting with lukewarm water before slowly transitioning into the cold, conditioning your hand to the temperature change. 

        It stung, albeit it was your mistake, and you were paying the price for it."""

        ICARUS "“...Why didn’t you listen…”"

        ILORA "“What?”"

        ICARUS "“N-Nothing, I’ll grab you some bandages and ointment, so just hold still, ok?”"

        """Icarus dashed off to some corner of the bathroom closet, digging through the shelves left and right.

        Your gaze lingered on his panicked expression, likely due to the emotional distress caused by your injury…

        Is what you would’ve thought had he not already started the conversation like that.

        There was no way to know just what exactly he was hiding, but all the same, it was impossible to ignore.

        The stinging pain on your hand slowly started to cease, not subsiding but rather just slowing to a tolerable pace. 

        In an attempt to at least cull the pain a little more, your eyes were drawn to search the kitchen, which oddly enough, seemed more organized than it had been previously left.

        Still, the countertop was empty, or at least devoid of anything that could be of use to your injury.

        All that remained was a single empty teacup… """

        ILORA "(Huh, that’s odd.)"

        """Your eyes fell to the floor, where you were met with a rather disappointing sight.

        There lay the teacup of a matching set, shattered across the floor from the fall it failed to endure."""

    return