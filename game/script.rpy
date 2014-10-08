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

  scene bg hospital_beds3 with fade

  "I've been here... for too long."
  "I've forgotten my name..."
  "What was it again?"

  jump Name


label Name:

  # The phrase in the brackets is the text that the game will display to prompt 
  # the player to enter the name they've chosen.
  $ player_name = renpy.input("Please enter your name:")

  # The .strip() instruction removes any extra spaces the player 
  # may have typed by accident.
  $ player_name = player_name.strip()

  # If the player can't be bothered to choose a name, then we
  # choose a suitable one for them:
  if player_name == "":
    $ player_name="The Chosen One"
  
  # Now we can use the player's name.
  # confirm that the name is correct
  menu:

    "... My name is %(player_name)s.":

      jump Name_Confirmed

    "... No, that isn't my name.":

      jump Name

label Name_Confirmed:

  "Pleased to meet you, %(player_name)s!"

  jump Shrines
label Shrines_Return:

  jump Africa
label Africa_Return: 

    
    return
