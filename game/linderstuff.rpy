label linderstuff:

    #(Someone's slumped over the table. They seem to be asleep.)#   

    scene bg xebdesk with fade
    nn "It looks like someone is asleep at their desk"  
    

    menu:
        "Should I wake them up?":
            call lind_wake
        "I should just let them rest.":
            call lind_nowake    
    
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
    rab "YEY! Wait until Ebola-Chan hears that I got to talk to the new kid! She'll freak out!"
    "But I already met her..."
    show rab unsure at left:
        zoom 1.8
    rab "Oh..."
    nn "The two of you stare at each other, awkwardly. It looks like she might still be drooling."
    show rab normal at left:
        zoom 1.8
    rab "Well, I know something YOU haven't seen yet. Come with me!"#
    nn "She grabs you by the hand and drags you off with her."

    scene bg xebgrass with fade

    show rab unsure at left:
        zoom 1.8
    rab "So...what do you think?"

    menu:
        "It's ok.":
            call lind_itsok
        "It's beautiful!":
            call lind_beut

    menu:
        "I don't mind the rain.":
            call lind_raingood
        "I hate the rain.":
            call lind_rainbad

    nn "The bell rings out signaling the end of the break."

    show rab shock at left:
        zoom 1.8
    rab "OH. We should get to class."
    show rab normal at left:
        zoom 1.8
    rab "I guess I'll see you around... sorry, what was your name again?"
    "It's %(player_name)s."
    rab "Well, it was nice to meet you, %(player_name)s-San, I'm Rabies. I guess I'll see you later, then..."

    nn "She skips away."
    show rab happy at left:
        zoom 1.8
    rab "I got to meet the new kid!~"

    scene bg black with fade

return

label lind_wake:
    "Uh, excuse me?"
    show rab unsure at left:
        zoom 1.8
    rab "Huh...wha...?"
return  

label lind_nowake:
    "They must be tired, I should just let them sleep"
    nn "Unfortunately the door makes a loud creek as I go to leave."
    show rab unsure at left:
        zoom 1.8
    rab "Huh...wha...?"
    show rab shock at left:
        zoom 1.8
    rab "NOCOMEBACK!"
return

label lind_itsok:
    show rab annoyed at left:
        zoom 1.8
    rab "WHAT? I go through all the effort of taking you here, and all you say is 'it's ok'?"
    show rab unsure at left:
        zoom 1.8
    rab "Well, I guess it's a bit cloudy. I'd rather have shown you when it was sunny out. It almost looks like it's about to rain.."
return

label lind_beut:
    show rab happy at left:
        zoom 1.8
    rab "I know, right? I come here all the time to get some fresh air."
    show rab unsure at left:
        zoom 1.8
    rab "Except when it rains... it kinda looks that way right now..."
return

label lind_raingood:
    show rab annoyed at left:
        zoom 1.8
    rab "NO. WATER IS BAD."
    show rab unsure at left:
        zoom 1.8
    rab "It gets in my ears and makes them feel all full."
return

label lind_rainbad:
    show rab shock at left:
        zoom 1.8
    rab "You do?"
    show rab normal at left:
        zoom 1.8
    rab "So do I. It's just such a downer..."
return


