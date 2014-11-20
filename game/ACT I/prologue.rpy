label prologue:
    call prologue_name
    call prologue_lab
    return
label prologue_name:
    $ player_name = renpy.input("What is your name?", pixel_width=300)
    $ player_name = player_name.strip()
    if player_name == '':
        $ player_name = "Chungus"
    menu:
        "So you are [player_name]-dono?"
        "Yes":
            pass
        "No":
            jump prologue_name
    return
label prologue_lab:
    plh "Show the facility where the protagonist works"
    plh "Show people in isolation suits, moving in each frame while the camera stays steady"
    plh "The camera switches to a secure room that could be seen previously in the distance"
    plh "The protagonist comes through the airlock, musing about how good it feels to be doing such important work"
    plh "It is revealed that while he is working for an institute seeking to control deadly pathogens, part of this involves the expectation that they may evolve into more deadly, more transmissible, or more survivable forms."
    plh "He is the one driving this evolution in the laboratory, and testing the results on animals."
    # Use rats to be generic, pigs to be plausible, or primates to be unnerving.
    plh "He gets bitten, but there appears to be no damage to the isolation suit and work continues, including work on a mutated Ebola."
    plh "His day ends, and he finishes logging his journal entries so the night staff can watch over the animals he infected, as they may sicken and die overnight, in which case they are to be quick-frozen for necropsy the next day."
    plh "He drives home, unable to find a temperature setting that suits him - they're all either a little too cold or a little too warm."
    plh "When he gets home, he finds Ebola-chan (without a skull) sitting on his couch as if she was waiting for him, with his TV remote in her hand and a bag of chips (crisps) on the table."
    ebby "It's about time, I was starting to think you'd never get here."
    plh "This is when he realizes that he must have contracted the virus through the bite earlier in the day, and starts to feel seriously ill."
    plh "He is dead within minutes, his head being cradled in the lap of a grief-stricken Ebola-chan, who keeps repeating that she \"only wanted to play\"."
    return
