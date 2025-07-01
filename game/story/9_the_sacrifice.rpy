label end03:
    """You open your mouth, then close it again.

    You sigh.""" 
    ILORA "“This is ridiculous.”"

    ILORA "“I’ve already fallen this hard. What’s the point of pretending I’m okay with you leaving?”"

    "You cross your arms, glance at the window, the cranes, anywhere but his face."

    ILORA "“I don’t want you to move on. I want you to stay.”"

    "The paper crane in his hands trembles slightly, as if it heard you."

    "ICARUS “You want me to… stay? You… truly mean that…?”"

    "You silently nod. "

    show i giggle light idle with dissolve
    "He crosses the space between you in two strides and throws his arms around you, burying his face in your shoulder."

    ICARUS "“I’ll stay! {w}I’ll stay as long as you’ll have me.”"

    "You let out a breath, slow and shaky. And for the first time in days, you give a bright smile."

    """His hair tickles your cheek. His grip is warm—not in temperature, but in presence. 

    Finally, you don’t feel alone anymore.""" 

    ILORA "“Good. Because I wasn’t ready to say goodbye.”"

    """You wrap your arms around him in return. His shoulders relax, and for a second, the world feels very, very still.

    From across the room, the fish bowl burbles with the tiniest plop. You both glance over."""

    if fish_count == 1:
        "[fish_name] has turned his little translucent back toward you, floating dutifully behind the castle ornament as if observing a strict privacy policy."

        ICARUS "“Haha..! Do you think he knows?”"

        ILORA "“Fish instincts can be quite sharp sometimes.”"

        "And in the soft glow of that moment, with paper cranes nesting on the table and [fish_name] continuing his tactful ignoring, it becomes perfectly clear—"
    elif fish_count == 2:
        "The fish have turned their little translucent backs toward you, floating dutifully behind the castle ornament as if observing a strict privacy policy."

        ICARUS "“Haha..! Do you think they know?”"

        ILORA "“Fish instincts can be quite sharp sometimes.”"

        "And in the soft glow of that moment, with paper cranes nesting on the table and fish continuing their tactful ignoring, it becomes perfectly clear—"
    elif not fish_count:
        "And in the soft glow of that moment, with paper cranes nesting on the table, it becomes perfectly clear—"

    """He’s not just someone who stayed.

    He’s someone you chose."""

    call gut_ending from _call_gut_ending
    call ending('03') from _call_ending_9

label end04:
    "You shift, knees brushing his, and your voice comes out quiet."

    ILORA "“…I love you.”"
    "His eyes widen. You can tell his thoughts are stuttering. "
    "You reach forward and nudge aside the folded paper cranes that sit between you—little messengers of unspoken longing—and make a small space just for you."
    "And him. "
    "Your hand hovers beside his, not touching yet."
    ILORA "“I know you’d stay if I asked.”"
    ILORA "“And I know I’ve been keeping a wall up this whole time. But…”"
    "You take a breath. Then two. Then finally look him in the eye."
    ILORA "“I want you to stay. Not because you're a ghost I’m trying to help move on.”"
    ILORA "“But because I want you here. {w}Because I love you.”"
    show i giggle light idle with dissolve
    "Icarus reaches out and delicately takes your hand, as if afraid this moment would break."
    ICARUS "“Even after everything?”"
    "You nod, your eyes stinging."
    ILORA "“Even so.”"
    "He lets out a breath he didn’t realize he was holding and laughs full of relief."
    ICARUS "“I can’t believe you just cleared space for me like this.” "
    ILORA "“Better late than never.”"
    ICARUS "“For the record, I… love you too.” "
    ICARUS "“But I’m sure you already knew a long time ago.” "
    "You lean in."
    "He leans back."
    "The cranes around you rustle like they’re smiling too."
    call gut_ending from _call_gut_ending_1
    call ending('04') from _call_ending_10

label end05:
    "You tilt your head, lips quirking upward as your voice drops into something playful."

    ILORA "“…You know, sometimes when I come home… and you pop out of nowhere—like, poof—there’s this one phrase that always plays in my head.”"

    "He raises an eyebrow, a little wary, a little curious."

    ICARUS "“Oh? Something like: ‘get out of my apartment’?”"

    ILORA "“No.”"

    ILORA "“‘Welcome home, honey.’”"

    "He freezes."

    "You let it hang there, air heavy but sweet between you." 

    ILORA "“It’s cheesy, right? But you feel warm and familiar. Just like how I imagine home to be.”"
    "His mouth opens. No words come out." 
    "You shrug, trying not to show how much that confession cost you."
    ICARUS "“[ILORA.name]…”"
    show i giggle light idle with dissolve
    "He puts the crane down—gently, with both hands. Then he shuffles forward on his knees and wraps his arms around you. "
    "You melt into it, curling slightly into his warmth, cheek pressed into his shoulder."
    ICARUS "“Welcome home, honey.”"
    "You laugh. You don’t mean to—but it bubbles up, sweet and giddy."
    ILORA "“That was fast.”"
    ICARUS "“You didn’t say there had to be a delay.”"
    ILORA "“Someone’s committed.”"
    ICARUS "“I plan on overusing that term now.”"
    "You press your forehead against his and close your eyes." 
    "More than anything, you feel peaceful. Like staying isn’t a question anymore—{w}it’s the answer."

    call gut_ending from _call_gut_ending_2
    call ending('05') from _call_ending_11

label gut_ending:
    "His eyes seem soaked in astonishment, yet you’re no longer sure that’s the reason why they’re glossy. His tight, surprised smile melts into a soft grin. {w}If you’re honest, your heart might be melting too as he looks back into your eyes."

    ICARUS "“[ILORA.name], I…”"

    "His hand twitches. Does he want to take yours?"

    ICARUS "“Your wish is the same as mine.”"

    ILORA "“It– It is?”"

    "Goodness you’re not one to stutter! Does he truly affect you so badly?"

    ICARUS "“Of course! Always.”"

    ICARUS "“And, and you won’t change your mind, will you?”"

    ILORA "“I wi–”"

    ILORA "“Wait, no. I, in fact, don't wish my wish was different.”"
    show i giggle light idle with dissolve
    "You smile as he doesn’t roll his eyes at you even though he could have."

    ILORA "“So, what’s next–? Whoa!”"

    "Before you realize it you find yourself wrapped between Icarus' long arms, the cotton of his clothing soft against your cheek as you rest your head against his chest. You both tumbled down, but he made sure to take the hit for you."

    ILORA "“Icarus?”"

    ICARUS "“Hmm?”"

    ILORA "“You’re crushing me.”"

    ICARUS "“OH! Sorry–!”"

    ILORA "“Please, don’t!”"

    "Before he lets you go, you hug him back, for a moment even tighter than he did just to make sure he doesn’t leave."

    ILORA "“Just… Stay.”"

    ICARUS "“Didn’t we agree on that already?”"

    ILORA "“You know what I mean!”"

    "You caress his hair dearly and he snuggles against your cheek as if he were an adoring pup. You laugh and, hearing you, so does he."

    ICARUS "“I’ll stay forever.”"
