# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
image bg black = Solid((0, 0, 0, 255))

image bg bg1 = "images/backgrounds/bg1.png"
image bg ashes = "images/backgrounds/tt2.png"

image tam1a = "images/sprites/tamamo_st01.png"
image tam1b = "images/sprites/tamamo_st01a.png"
image tam1c = "images/sprites/tamamo_st01b.png"
image tam1d = "images/sprites/tamamo_st01c.png"

image tam2a = "images/sprites/tamamo_st03a.png"
image tam2b = "images/sprites/tamamo_st03b.png"

image tam3a = "images/sprites/tamamo_st04a.png"
image tam3b = "images/sprites/tamamo_st04b.png"
image tam3c = "images/sprites/tamamo_st04c.png"

image ec1 = "images/sprites/ec1.png"
image ec2 = "images/sprites/ec2.png"
image ec3 = "images/sprites/ec3.png"
image ec4 = "images/sprites/ec4.png"
image ec5 = "images/sprites/ec5.png"
image ec6 = "images/sprites/ec6.png"
image ec7 = "images/sprites/ec7.png"

image ev = "images/sprites/v.png"

image ctc_tball = anim.Filmstrip("images/tballstrip3.png", (30,30), (8,1), 0.1, xpos=1840, ypos=1020, xanchor=0, yanchor=0)

define ec = Character(name='Ebola-chan', what_color="#fdb2b6", who_color="#000000", what_prefix='"', what_suffix='"')
define vc = Character(name='Vu-chan', what_color="#fdb2b6", who_color="#000000", what_prefix='"', what_suffix='"')
define narrator = Character(name=' ', what_color="#fdb2b6", who_color="#000000", what_prefix='"', what_suffix='"')
define centered = Character(name=' ', what_style="centered_text", window_style="centered_window")

# The game starts here.
label start:

    scene bg black with fade
    
    centered "{i}Maybe today...{/i}"
    
    centered "{i}Maybe in Africa...{/i}"
    
    scene bg bg1 with fade
    
    pause 1.0
    
    "Vu-chan!{w=1.5} Vu-chan!{p=1.5}
    Where are you Vu-chan?"

    show ec3:
        zoom 1.0
        xalign 0.1
        yalign 1.0
        
    ec "Vuuuu-chaaaan!!"
    
   
    show ev:
        zoom 1.0
        xalign 0.9
        yalign 1.0

    vc "Keep yer shimpan on dearie,{p=1.0}
    I'm here."

    hide ec3
    show ec6:
        zoom 1.0
        xalign 0.1
        yalign 1.0

    ec "Vu-chan! {w=1.0}Yay!"
    ec "It's gotten so quiet around here,"

    hide ec6
    show ec7:
        zoom 1.0
        xalign 0.1
        yalign 1.0

    ec "Ebola-chan was getting lonely!"

    vc "Of course it's quiet you puerile pestillance!{p=1.5}
    Everybody's dead!"

    hide ec7
    show ec2:
        zoom 1.0
        xalign 0.1
        yalign 1.0

    ec "Dead?"

    vc "Yes, Dead!{w=1.0} Expired!{w=1.5} Bereft of Life!{p=1.5}
    You've bled 'em all dry!"
    vc "Me and me mates 'ave been munching on 'em all morning!{p=1.5}
    Unless they can magically come back from a vultures lower intestine,{p=1.5}
    yes, they are all very much dead!"

    ec "But what will ebola-chan do?"
    ec "Ebola-chan doesn't want to be lonely!{p=1.5}
    She wants to play with more and more humans!"

    vc "Bloomin' eck you're voracious-virus!"
    vc "Don't you want to 'ave an after-epidemic nap or something?"

    hide ec2
    show ec4:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    ec "Ebola-chan doesn't want a nap!{p=1.5}
    Ebola-chan doesn't want to be lonely!"
 
    ec "Ebola-chan wants to PLAY!"

    vc "All right, all right, calm yer waterworks already.{p=1.5}
    I'll think of something."

    hide ec4

    show ec6:
        zoom 1.0
        xalign 0.1
        yalign 1.0

    ec "Yay! Vu-chan!{p=1.5}
    Ebola-chan is glad she has a friend like you!{p=1.5}
    You're soooo reliable!"

    vc "Yeah, and you're so bloody virulant I'm suprised I haven't burst."

    hide ec6
    show ec7:
        zoom 1.0
        xalign 0.1
        yalign 1.0

    vc "Ok there is this one place I 'erd of {p=1.5}
    loads a humans"
    vc "they pack 'em into trains like sardines{p=1.5}
    and stack 'em in buildings like waffles."


    vc "It's called {w=2.0}'Japan'...."

    scene bg black with fade
    
    
    

    
    
    
    return
