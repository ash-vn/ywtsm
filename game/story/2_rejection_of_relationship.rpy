label rejection_of_relationship:
    scene door with dissolve
    """
    Your skin still crawls, but your rational brain latches onto one thought like a safety railing: ghost. 

    If they exist, they shouldn’t be able to touch you. To hurt you. That’s the rule, isn’t it? You’re safe.

    Probably. 
    You turn away, pulse still in your throat, and do what anyone does when reality gets a little wrinkled around the edges:
    You pretend it never happened. 
    """
    if not points['blue']:
        """
        And — for good measure — you clarify that.
        
        Just in case any local entities are feeling self-conscious.
        """

        ILORA "I wasn’t talking to the curtain, by the way. I was talking to myself."

        ILORA "As you do. Alone. In new apartments."

    
    play music "assets/audio/music/bgm.mp3" volume 1.0 fadeout 0.2
    """
    Anyways, back to renovating.

    You drag over the sad metal stepstool from the corner. It wobbles slightly, legs uneven from years of abuse by previous tenants, but it’ll do.
    """

    ILORA "Okay, buddy. Just you, me, and your one job: not collapsing."

    """
    You reach toward the ceiling light and unscrew the old bulb, motion smooth and practiced. The new one waits in your palm, cool against your skin.

    You screw it in. Done.
    """
    ILORA "(Maybe this place won’t kill me after all.)"

    """
    You start your way back down.
    One foot. Then—
    The edge of your sock slides against the metal step, and your balance slips. 

    Before you can gasp, gravity yanks you backwards into a sharp, short tumble. 
    """

    scene black with dissolve
    with hpunch
    pause(0.5)
    
    """
    But then you land into something warm and…soft? 
    """

    scene door with dissolve
    show i closer startle idle at center with dissolve:
        yalign 0.3 zoom 2
    "You blink and look down to see him, crouched below you, palms up, like he knew exactly where you’d fall.
    His eyes are wide and startled. Almost guilty, like a puppy caught mid-miracle."
    show i thinking
    "???" "!!!{w=1.5}...Hi."
    
    "What the hell…?"
    show i startle_ farther
    
    ILORA "AAAAAAAAAAAAAAAA!" 
    show i surprise 
    scene black with dissolve
    with hpunch
    pause(0.5)
        
    show i surprise_ startle idle at center with dissolve:
        yalign 0.3 zoom 3    
    with hpunch
    "???" "AAAAAAAAAAAAAAAA!" 
    with vpunch
    with hpunch
    "You recoil. He jumps."
    with flash
    show i surprise idle surprise_ at center:
        yalign 0.3 zoom 3
    "In your quick stumble back, you trip and fall flat on your face."
    scene door with dissolve
    with hpunch
    pause(0.5)
    # $ renpy.transition(hpunch, layer="screens")
    with vpunch

    ILORA "...Ugh."

    """By the time you get back on your feet, he’s gone again, the curtain swaying gently in his wake. 

    You rub your sore ankle, the warmth of his hand still tingling. 

    {i}He can touch things. He can touch you.{/i}

    But he didn’t harm. Just disappeared like a nervous kid, without even an explanation."""

    menu:
        "“Hey! What the hell was that?”":
            $ points['blue'] += 1
            "You point toward the curtain, heart still racing."
            ILORA "You caught me. What even are you?"
        "Say nothing.":
            $ points['purple'] += 1
            "You dust yourself off, avoid looking at the curtain, and say nothing. If anyone asks later, you tripped. That’s all."
        "“...Thanks. For catching me.”":
            $ points['orange'] += 1
            "Your voice is quiet, just enough to carry."
            ILORA "I’m not sure what would’ve happened otherwise. So, thank you."

    """        
    The curtain shifts a couple of times. 
    
    Then, slowly, cautiously he peeks out and steps into the light. 
    """

    show i thinking idle at center with dissolve

    "There is no shadow behind him, but he clearly looks human."
    show i worry
    "???" "Sorry, I didn’t mean to startle you…"
    show i thinking
    "???" "I just didn’t want you to get hurt."

    "You stare at him. Not with fear, necessarily, but with questions."

    ILORA "You’re a ghost."
    show i serious
    ILORA "Ghosts aren’t supposed to be able to touch people."

    "He shifts a little, uneasy."
    show i thinking_
    "???" "Yeah, well I sometimes can’t."
    "???" "Sometimes I try to hold things and it just goes through."

    "???" "But other times… it works. And I don’t know why."
    
    ILORA "So it’s like a glitch."
    show i thinking giggle_ thinking_ 
    "He frowns, but then brightens awkwardly."
    show i happy
    "???" "Well, at least I caught you. I guess I’m a good glitch?" 

    "You don’t answer right away, crossing your arms instead."

    ILORA "Let’s get something straight."
    show i serious
    ILORA "As much as I appreciate the catch, it’s not proper to touch other people without consent."
    show i -thinking_ shy_
    "???" "Yes! Totally fair. I—yes. Got it."
    show i thinking_
    """
    His fingers begin to fidget with the paper crane again, now slightly crumpled from the nervous squeezing. 

    He tries to smooth it out and fails.

    He pouts with a face that really shouldn’t be allowed to belong to a supernatural entity.
    """
    ILORA "(It’s not fair to look that cute while technically haunting someone.)"
    show i shy
    "???" "So. Umm."
    show i -thinking_ content_
    "???" "I guess this is the part where I say hi, again."
    show i light idle -shy giggle 
    ICARUS "My name…what was it again…Oh! Icarus! Everybody calls me that."
    show i happy -giggle -shy
    pause(0.5)
    scene white with dissolve
    with fadehold