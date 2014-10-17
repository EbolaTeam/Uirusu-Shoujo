label day1_morningRy_libraryRy:
    scene bg xebcorridor with fade
    show ebby normal:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    "We got to school not long after"
    ec "...the principals office is just beside you, and over here is the library"
    ec "We should probably get you a library card so you can borrow books"
    pr "Do we have time? We've been walking around for a while?"
    ec "Don't worry, class doesn't start 'till 9"
    scene bg xeblibrary
    "We walked into the sparse library, it was mostly empty spare one girl reading a book"
    
    show ebby sad:
        zoom 1.0
        xalign 0.3
        yalign 1.0
    ec "Aww, the librarian's not in"
    pr "Shame, we still have a few minutes before class"
    show ebby joy
    ec "Hey look, it's Eidzu!"
    pr "Who?"
    show ebby excited
    ec "EIDSU-CHAN! EIDSU-CHAN!"
    pr "Quiet, we're in a library!"
    show ebby wink
    ec "We're the only onces here, silly! Come on, let's go chat with Aids!"
    show aids excited:
        zoom 1.8
        xalign 0.9
        yalign 1.0
    ai "h-Hi Ebby, who's your new friend?"
    show ebby concerned
    ec "He's... wait, Eidzu, are you reading a naughty book again?"
    show aids concerned
    ai "N-no! It isn't like that I'm not"
    ec "Gimmie"
    show aids sad
    ai "n-No! Don't read that!"
    show ebby sad
    ec "Let's see what you've been reading: \"I don't love you. I've never loved anyone. I wanted you from the first moment I saw you. I wanted you as one wants a whore – for the same reason and purpose.\""
    show ebby concerned
    ec "Eidzu, why are you always reading such lewd things? A girl like you shouldn't be interested in this sort of thing!" 
    ai "I-I'm sorry Ebby, I, I just,"
    show aids rape
    ai "Hey, you haven't even introduced your friend yet! How rude!"
    show ebby rape
    ec "Don't try to chance the subject you little pervert!"
    ai "Nu-uh. Who is he? Is he your boyfriend?"
    show ebby concerned
    ec "No! It's not like that, he's just a friend of Papa"
    show aids joy
    ai "Shame. He's pretty cute."
    pr "He's right here you know."
    show aids normal
    show ebby normal
    ai "I'm just playing with you. Maybe we can meet up after class?"
    menu:
        "Sure":
            $ AidsCount += 1
            pr "Sure, See you then!"
            show aids excited
            ai "YAY! I can't wait!"
        "I don't know":
            pr "I don't know, I still have plenty of stuff to do today."
            show aids sad
            ai "Aww, I wanna hang out with cute boys..."
    show ebby concerned
    ec "Are you gonna keep behaiving like that around boys?"
    show aids joy
    ai "Yep!"
    ai "Anyway, class starts soon. We better get going"
    show ebby normal
    ec "Bye then."
    if AidsCount == 1:
        ai "See you after class!"
    pr "Later!"
    $ AidsCount += 1
    $ AidsMeet += 1
    return
    
    
    
    
    
    
label day1_lunchRy_corridorRy:
    scene bg xebcorridor with fade
    if AidsMeet == 0:

        show ebby normal:
            zoom 1.0
            xalign 0.1
            yalign 1.0
        ec "You're probably hungry, I'll show you the cafiteria"
        pr "Yeah, funny how lunch does that to you"
        "There's a sad looking girl sitting down over there"
        show ebby concerned
        ec "Aww, Eidzu's sad, maybe we should go and chear her up?"
        menu:
            "Sure":
                pr "Of course, let's go chat to her"
                jump Day1AidLunchComfort
            "Let's not":
                pr "Nah, she's probably just resting"
                $ EbbyBrowniePoints -= 1
                show ebby sad
                ec "She's crying you inconsiderate shit!"
                "A guy just walked up to her"
                ec "Oh, HIV's here, I guess she'll be fine."
                jump Day1AidsLatterLunch



    else:
        "elsetest"
        return
        
        
    "afteriftest"
    return
    

















    
    show ebby sad:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    show aids sad:
        zoom 1.8
        xalign 0.9
        yalign 1.0
    ec "Poor Aids wanted to have lunch with Hiv but he is not around so she ate with protag instead."
    $aids_affection+=1
    return

























    
label day1_afternoonRy_gateRy:
    scene bg xebgate with fade
    show ebby sad:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    show aids sad:
        zoom 1.8
        xalign 0.9
        yalign 1.0
    ec "Poor Aids wanted to walk home with Hiv but he is off to bang a floozy."
    $aids_affection+=1
    return
    
    
label day1_eveningRy_showerRy:
    scene bg xebshower with fade
    show ebby rape:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    show aids joy:
        zoom 1.8
        xalign 0.9
        yalign 1.0
    ec "Aids walks in on protag naked in the shower! What a perverted girl!"
    $aids_affection+=1
    return