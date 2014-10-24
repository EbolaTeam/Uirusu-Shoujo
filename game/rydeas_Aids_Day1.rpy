label Day1AidLunchComfort:
        ec "Eidzu? Are you okay?"
        show aids sad
        ai "HIV-kun said he'd meet me at lunch but he's too buisy railing that slut Sian"
        pr "Did you say Sian?"
        show ebby normal
        ec "Aww, poor girl. Want a huggu?"
        show aids rape
        ai "Depends, is your friend free?"
        show ebby concerned
        ec "Don't be lewd!"
        pr "I'm fine with it Ebbs"
        show ebby normal
        ec "Oh, o-okay then."
        show aids normal
        ai "So, how do you two know each other?"
        ec "My dad introduced me to him"
        show aids excited
        ai "Oh, so that's what's going on"
        show ebby concerned
        ec "No, it's not like that, daddy just wanted me to make sure he fits in well"
        show aids joy
        ai "I bet I can make him fit in well!"
        "Show ebby flustered"
        ec "Y-you shouldn't be saying things like that!"
        pr "Wha~?"
        show aids normal
        ai "Anyway, I hope we can meet soon, maybe after school some time?"
        pr "We'll see"
        show aids joy
        ai "YAY!"
        ec "Anyway, it's getting on, we better go eat lunch"
        ai "Later you two"
        pr "Bye"
        jump Day1AidsLatterLunchEbbs
        return






label Day1AidsLatterLunchEbbs:
"NomNomLunchWithEbbsNom"
return  


label Day1AidsLatterLunchAids:
"NomNomLunchWithEidzNom"
return



label day1_NightRy_BedRy:
scene bg black with fade
pause (1)
scene bg xebdorm_room with fade
pause (1)
prin "Bloody hell, what a day..."
prin "Wait, What the fuck? Why am I in a school? I'm 25! I graduated Uni years ago! THIS DOESN'T MAKE ANY FUCKING SENCE"
prin "Oh who cares, time for some sleep"
ug "Can it wait?"
pr "Who's there?"
show aids normal
ai "Me, silly."
pr "Eidz, what are you doing in here?"
show aids sad
ai "I couldn't sleep, I had a dream"
pr "Aww, I'm sorry"
show aids joy
ai "I never said it was a bad one, but you are to blame, so I'll keep that apology"
pr "What, what?"
show aids normal
ai "Mind if we cuddle"
pr "What?"
show aids excited
ai "That's a yes to me!"
scene bg black
"CLICK"
ai "Night"
if AidsProprietary == 1:
    prin "..."
    pr "C-could you move a little? Your knee's kinda poking into me."
    ai "That's not my knee."
scene bg xebfin with fade
pause (3)
scene bg black with fade
jump end




label ElseAids:
    scene bg xebclass with fade
    show ebby joy:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    "You do something with someone that doesn't involve Aids"
    return
    
    
    
    
    
    
    
label day1_morningRy_ElseAids:
    scene bg xebclass with fade
    show ebby joy:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    "You do something with someone that doesn't involve Aids"
    return
    
label day1_lunchRy_ElseAids:
    scene bg xebclass with fade
    show ebby joy:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    "You do something with someone that doesn't involve Aids"
    return
    
label day1_afternoonRy_ElseAids:
    scene bg xebclass with fade
    show ebby joy:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    "You do something with someone that doesn't involve Aids"
    return
    
    
label day1_eveningRy_ElseAids:
    scene bg xebclass with fade
    show ebby joy:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    "You do something with someone that doesn't involve Aids"
    return
    
    
    