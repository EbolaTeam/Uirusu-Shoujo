label day1_SnackFin_libraryFin:
    scene bg xebcorridor with fade
    show ebby normal:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    ec "...the principal's office is just beside you, and over here is the library."
    ec "We should probably get you a library card so you can borrow books."
    pr "Do we have time? We've been walking around for a while."
    ec "Don't worry, class doesn't start again for 10 minutes."
    scene bg xeblibrary
    "We walked into the sparse library, it was mostly empty spare one girl reading a book."
    
    show ebby sad:
        zoom 1.0
        xalign 0.3
        yalign 1.0
    ec "Aww, the librarian's not in."
    pr "Shame, we still have a few minutes before class."
    show ebby joy
    ec "Hey look, it's Eidzu!"
    pr "Who?"
    show ebby excited
    ec "EIDSU-CHAN! EIDSU-CHAN!"
    pr "Quiet, we're in a library!"
    show ebby wink
    ec "We're the only ones here, silly! Come on, let's go chat with Eids!"
    show aids excited:
        xalign 0.9
        yalign 1.0
    ai "H-hi Ebby, who's your new friend?"
    show ebby concerned
    ec "He's... wait, Eidzu, are you reading a naughty book again?"
    show aids concerned
    ai "N-no! It isn't like that I'm not-"
    ec "Gimmie"
    show aids sad
    ai "N-no! Don't read that!"
    show ebby sad
    ec "Let's see what you've been reading: \"I don't love you. I've never loved anyone. I wanted you from the first moment I saw you. I wanted you as one wants a whore – for the same reason and purpose.\""
    show ebby concerned
    ec "Eidzu, why are you always reading such lewd things? A girl like you shouldn't be interested in this sort of thing!" 
    ai "I-I'm sorry Ebby, I, I just-"
    show aids rape
    ai "Hey, you haven't even introduced your friend yet! How rude!"
    show ebby rape
    ec "Don't try to change the subject you little pervert!"
    ai "Nu-uh. Who is he? Is he your boyfriend?"
    show ebby concerned
    ec "No! It's not like that, he's just a friend of Papa."
    show aids joy
    ai "Shame. He's pretty cute."
    pr "He's right here you know."
    show aids normal
    show ebby normal
    ai "I'm just playing with you. Maybe we can meet up after class?"
    menu:
        "Sure":
            $ AidsCount += 1
            $ AidsMetFulfilled = 1
            $ AidsMetAtLunch = 1
            pr "Sure, see you then!"
            show aids excited
            ai "YAY! I can't wait!"
        "I don't know":
            pr "I don't know, I still have plenty of stuff to do today."
            show aids sad
            ai "Aww, I wanna hang out with cute boys..."
    show ebby concerned
    ec "Are you gonna keep behaving like that around everyone?"
    show aids joy
    ai "Yep!"
    ai "Anyway, class starts soon. We better get going."
    show ebby normal
    ec "Bye then."
    if AidsCount == 1:
        ai "See you after class!"
    pr "Later!"
    $ AidsCount += 1
    $ AidsMeet += 1
    $ aids_affection += 1
    return
    
    
    
    
    
    
    
    
    
    
    
    
label day1_lunchFin_corridorFin:
    scene bg xebcorridor with fade
    if AidsMeet == 0:

        show ebby normal:
            zoom 1.0
            xalign 0.1
            yalign 1.0
        ec "You're probably hungry, I'll show you the cafeteria."
        pr "Yeah, funny how lunch does that to you."
        "There's a sad looking girl sitting down over there."
        show ebby concerned
        ec "Aww, Eidzu's sad, maybe we should go and cheer her up?"
        menu:
            "Sure":
                pr "Of course, let's go chat to her."
                $ AidsMeet = 1
                $ AidsCount =+ 1
                $ aids_affection += 1
                jump Day1AidLunchComfort
            "Let's not":
                pr "Nah, she's probably just resting."
                $ EbbyBrowniePoints -= 1
                $ AidsPassed = 1
                show ebby sad
                ec "She's crying you inconsiderate shit!"
                "A guy just walked up to her"
                show ebby normal
                ec "Oh, HIV's here, I guess she'll be fine."
                jump Day1AidsLatterLunchEbbs



    else:
        if AidsCount < 2:
            show aids sad at right
            pr "Hey, Eidzu!"
            show aids excited
            ai "Protag?"
            ai "YAY! I was hoping I'd see you again!"
            pr "Same here"
            show aids joy
            ai "Really?"
            $ AidsProprietary = 1
            show aids normal
            pr "Yeah."
            ai "Hey, where's Ebby? Usually on their first day people stick to their guides like glue!"
        else:
            $ AidsMetFulfilled = 0            
            show aids normal at center
            pr "Hey, Eidzu!"
            show aids excited
            ai "YAY, YOU MADE IT!"
            pr "Hope I didn't keep you waiting too long, had a little mixup with Ebby."
            show aids normal
            ai "Where is she, anyway? Usually on their first day people stick to their guides like glue!"
        ai "Thick, viscuss, sticky white glue..."
        show aids normal
        pr "I dunno, she whent off chasing after some green haired girl, I think she stole her hat or something..."
        pr "They looked pretty similar, does she have a sister or something?"
        ai "Yeah, but they're all equally pink. Weird, I haven't seen anyone with green hair around in ages..."
        pr "Maybe someone else joined today?"
        show aids joy
        ai "Who knows?"
        show aids normal
        ai "Anyway, wanna go get lunch togeather?"
        pr "Sure, I'm starving. I- I don't even remember the last time I ate..."
        show aids joy
        ai "You're almost as ditsy as Ebby!"
        show aids normal
        show ebbyzch:
            zoom 1.0 xalign -2 yalign 0.7 
        show ebbyzch:
            linear 1.0 zoom 1.0 xalign 3.0 yalign 0.7
        "SWWWOOOOSHHH"

        "A green streak shot past us, followed by a shorter pink one."
        ai "Well that's Ebster explained."
        pr "Still, brings up a couple more questions than it answers."
        pr "..."
        pr "So, lunch?"
        show aids excited
        ai "LUNCH!"
        $ AidsCount += 1
        $ aids_affection += 1
        jump Day1AidsLatterLunchAids


#AutoReturn








label Day1AidLunchComfort:
        ec "Eidzu? Are you okay?"
        show aids sad at center
        ai "HIV-kun said he'd meet me at lunch but he's too busy railing that harlot Sian."
        pr "Did you say Sian?"
        show ebby normal
        ec "Aww, poor girl. Want a huggu?"
        show aids rape
        ai "Depends, is your friend free?"
        show ebby concerned
        ec "Don't be lewd!"
        ai "That wasn't lewd at all!"
        ec "What you where thinking was!"
        pr "I'm fine with it Ebbs"
        show ebby normal
        ec "Oh, o-okay then."
        show aids normal
        ai "So, how do you two know each other?"
        ec "My dad introduced me to him."
        show aids excited
        ai "Oh, so that's what's going on."
        show ebby concerned
        ec "No, it's not like that, daddy just wanted me to make sure he fits in well."
        show aids joy
        ai "I bet I can make him fit in well!"
        ec "Y-you shouldn't be saying things like that!"
        pr "Wha~?"
        show aids normal
        ai "Anyway, I hope we can meet soon, maybe after school some time?"
        pr "We'll see."
        show aids joy
        ai "YAY!"
        ec "Anyway, it's getting late, we better go eat lunch."
        ai "Later you two."
        pr "Bye."
        jump Day1AidsLatterLunchEbbs
        return






label Day1AidsLatterLunchEbbs:
"NomNomLunchWithEbbsNom"
return  


label Day1AidsLatterLunchAids:
"NomNomLunchWithEidzNom"
return






init:
    $ AidsPassed = 0

label day1_afternoonFin_gateFin:
    scene bg xebgate with fade
    show ebby normal at left
    if AidsMeet == 0:
        nn "Me and Ebster walk home together"
        nn "Huh, funny. I called the dorm \"Home\". Guess I've really snapped out of reality pretty quickly..."
        if AidsPassed == 1:
            nn "She looks like the one we saw earlier at lunch, I wonder if Ebby still thinks I'm a dick for that..."
        show ebby sad
        ec "Aids! AIDS!"
        show aids normal
        ai "Y-yeah Ebby?"
        show ebby concerned
        ec "You've been alone a lot recently. Ebola-chan is worried about you!"
        ai "D-don't be, it's just HIV, he's not spending as much time with me anymore."
        show ebby normal
        ec "Aww, poor girl. Want a huggu?"
        show aids rape
        ai "Depends, is your friend free?"
        show ebby concerned
        ec "Don't be lewd!"
        pr "I'm fine with it Ebbs."
        show ebby normal
        ec "Oh, o-okay then."
        ec "Anyway, wanna walk home with us?"
        show aids joy
        ai "Sure! So, how did you two meet?"
        ec "My dad introduced me to him."
        show aids excited
        ai "Oh, so that's what's going on."
        show ebby concerned
        ec "No, it's not like that, daddy just wanted me to make sure he fits in well."
        show aids joy
        ai "I bet I can make him fit in well!"
        "Show ebby flustered"
        ec "Y-you shouldn't be saying things like that!"
        pr "Wha~?"
        $ AidsMeet = 1
    else:
        nn "I see Aids sitting alone on a bench, looking like she's waiting for someone."    
        show aids sad at right
        pr "Aids, you okay?"
        show aids normal
        ai "Mostly. HIV's ditched me again for another floozy."
        show aids sad
        ai "Why don't I ever get to have fun with him anymore?"
        pr "If you want you can always hang out with me."
        show aids excited
        ai "REALLY! YAY!"
        show aids normal
        nn "Aids followed me an Ebby back to the dorm."
    show ebby normal
    show aids normal
    ec "Huh, home already..."
    pr "Just in time, it's almost starting to rain..."
    ai "Well, I better go then. I'm all dirty, so I gotta have a shower."
    ec "I should probably get going too, I promised Bee I'd help her cook tonight."
    ai "Later you two!"
    ec "Seeya!"
    $ AidsCount += 1
    $ aids_affection += 1
    $ AidsInvite = 1
    return
    
    
label day1_eveningFin_showerFin:
    scene bg xebshower with fade
    if AidsMeet == 0:
        show aids concerned at right
        nn "After today's shinanigans a nice warm shower feels suprisingly good...{p}
        I'm pretty sure I saw a girl I met earlier peeking at me."
        hide aids
        with moveoutright
        nn "Nevermind, nothing wrong with a pervert, plus I wouldn't mind a peek at Ebby, if I do say so..."
        $ AidsMeet = 1
    else:
        nn "After today's shinanigans a nice warm shower feels suprisingly good."
        show aids joy at right
        nn "Aids accidentally walked in on me, although \"Accidentally\" may be up for debate."
        ai "S-sorry, I didn't mean to walk in on you l-like this..."
        hide aids
        with moveoutright
        nn "I wouldn't mind too bad, but she's already gone."
        
    
    $ AidsCount += 1
    $ aids_affection += 1
    return
    
    
    
    
    
    
    
    

label day1_NightFin_BedFin:
scene bg black with fade
pause (1)
scene bg xebdorm_room with fade
pause (1)
prin "Bloody hell, what a day..."
prin "Wait, what the fuck? Why am I in a school? I'm 25! I graduated Uni years ago! THIS DOESN'T MAKE ANY FUCKING SENSE!"
prin "WHY DID I NOT NOTICE HOW WEIRD THIS IS EARLIER, WHAT THE SHIT."
prin "Oh who cares, time for some sleep"
ug "Can it wait?"
pr "Who's there?"
show aids normal at center
ai "Me, silly."
pr "Eidz, what are you doing in here?"
show aids sad
if AidsInvite == 1:
    ai "You said I could hang out with you if I wanted."
    pr "This isn't really what I had in mind, but still, why are you up so late?"
ai "I couldn't sleep, I had a dream. Mind if I stay with you tonight? I don't wanna be in my room alone."
pr "Aww, I'm sorry, sure... I guess, stay if you want. What was your nightmare about, if you don't mind me asking?"
show aids joy
ai "I never said it was a bad dream, but you are to blame, so I'll keep that apology."
pr "Wait, what?"
show aids normal
ai "Mind if we cuddle?"
pr "WHAT?"
show aids excited
ai "That's a yes to me!"
scene bg black
"CLICK"
ai "Night"
if AidsProprietary == 1:
    prin "..."
    pr "C-could you move a little? Your knee's kinda poking into me."
    ai "That's not my knee."
jump end




label ElseAids:
    scene bg xebclass with fade
    show ebby joy:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    "You do something with someone that doesn't involve Aids"
    return
    
    
    
    
    
    
    
label day1_morningFin_ElseAids:
    scene bg xebclass with fade
    show ebby joy:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    "You do something with someone that doesn't involve Aids"
    return
    
label day1_lunchFin_ElseAids:
    scene bg xebclass with fade
    show ebby joy:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    "You do something with someone that doesn't involve Aids"
    return
    
label day1_afternoonFin_ElseAids:
    scene bg xebclass with fade
    show ebby joy:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    "You do something with someone that doesn't involve Aids"
    return
    
    
label day1_eveningFin_ElseAids:
    scene bg xebclass with fade
    show ebby joy:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    "You do something with someone that doesn't involve Aids"
    return
    
    
    