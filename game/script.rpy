# You can place the script of your game in this file.
# test for GitHub procedure, DevZero, this line can be removed later

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
image bg black = Solid((0, 0, 0, 255))

image bg bg1 = "images/backgrounds/bg1.png"
image bg ashes = "images/backgrounds/tt2.png"
image bg hospital_beds3 = "images/backgrounds/hospital_beds3.jpg"

image bg s01 = "images/backgrounds/shrines/shrine01.jpg"
image bg s02 = "images/backgrounds/shrines/shrine02.jpg"
image bg s03 = "images/backgrounds/shrines/shrine03.jpg"
image bg s04 = "images/backgrounds/shrines/shrine04.jpg"
image bg s05 = "images/backgrounds/shrines/shrine05.jpg"
image bg s06 = "images/backgrounds/shrines/shrine06.jpg"
image bg s07 = "images/backgrounds/shrines/shrine07.jpg"
image bg s08 = "images/backgrounds/shrines/shrine08.jpg"
image bg s09 = "images/backgrounds/shrines/shrine09.jpg"
image bg s10 = "images/backgrounds/shrines/shrine10.jpg"
image bg s11 = "images/backgrounds/shrines/shrine11.jpg"
image bg s12 = "images/backgrounds/shrines/shrine12.jpg"
image bg s13 = "images/backgrounds/shrines/shrine13.jpg"
image bg s14 = "images/backgrounds/shrines/shrine14.jpg"
image bg s15 = "images/backgrounds/shrines/shrine15.jpg"
image bg s16 = "images/backgrounds/shrines/shrine16.jpg"
image bg s17 = "images/backgrounds/shrines/shrine17.jpg"
image bg s18 = "images/backgrounds/shrines/shrine18.jpg"
image bg s19 = "images/backgrounds/shrines/shrine19.jpg"
image bg s20 = "images/backgrounds/shrines/shrine20.jpg"
image bg s21 = "images/backgrounds/shrines/shrine21.jpg"
image bg s22 = "images/backgrounds/shrines/shrine22.jpg"
image bg s23 = "images/backgrounds/shrines/shrine23.jpg"
image bg s24 = "images/backgrounds/shrines/shrine24.jpg"
image bg s25 = "images/backgrounds/shrines/shrine25.jpg"
image bg s26 = "images/backgrounds/shrines/shrine26.jpg"
image bg s27 = "images/backgrounds/shrines/shrine27.jpg"
image bg s28 = "images/backgrounds/shrines/shrine28.jpg"
image bg s29 = "images/backgrounds/shrines/shrine29.jpg"
image bg s30 = "images/backgrounds/shrines/shrine30.jpg"
image bg s31 = "images/backgrounds/shrines/shrine31.jpg"
image bg s32 = "images/backgrounds/shrines/shrine32.jpg"
image bg s33 = "images/backgrounds/shrines/shrine33.jpg"
image bg s34 = "images/backgrounds/shrines/shrine34.jpg"
image bg s35 = "images/backgrounds/shrines/shrine35.jpg"
image bg s36 = "images/backgrounds/shrines/shrine36.jpg"
image bg s37 = "images/backgrounds/shrines/shrine37.jpg"
image bg s38 = "images/backgrounds/shrines/shrine38.jpg"
image bg s39 = "images/backgrounds/shrines/shrine39.jpg"
image bg s40 = "images/backgrounds/shrines/shrine40.jpg"
image bg s41 = "images/backgrounds/shrines/shrine41.jpg"
image bg s42 = "images/backgrounds/shrines/shrine42.jpg"
image bg s43 = "images/backgrounds/shrines/shrine43.jpg"
image bg s44 = "images/backgrounds/shrines/shrine44.jpg"
image bg s45 = "images/backgrounds/shrines/shrine45.jpg"
image bg s46 = "images/backgrounds/shrines/shrine46.jpg"
image bg s47 = "images/backgrounds/shrines/shrine47.jpg"
image bg s48 = "images/backgrounds/shrines/shrine48.jpg"
image bg s49 = "images/backgrounds/shrines/shrine49.jpg"
image bg s50 = "images/backgrounds/shrines/shrine50.jpg"
image bg s51 = "images/backgrounds/shrines/shrine51.jpg"
image bg s52 = "images/backgrounds/shrines/shrine52.jpg"
image bg s53 = "images/backgrounds/shrines/shrine53.jpg"
image bg s54 = "images/backgrounds/shrines/shrine54.jpg"
image bg s55 = "images/backgrounds/shrines/shrine55.jpg"

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


  jump Shrines
  jump Africa




label Shrines:
  scene bg black with fade
  centered "{i}TRIGGER WARNING{/i}"
  centered "{i}This is the Occult{/i}"
  centered "{i}Some images may be disturbing{/i}"

  $renpy.music.set_volume (1.0, channel="music")
  play music "O_Fortuna.mp3" noloop

  scene bg s01
  pause(2)
  scene bg s02
  pause(2)
  scene bg s03
  pause(2)
  scene bg s04
  pause(2)
  scene bg s05
  pause(2)
  scene bg s06
  pause(2)
  scene bg s07
  pause(2)
  scene bg s08
  pause(2)
  scene bg s09
  pause(2)
  scene bg s10
  pause(2)
  scene bg s11
  pause(2)
  scene bg s12
  pause(2)
  scene bg s13
  pause(2)
  scene bg s14
  pause(2)
  scene bg s15
  pause(2)
  scene bg s16
  pause(2)
  scene bg s17
  pause(2)
  scene bg s18
  pause(2)
  scene bg s19
  pause(2)
  scene bg s20
  pause(2)
  scene bg s21
  pause(2)
  scene bg s22
  pause(2)
  scene bg s23
  pause(2)
  scene bg s24
  pause(2)
  scene bg s25
  pause(2)
  scene bg s26
  pause(2)
  scene bg s27
  pause(2)
  scene bg s28
  pause(2)
  scene bg s29
  pause(2)
  scene bg s30
  pause(2)
  scene bg s31
  pause(2)
  scene bg s32
  pause(2)
  scene bg s33
  pause(2)
  scene bg s34
  pause(2)
  scene bg s35
  pause(2)
  scene bg s36
  pause(2)
  scene bg s37
  pause(2)
  scene bg s38
  pause(2)
  scene bg s39
  pause(2)
  scene bg s40
  pause(2)
  scene bg s41
  pause(2)
  scene bg s42
  pause(2)
  scene bg s43
  pause(2)
  scene bg s44
  pause(2)
  scene bg s45
  pause(2)
  scene bg s46
  pause(2)
  scene bg s47
  pause(2)
  scene bg s48
  pause(2)
  scene bg s49
  pause(2)
  scene bg s50
  pause(2)
  scene bg s51
  pause(2)
  scene bg s52
  pause(2)
  scene bg s53
  pause(2)
  scene bg s54
  pause(2)
  scene bg s55
  pause(4)

  stop music

  jump Africa




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
    
    return
