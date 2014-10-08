label Africa:

    scene bg black with fade
    $renpy.music.set_volume (0.5, channel="music")
    play music "FeelsChiptune.mp3" noloop
    
    centered "{i}Maybe today...{/i}"
    
    centered "{i}Maybe in Africa...{/i}"
    
    scene bg bg1 with fade
    
    pause 1.0
    
    "Vu-chan!{w=1.5} Vu-chan!{p=1.5}
    Where are you Vu-chan?"

    show ebby excited:
        zoom 1.0
        xalign 0.1
        yalign 1.0
        
    ec "Vuuuu-chaaaan!!"
    
   
    show vu normal:
        zoom 1.0
        xalign 0.9
        yalign 1.0

    vc "Keep yer shimpan on dearie,
    I'm here."

    show ebby joy

    ec "Vu-chan! Yay!"
    ec "It's gotten so quiet around here,"

    show ebby normal

    ec "Ebola-chan was getting lonely!"

    vc "Of course it's quiet you puerile pestillance!"
    vc "Everybody's dead!"

    show ebby concerned
    
    ec "Dead?"

    vc "Yes, Dead! Expired! Bereft of Life!
    You've bled 'em all dry!"
    vc "Me and me mates 'ave been munching on 'em all morning!"
    vc "Unless they can magically come back from a vultures lower intestine,
    yes, they are all very much dead!"

    ec "But what will ebola-chan do?"
    ec "Ebola-chan doesn't want to be lonely!
    She wants to play with more and more humans!"

    vc "Bloomin' eck you're voracious-virus!"
    vc "Don't you want to 'ave an after-epidemic nap or something?"


    show ebby sad
    
    ec "Ebola-chan doesn't want a nap!
    Ebola-chan doesn't want to be lonely!"
 
    ec "Ebola-chan wants to PLAY!"

    vc "All right, all right, calm yer waterworks already.
    I'll think of something."



    show ebby joy

    ec "Yay! Vu-chan!"
    ec "Ebola-chan is glad she has a friend like you!"
    ec "You're soooo reliable!"

    vc "Yeah, and you're so bloody virulant I'm suprised I haven't burst."


    show ebby normal

    vc "Ok there is this one place I 'erd of"
    vc "loads a humans"
    vc "they pack 'em into trains like sardines"
    vc "and stack 'em in buildings like waffles."

    vc "It's called {w=2.0}'Japan'...."

    scene bg black with fade
    jump Africa_Return