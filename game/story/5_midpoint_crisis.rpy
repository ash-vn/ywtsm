label midpoint_crisis:
    """
    It hasn’t been long enough for the seasons to change, only a month actually. Still, the gentle face of a ghostly presence greeting you every morning has become familiar.

    Dear even, maybe.

    Isn’t it senseless, though? You don’t understand what such care for Icarus means, only that it lies somewhere in your heart. How deep it runs is… debatable. Is there a point to letting yourself grow fonder of him anyhow? Where will this lead you?
    """

    $ high_affinity = (points[player_color] >= 4)
    $ low_affinity = (points[player_color] <= 3)

    menu:
        "Everything must stay as it is.":
            "This is safe, as long as nothing else changes, right?"
            

        "You’re not sure.":
            "This is an unexpected feeling and, since you can’t pinpoint it, full of uncertainty."

            """
            You can’t deal with this.

            You don’t want to deal with this.

            He’s not a bad one, probably, just inconvenient. You didn't buy a near desolate but pretty place to get an extra ghost in the package, so you’re not going to carry the weight of having to share the rest of your life with him. 

            Well, not the rest of your life, that might be a bit dramatic, but to share your space with him for at least the next couple of years. There’s no comfort in living with a… stranger.

            It’s time for him to go.
            """

            if low_affinity:
                if player_color == 'blue':
                    jump end09
                else:
                    jump end10
                
            elif high_affinity:
                "You are comfortable. But you’re unsure of this. You decide to escape."
                if player_color == 'blue':
                    jump end12
                else:
                    jump end11

    return

label end09:
    """It’s a cold evening, cold enough to give you the strength to confront Icarus. 

    On a warmer day you could have grown too soft, you would have postponed delivering the news. You would have bought sweet ice cream and sat under the sun even if it melted your dessert. 

    Now, on the other hand, you hold a cup of sugarless coffee, drink it down and leave it in the sink.

    After finishing lunch, you ask him to come follow you into another room; you bring him to the one where it all started, where you met.

    His eyes shift around the room, visibly anxious. He might know what you’ll say already."""

    ILORA "“Icarus, I am grateful to have had your company for the past days, truly…”"

    "No, in truth, you’d rather not have had him but - oh well, you can still be kind when you wish to be."

    ILORA "“But I didn’t plan to have company, and my patience has worn thin. I’d rather be left alone now so…”"

    "With a determined glance at him, you make your verdict."

    ILORA "“You must leave now!”"

    "Poof!"

    ILORA "“Ugh!”"

    """You step back instinctively, yet he hasn't moved towards you. No, as if he had been no more than mist, he vanishes.

    His light eyes are the last of him you see, staring back at you in disbelief.

    Yay you."""

    call ending('09') from _call_ending

label end10:
    """He sits there, opposite you on the other end of the table.

    You feel like a grumpy middle school teacher, a quiet, muttering teacher. 

    You’re giving a kid detention and sending him off to the principal’s office. 

    After all, you’re getting rid of Icarus just because he breathes… Well, he doesn’t exactly breathe anymore - but to finish the idea, just because he breathes the same air you do. 

    Technically, it’s your right to be able to live alone in your own property, but it doesn’t feel right. """

    ILORA "“I can’t do this…”"

    ICARUS "“Did you say something?”"

    ILORA "“Nothing! Nothing at all.”"

    """He blinks, perplexed, and returns to his making of paper cranes.

    Of course you can’t kick him out. Righteousness or lack of backbone, whichever you’d rather pick, won’t let you ask him to take leave.

    He’s not a vampire, but with how much energy he’ll drain from you he might as well be.

    You continue to let him stay, even if you’re only tolerating him. In the end, isn’t that what life in society is like? 

    No matter what rock you live under, you’ll always be stuck with a guy who’ll never stop filling the silence of the emptiest cave.

    And you’ve got yourself that guy for your own little stone-made place in the world."""

    call ending('10') from _call_ending_1

label end11:
    """You could be frank, maybe a bit rude if you really want to be, and tell Icarus you can’t stand him anymore, to leave and never show his face again so you can restore your peace.

    You could be kind, too soft if his poor gaze makes you regret your choice, and explain your need for solitude to recover from a harsh life.

    You can also let him be, resist the wish of your heart and share your days with him, hoping he’ll leave one day on his own.

    Or you can escape.

    You are an excellent runner in many ways, so running away is the most natural thing you or anyone else would do.

    Just as you unpacked everything the first day you got here, you packed up again. You do so in the dark and by the time daylight touches the first mountain peaks, you’ll be gone.

    You catch a glimpse of him before you lock the door behind you, never to come back again.

    Tears threaten to fall, but you rapidly blink them away, shutting the door.

    Even though you don’t understand why this pains you so much, you know it’s the only way to keep yourself safe."""

    call ending('11') from _call_ending_2

label end12:
    """You’re a schemer, be it by nature or nurture. 

    Smart or that’s what you like to think you are. 

    Regardless of whether that's the case, you carefully reviewed all of your options. There are variants of the same ‘solutions’ and none quite satisfy you. 

    You’d rather not bother asking him to leave or pestering him until he does, nor let him stay.

    That’s why you have another idea.

    You don’t text that much, or maybe you do, but no matter if you have experience first hand with it or heard from somebody else, there’s a certain occurrence that’s common over there: ghosting.

    Everybody does it, you don’t have to feel bad about doing it yourself. You’ve never tried doing it to a person in real life, yet you’re not unwilling to do so.

    Thus, you initiate your plan.

    No drama. 

    No hysterics."""


    ICARUS "“Good morning!”"

    ILORA "“...”"

    ICARUS "“[ILORA.name], can you hear me?”"

    """The next day…

    Another one of Icarus paper cranes lays atop the table while he finishes the one in his hands."""

    ICARUS "“Look, do you think the head’s right?”"

    "You turn your gaze to the windows, to clouds that are swept away by the blowing wind."

    ICARUS "“[ILORA.name], can you see me?”"

    """The next–

    He taps your shoulder.""" 

    ICARUS "“[ILORA.name], can you feel me?”"

    """His hand rests in place, gingerly.


    You simply pretend he doesn’t exist.

    Eventually, his vain attempts at bringing your attention fade. Or rather, he fades. One day, you return home as usual. You expect to hear the faint, manic pleas or the eager ‘welcome’ of a young man.

    You don’t.

    No voice echoes across the rooms of your voice other than yours.

    You wanted this.

    You are alone."""

    call ending('12') from _call_ending_3