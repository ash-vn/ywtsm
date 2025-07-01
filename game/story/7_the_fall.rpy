label the_fall:
    """
    The world feels muffled today, wrapped in a dark fog and the unceasing patter of rain. 

    You sit cross-legged with Icarus on the floor, paper-cranes surrounding the both of you. 

    In his hand, the final one. 

    A white crane, folded clean. 

    He turns it between his fingers with a strange gentleness, like if he’s too direct, it’ll vanish.
    """

    ICARUS "“One thousand.”"

    ILORA "“You remember what I asked the first time you told me about this?”"

    "He nods silently. "

    ILORA "“What’s your wish, Icarus?”"

    "He doesn’t answer immediately. His gaze drops again to the crane."

    ICARUS "“I used to say it was to move on.”"

    ICARUS "“I thought... if I could finish this, something would finally click. And it would all make sense.”"

    ICARUS "“But now, I don’t know what I’m supposed to want…”"

    "He looks at you again, this time without a smile. However, there’s a soft openness to his eyes. "

    ICARUS "“Do you have any thoughts?”"
    
    menu:
        "“I wish you can move on.”":
            if low_affinity:
                ILORA "“I think it’s time.”"

                ILORA "“You’ve done what you came here to do.”"

                ILORA "“You deserve to go.”"

                "There is a moment of silence. The crane crinkles a little in Icarus’ grip. "

                ICARUS "“Even if I don’t want to?”"

                ILORA "“Even then.”"

                ICARUS "“In that case, I hope…I do.” "

                "He stares down at the crane again. "

                "Then, he places it on the table, quietly completing the circle. "
                
                if player_color == 'blue':
                    jump end06
                elif player_color == 'purple':
                    jump end07
                elif player_color == 'orange':
                    jump end08
            elif high_affinity:
                ILORA "“I think…it’s time.”"

                ILORA "“You’ve done what you came here to do.”"

                ILORA "“You’ve earned the chance to go.”"

                "The words don’t come easy. They never would." 

                "Icarus clutches the final crane a little too tightly, paper rustling."

                ICARUS "“Even if I don’t want to?”"

                "You don’t answer immediately. "

                "You look at him — really look at him. The cute and clingy ghost who accompanied you day and night. Who always listened and lingered, when no one else did."

                # WHISPER
                ILORA "{size=20}{color=#99B}{cps=*0.2}“{i}Yes, even then.{/i}”" 

                "His eyes redden without crying. Although now would certainly seem like an appropriate time to do so. "

                ICARUS "“In that case…I hope I do.”"

                "He looks down at the white crane — holds it for one long second more — and sets it gently down."

                if player_color == 'blue':
                    jump end13
                elif player_color == 'purple':
                    jump end14
                elif player_color == 'orange':
                    jump end15
    return

label end06:
    "You look at Icarus."

    "He looks back at you, trembling a bit, as if this is the part where something important is supposed to happen."

    ILORA "“Well. That’s that.” "

    ICARUS "“...That’s what?”"

    ILORA "“One thousand. The wish. You can go now.” "

    "He blinks. "

    ICARUS "“Oh. Right.”"

    "There is a long pause, where you just stare at each other. "

    "Then, without any dramatic flourishes, he just vanishes in a pop. Like a soap bubble. "

    ILORA "(It’s been so long.)"

    ILORA "(I should probably feel more than this. But honestly? I’m just glad I got the room back to myself.)"

    "You search around for a plastic bag to stuff all the cranes in. "

    ILORA "“Seems like I can use these for my air freshener decorations.” "

    # [Cut to ending with a deadpan face 🗿]
    return


label end07:
    ILORA "“Ugh, it hurts. Just because something is inevitable doesn’t mean it hurts any less.” "

    ICARUS "“Are you quoting a K-drama?”"

    ILORA "“No.”"

    "You totally were."

    "Icarus smiles sadly. "

    ICARUS "“You’ll be okay without me?”"

    "You sigh and shake your head, but you give a shoo-ing motion anyways. "

    "He slowly fades." 

    # [SCENE: CUT to Ilora standing alone in the middle of the room]

    "One crane flutters dramatically from the ceiling and lands in your open hands. "

    # [Note: some melo-dramatic sound-track playing. With potentially lots of violin.]

    ILORA "(Every year, on this day, I will light a single candle by the window.)"

    ILORA "(I will wear black.)"

    ILORA "(I will eat exactly one boiled egg in solemn remembrance. {w}I don’t even like eggs.)"

    "A single tear slides down your cheeks. "

    # [Cut to ending where “I MOURN YOU” appears in gothic cursive, with glittering overlay and a looping sad flute sound.]
    return


label end08:
    "You suddenly stand up. "

    ILORA "“Nope. Not like this.”"

    ICARUS "“What?”"

    ILORA "“We’re not ending your haunting career with you sadly folding yourself out of existence.”
"
    ILORA "“If you’re going, we’ll make sure you go out in style.”"

    "You rummage around the drawer for tacks, twine, washi tape, whatever’s on hand. "

    "And then, as if possessed, you begin stringing cranes from the ceiling. "

    ICARUS "“Wow! I didn’t know I warranted a send-off party.”"

    ILORA "“You’ve been squatting in my apartment for a month. You absolutely do.”"

    "He breaks out into one of the brightest grins you’ve ever seen. "

    # [Potential CG cut: the two of you decorating!] 

    "You work together, laughing under strings of cranes. "

    "Icarus floats up to tape absurdly high on the ceiling, while you playfully aim a slipper at him. "

    # [TIME SKIP]

    "Eventually the living room glows, filled with a thousand tiny birds in the air. "

    ICARUS "“I don’t want to forget this.”"

    ILORA "“...Then don’t.”"

    ICARUS "“Can I say something weird?” "

    ILORA "“You usually do.”"

    ICARUS "“I think I’m glad I died here.” "

    "You don’t laugh. You just lean closer, until your shoulder barely touches his. "

    "Outside, the rain softens into a light patter. "

    ICARUS "“Thank you.”"

    "And then, light gathers around him. Cranes start to lift, just barely, as if fluttering into life. "

    "He slowly begins to fade. "

    ICARUS "“You really were my wish.” "

    "And then, just like that, he’s gone. "

    "You remain sitting, surrounded by the cranes still swaying in the aftermath of his presence. "

    ILORA "“...what should i do now? You… really left me with all these cranes.. It’s too much, it might fit a baggage.”"

    return

label end13:
    "He lets out a breath — too light for lungs. Just the idea of one."

    "There’s a faint hum in the room, like a microwave turning on. "

    "You blink, and he’s already halfway transparent."

    ICARUS "“Hey… don’t forget me, okay?”"

    "You open your mouth. But the words get stuck somewhere in your throat."
    "By the time you find them, he’s already gone."
    # [TIME SKIP] 
    "Later, you stand at your desk, holding your notebook. "
    "The one which contained the secret poem you wrote about him. "
    "You remember starting it the first week he showed up and never stopping with the fiddling, sentence by sentence, whenever he was sitting nearby."
    "You always tilted the screen just enough so he couldn’t peek."
    "Now he never will."
    "You fold it up one last time and walk over to... the urn? "
    "You stare at the cool, white surface devoid of labels. "
    ILORA "“...Wait. Where exactly am I supposed to leave this?”"
    "You look around."
    ILORA "“Was I even spelling Icarus right this whole time?”"
    "You crouch down next to it, hug your knees, and sigh."
    return

label end14:
    "Outside, the storm that had been hammering the world just… stops."

    ICARUS "“Huh. Guess even the sky knows when to say goodbye.”"

    "His outline’s already starting to fade, like ink in water."

    ILORA "“You’ll be okay, right?”"

    ICARUS "“Not sure. But I think I’ll find out.”"
    "He looks at you one last time."
    "And then—"
    "He rises. Like a kid in a dream getting pulled upward by too many balloons."

    # add alive fish check
    ICARUS "“Tell the fish I might actually miss him too!”"

    "You squint after him through the now-sunny window as he floats higher, wobbling slightly, arms out."

    ILORA "“Fly safe, Icarus.”"
    "And for once, he does."

    return

label end15:
    "You open your mouth."
    "What you mean to say is {i}Stay{/i}."
    "What comes out is—"

    ILORA "“I think you should move on.”"

    "The words are barely off your tongue before your heart plummets in betrayal."

    "Icarus blinks as his smile wilts. "

    ICARUS "“...Oh.”"

    ILORA "“I mean—{i}technically{/i} that’s true — morally — ethically — spiritually—but also—”"

    "You grip the nearest paper crane for emotional support."

    ILORA "“But, um—if you wanted to maybe... wait a bit?”"

    ILORA "“Just until my time is up too or something. No pressure.”"

    "You laugh quickly, as if you did not just propose a literal lifetime together. "

    "Icarus stares at you, utterly still. Then, slowly, the realization dawns in a bright grin. "

    "He takes your hand in reverence."

    ICARUS "“You… want me to stay?”"

    "You open your mouth but no words come out. You only nod. "

    ICARUS "“I want that too. I really do.”"

    "He grabs you in a full-force hug, sending paper cranes flying everywhere."

    ICARUS "“Until your time is up. Until forever, if you want.”"

    return
