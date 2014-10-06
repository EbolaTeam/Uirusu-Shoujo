# You can place the script of your game in this file.
# test for GitHub procedure, DevZero, this line can be removed later

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
image bg black = Solid((0, 0, 0, 255))

image bg bg1 = "images/backgrounds/bg1.png"
image bg ashes = "images/backgrounds/tt2.png"
image bg hospital_beds3 = "images/backgrounds/hospital_beds3.jpg"

image ebby wink = "images/sprites/EbbyWink.png"
image ebby concerned= "images/sprites/EbbyConcerned.png"
image ebby excited = "images/sprites/EbbyExcited.png"
image ebby sad= "images/sprites/EbbySad.png"
image ebby rape= "images/sprites/EbbyRape.png"
image ebby joy= "images/sprites/EbbyJoy.png"
image ebby normal = "images/sprites/EbbyNormal.png"

image vu normal = "images/sprites/VuNormal.png"

image ctc_tball = anim.Filmstrip("images/tballstrip3.png", (30,30), (8,1), 0.1, xpos=1840, ypos=1020, xanchor=0, yanchor=0)

define ec = Character(name='Ebola-chan', what_color="#fdb2b6", who_color="#000000", what_prefix='"', what_suffix='"')
define vc = Character(name='Vu-chan', what_color="#fdb2b6", who_color="#000000", what_prefix='"', what_suffix='"')
define narrator = Character(name=' ', what_color="#fdb2b6", who_color="#000000", what_prefix='"', what_suffix='"')
define centered = Character(name=' ', what_style="centered_text", window_style="centered_window")

# The game starts here.
label start:

  jump Name




label Name:

  scene bg hospital_beds3 with fade

  "I've been here... for too long."
  "I've forgotten my name..."
  "What was it again?"

# The phrase in the brackets is the text that the game will display to prompt 
# the player to enter the name they've chosen.

  $ player_name = renpy.input("What is your name?")

  $ player_name = player_name.strip()

# The .strip() instruction removes any extra spaces the player 
# may have typed by accident.

#  If the player can't be bothered to choose a name, then we
#  choose a suitable one for them:
  if player_name == "":
    $ player_name="The Chosen One"
  
# Now we can use the player's name.
  
  "Pleased to meet you, %(player_name)s!"

  jump Africa




label Africa:

    scene bg black with fade
    
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
    
    return
