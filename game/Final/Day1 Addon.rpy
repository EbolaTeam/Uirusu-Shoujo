label day1_morningFin:
    scene bg black with fade
    scene bg xebdorm_room with fade
    show ebby concerned:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    ug "H-hello? Are you awake?"
    pr "Y-yeah, I think? Where am I? Who are you? How did I get here?"
    show ebby sad
    ug "Daddy told me you're staying with us for a bit and that you'd know what's going on."
    pr "He was a little vauge. Anyway, what's your name?"
    show ebby normal
    ec "Ebby. And yours?"
    pr "I'm having a hard time remembering..."
    show ebby joy
    ec "Heh, that happens to me some times"
    pr "Seriously, what's my name..."
    $ bullshitname = renpy.input("Please enter your name:")
    $ bullshitname = bullshitname.strip()
    pr "I remember, it's %(bullshitname)s"
    show ebby concerned
    ec "Seriously? What a weird name"
    pr "Wait no, that isn't it, obviously. Forgive me, I'm still half asleep."
    show ebby normal
    pr "I'm Chungus. Nice to meet you Ebby."
    show ebby joy
    ec "Well that's a much more normal name. Nice to meet you, Chungus."
    pr "Anyway, what's the time? I'm pretty tired."
    show ebby normal
    ec "Oh, it's 3AM. Sorry for waking you, I coundn't wait to meet you"
    pr "No chance you'd let me go back to sleep?"
    show ebby joy
    ec "No worries! Ebby's just happy she got to make a new friend. See you in the morning!"
    pr "Night, Ebby."
    scene bg black with fade
    
    return






label day1morningwakeFin:

        
    scene bg xebdorm_room with fade

    prin "I wake to sunlight streaming in the window and give a stretch."
    nn "Mmmm this is nice - when was the last time waking up in the morning felt so damn good?"
    prin "There's a school uniform with my name tagged onto it. I have no clue what the hell's going on, but I think I can understand that much"
    
    scene bg xebdorm with fade
    prin "I walk out into what looks like the main room, onty to be greeted by a small girl getting dressed"
    show sars
    ug "Wh-what are you doing here, intruder! Pervert! GET OUT!"
    prin "I promptly fuck off back to my room. Maybe I'll clean myself up a bit..."
    scene bg xebshower with fade

    "After getting washed and dressed I give myself a look over in the mirror.{p}
    So this is how I look in a school uniform?{p}
    Not half bad if I say so myself.{p}"
    nn "Laughing, I head down for breakfast."

    scene bg xebdorm with fade

    show sars notamused at left:
        zoom 1.5

    sars "AHH! It's the pervert! Don’t look at him or you’ll get molested!"

    show aids concerned behind sars:
        zoom 1.8
        xalign 0.3
        yalign 1.0
    eidzu "Ehhhh? What?!?!?"
    pr "Good morning ladies!"
    sars "Grrrrrr!"
    eidzu "Ah..g-good morning!"

    hide sars
    hide aids

    show mal happy at left:
        xalign 0.1
    mal "*smile* *nod*"

    show ebby toastdead behind mal:
        xalign 0.3
        yalign 1.0

    ec "...."

    nn "Ebola-chan is nibbling on her toast, but she seems to be still asleep.
    I guess she isn’t good with mornings."

    hide ebby
    hide mal

    show bp happy:
        xalign 0.1

    bp "Now now, settle down and enjoy your breakfast! It’s the most important meal of the day you know!"

    nn "Not one to refuse a nice homecooked meal, I dig in."

    "Mmm! This is delicious!"

    bp "I’m glad it’s to your tastes!"

    "Definitly!"

    pr "I could easily get used to this." 

    hide bp

    show sars notamused at left:
        zoom 1.5
    sars "I’m done! Come on Eidzu, let's leave now, I don’t want to be around HIM any longer than I have to!"
    show aids concerned behind sars:
        zoom 1.8
        xalign 0.3
        yalign 1.0
    eidzu "Ah! Yes - we’ll be going now!"

    hide sars
    hide aids

    pr "She barely has time to call out as she is dragged out the door."

    show mal notmal at left:
        xalign 0.1

    mal "I should be going too, I want to study a little before class while it’s quiet."
    mal "Thank you for the meal."

    show bp happy behind mal:
        xalign 0.3

    bp "Have a good day!"
    mal "I’ll see you two in class."

    hide mal
    hide bp

    show ebby toastdead:
        xalign 0.1
        yalign 1.0
    ec "..."

    hide ebby
    return




label day1_morningFin_dorm:
    nn "Well there is no sense in being too early on my first day, but I don’t want to be late either."
    nn "I head back to my room and double-check that I have everything I need for the day."
    scene bg xebdorm_room with fade
    nn "Ok, looking good."
    scene bg xebdorm_door with fade
    nn "All right, time to go.{p}
    I’m actually starting to feel a bit nerv-"
    ec "AAAAAAAHHHHHHHHHHHHHHHHHHHHHH!!!!!!!!!"
    nn "With a toast-muffled cry Ebola-chan bursts out of into the hall."
    show ebby toastsad at left
    ec "Mfff mff! Mfff mfffff mff mff mffff!"
    nn "Years of cultist experience in understanding the esoteric utterances of summoned other-worldly entities kick in instantly."
    ec "{color=#57bab7}(Oh no! I'm going to be late!){/color}"
    "No, no, you’re ok. We have plenty of time, it’s only half past."
    nn "I glance up at the clock over the door - it says ten to.{p}...oh no."
    nn "My watch still says half past{p}..and isn’t ticking."    
    "AHHHHH!! I’m going to be late!"
    ec "Mfff mffff mfffff-mff mmmmff mffff, mfff!\"{p}
    \"{color=#57bab7}(That's what Ebola-chan already said, silly!){/color}"
    nn "Think, think, think - yeah we can do this."
    "If we run we can still make it!"
    nn "I grab her hand and drag her out the door!"
    ec "Mffffffff!\"{p}
    \"{color=#57bab7}(Kyaaaaa!){/color}"
    "We’ll be heading out!"
    bp "Have a good day!"


    hide ebby
    show bg xebstreet with fade
    show bg xebstreet2 with fade
    show bg xebstreet3 with fade
    nn "It’s actually quite exhilarating.{p}
    Running along like this, I’d almost forgotten this feeling, legs pounding, wind in my hair."
    nn "I feel...alive."
    nn "Being hand in hand with a cute girl is not unpleasant either."
    nn "Although her status as ‘girl’ is perhaps open to debate, she certainly measures up to cute in my book."
    show ebby toastjoy at left
    nn "I turn to look at her, twintails streaming she runs along beside me earnestly."
    nn "She flashes me a smile and gives my hand a friendly squeeze."
    ec "Mfff mf mf! Mf mfff mf mf!\"{p}
    \"{color=#57bab7}(Keep it up! We can do it!){/color}"
    hide ebby
    nn "Giving her hand a squeeze back I run on.{p}
    Why the hell she still has the toast in her mouth is beyond me."

    show bg xebstreet4 with fade
    show bg xebstreet5 with fade
    show bg xebgate with fade
    nn "We skid to a stop in front of the school gate."
    "I don't know the way from here!"
    show ebby toastjoy at left
    ec "Mmff mffff, mmfff-mfff mfff!\"{p}
    \"{color=#57bab7}(Don't worry, Ebola-chan does!){/color}"
    hide ebby
    nn "Pulling me along, she dashes off towards the main building."
    show bg xebgrass with fade
    show bg xeblockers with fade
    show bg xebstairs with fade
    show bg xebcorridor with fade
    show bg xebclass with fade

    show ebby toastjoy at left
    ec "MFFF!!\"{p}
    \"{color=#57bab7}(SAFE!!){/color}"
    hide ebby
    show sars stars at left:
        zoom 1.5
    sars "WHAT THE HELL ARE YOU DOING WITH MY EBOLA-CHAN!!!"
    with vpunch
    sars "PERVERT!"
    with hpunch
    sars "MOLESTER!"
    with vpunch

    nn "Before I can even catch my breath, I’m assaulted by a manic Sars-chan."

    show ebby toastsad
    ec "mfff mf mfff-mfff! mff mmmfffff mfff mfff!\"{p}
    \"{color=#57bab7}(Stop it Sars-chan! It's nothing like that!){/color}"
    show sars concerned at left:
        zoom 1.5
    sars "What? Take that toast out of your mouth, I can't understand a word!"
    show sars stars at left:
        zoom 1.5
    sars "-or did he force it on you?"
    with hpunch
    sars "TOAST FETISHIST!"
    ec "Mffff! Mf mmmffff.\"{p}
    \"{color=#57bab7}(Ohh! I forgot.){/color}"
    nn "Finally she takes it out of her mouth."
    show ebby rape
    ec "%(player_name)s-kun didn’t do anything like that! Stop being so mean!{p}
    He was very kind and ran with me all the way here so that I wouldn’t be late!"
    show sars concerned at left:
        zoom 1.5
    sars "Hmph! I dont care how kind he is, he shouldn’t be holding your hand with such familiarity!"
    show ebby concerned
    ec "Eh?"
    nn "She looks down as if suddenly realizing we’re still holding hands."
    show ebby joy
    ec "Oh! Hehe"
    nn "She gives my hand a last friendly squeeze before letting go and giving me a quick bow."
    ec "Thank you %(player_name)s-kun, I wouldn't have made it on time without you!"
    nn "Now I actually start to feel embarrassed."
    "We both made it in time, that’s the important thing."
    teach "All right! Settle down and get to your seats everyone!"
    nn "And here is the teacher now, looks like we really did make it just in time."
    nn "Ebola-chan flashes me a quick smile and heads to her seat."
    hide ebby
    sars "I'm watching you, toast-fetishist!"
    hide sars
    "Yes, this is going to be an experience indeed."

    scene bg black with fade
    $ebby_affection+=1
    return
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
label day1_SnackFin_classFin:
    scene bg xebdesk with fade
    "It looks like someone is asleep at their desk."  
    
    
    menu:
        "Should I wake them up?":
            call lind_wakeFin
        "I should just let them rest.":
            call lind_nowakeFin   
    
    "Are you ok? I think you fell asleep there."
    show rab annoyed at left:
        zoom 1.8
    rab "I KNOW THAT."
    show rab unsure at left:
        zoom 1.8
    rab "I don't sleep well, so sometimes I come where it's quiet."
    show rab normal at left:
        zoom 1.8
    rab "Oh well... I'm awake now... sorry, who were you again?"
    "I'm %(player_name)s. It's my first day here."
    show rab unsure at left:
        zoom 1.8
    rab "You're... new here...?"
    show rab happy at left:
        zoom 1.8
    rab "YEY! Wait until Ebola-chan hears that I got to talk to the new kid! She'll freak out!"
    "But I already met her..."
    show rab unsure at left:
        zoom 1.8
    rab "Oh..."
    "The two of you stare at each other, awkwardly. It looks like she might still be drooling."
    show rab normal at left:
        zoom 1.8
    rab "Well, I know something YOU haven't seen yet. Come with me!"#
    "She grabs you by the hand and drags you off with her."

    scene bg xebgrass with fade

    show rab unsure at left:
        zoom 1.8
    rab "So...what do you think?"

    menu:
        "It's ok.":
            call lind_itsokFin
        "It's beautiful!":
            call lind_beutFin

    menu:
        "I don't mind the rain.":
            call lind_raingoodFin
        "I hate the rain.":
            call lind_rainbadFin

    "The bell rings out signaling the end of the break."

    show rab shock at left:
        zoom 1.8
    rab "OH. We should get to class."
    show rab normal at left:
        zoom 1.8
    rab "I guess I'll see you around... sorry, what was your name again?"
    "It's %(player_name)s."
    rab "Well, it was nice to meet you, %(player_name)s-San, I'm Rabies. I guess I'll see you later, then..."

    "She skips away."
    show rab happy at left:
        zoom 1.8
    rab "I got to meet the new kid!~"

    scene bg black with fade

    return

label lind_wakeFin:
    "Uh, excuse me?"
    show rab unsure at left:
        zoom 1.8
    rab "Huh...wha...?"
    return  

label lind_nowakeFin:
    "They must be tired, I should just let them sleep."
    "Unfortunately the door makes a loud creek as I go to leave."
    show rab unsure at left:
        zoom 1.8
    rab "Huh...wha...?"
    show rab shock at left:
        zoom 1.8
    rab "NOCOMEBACK!"
    return

label lind_itsokFin:
    show rab annoyed at left:
        zoom 1.8
    rab "WHAT? I go through all the effort of taking you here, and all you say is 'it's ok'?"
    show rab unsure at left:
        zoom 1.8
    rab "Well, I guess it's a bit cloudy. I'd rather have shown you when it was sunny out. It almost looks like it's about to rain.."
    return

label lind_beutFin:
    show rab happy at left:
        zoom 1.8
    rab "I know, right? I come here all the time to get some fresh air."
    show rab unsure at left:
        zoom 1.8
    rab "Except when it rains... it kinda looks that way right now..."
    return

label lind_raingoodFin:
    show rab annoyed at left:
        zoom 1.8
    rab "NO. WATER IS BAD."
    show rab unsure at left:
        zoom 1.8
    rab "It gets in my ears and makes them feel all full."
    return

label lind_rainbadFin:
    show rab shock at left:
        zoom 1.8
    rab "You do?"
    show rab normal at left:
        zoom 1.8
    rab "So do I. It's just such a downer..."
    return
























    
    



label day1_lunchFin_explore:
    scene bg xebriver with fade
    show pro:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    pr "How did I end up here?"
    pr "I realy shouldn't have walked around without someone to guide me, now I'm lost"
    show zmapp:
        zoom 1.0
        xalign 0.9
        yalign 0.7
    "I think there's someone else here"
    pr "Hello?"
    ug "WHAAAAAAAAA. Don’t sneak up on me like that! I’m working here."
    pr "Working on what?"
    ug "Oh, you’ll see… Now, let me get back to work."
    ug "So… if I put this one here…"
    ug "OH SHIT"
    show ebby rape:
        zoom 1.0
        xalign 0.7
        yalign 0.7
    ec "IT'S RAPE TIME"
    ug "No, No, No!"
    ec "I GOT YOU NO-oh."
    ec "MC?"
    hide zmapp
    ec "OH GOD I’M SO SORRY. I didn’t mean to hurt you. Are you ok?"
    pr "Yes, I think."
    ec "Anyway, you didn’t happen to see someone in green run this way, did you?"
    pr "Yeah… they went that way, why?"
    ec "I’LL TELL YOU LATER."
    
    
    scene bg xebroof
    "I think I finally found them"
    show ebby sad:
        zoom 1.0
        xalign 0.7
        yalign 0.7
    show zmapp:
        zoom 1.0
        xalign 0.9
        yalign 0.7
    ug "Come on, ‘Pinky’, you’ll have to do better than that if you want your hat back."
    ec "Oh yeah?"
    hide ebby
    hide zmapp
    show ebbyz:
        zoom 1.0
        xalign 0.7
        yalign 0.7
    ug "Shit."
    ec "Wait, we're laste for class"
    hide ebbyz
    show zmapp:
        zoom 1.0
        xalign 0.7
        yalign 0.9
    ug "(Panting on the ground)"
    scene bg black with fade
    return







