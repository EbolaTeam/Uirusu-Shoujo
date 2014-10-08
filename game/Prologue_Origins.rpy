label Origins:

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

  jump Origins_Return