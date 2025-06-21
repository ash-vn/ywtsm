label meet_cute:
    menu:
        "You realize now, the person behind that curtain has no shadow. However, you can see the distorted yet identifiable paper crane's shadow. Peering more closely, you also notice the person, if they can be called that, is holding the design."
        "You ‘saw nothing’.":
            """
            You know what? You're not in the mood to deal with any intruders.

            There are other ways to get rid of your problems, and though ignoring them is usually pointed out as a bad way to deal with, that's exactly what you'll do now. 

            You don't want to be irresponsible, but the day just started and you'd rather keep your sanity and lifestyle goals intact.

            You go back to your original task, focusing on putting all your clothes into your closet, and soon enough the shadows of midday sun begin showing. Possibly out of curiosity, or dread, you glance back at the window where the stranger was.

            They changed their hiding spot.
            """
            $ blue += 1

        "Take them down.":
            """
            Calmly, you go open a particular box to find a particular item as well. 

            After some searching, you finally catch a glimpse of silver in the dark. You grab the thin but effective blade by the handle and make your way back to the window where the criminal hides.

            But the silhouette is gone.
            """
            ILORA "…"

            ILORA "Hey!"

            ILORA "I know you're hiding somewhere!"

            ILORA "It's in your best interest to show yourself now."

            "…"

            ILORA "Fine."

            """
            Of course it's alright. You don't need to escalate things, and you weren't really eager to do so.

            Self-defense. That's all. And you're safe.

            They're gone… apparently.
            """
            $ purple += 1

        "Call them out.":
            ILORA "Hello?"

            "And behind a thin curtain that you could slice in two with a kitchen knife if you were impetus."

            ILORA "Playing deaf?"

            """
            A light chuckle is your only answer.

            That was… rather innocent. Sounded young and harmless, actually.

            You’re deeply aware that appearances can deceive, but maybe this isn't so dangerous.

            Maybe there's a boy messing about outside?

            You don't know what kind of game this is, so you go back to organizing your clothes.

            For now, you'll let this stranger be.
            """
            $ orange += 1