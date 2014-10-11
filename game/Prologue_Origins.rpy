label Origins:

  scene bg black with fade

  centered "{i}Chapter 1, Origins{/i}"
  
  scene bg ebola_isolation_room with fade

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

  "Yes, I remember... my is, %(player_name)s!"
  
  "It all started a few months ago..."
  
  scene bg libereia_slums with fade
  
  "My father was a doctor."
  "He was in Liberia, trying to fight an Ebola outbreak."
  
  scene bg liberia_village with fade
  
  "But things didn't go well."
  "The small villages didn't listen."
  
  scene bg ebola_hazmat3 with fade
  
  "The outbreak spread."
  "The number of infected surpassed all estimates."
  
  scene bg ebola_hospital1 with fade
  
  "The hospitals were overwhelmed."
  "The virus was brutal, liquefying the organs of the infected."
  "There wasn't much that could be done."
  "The death rate was over 70 percent."

  scene bg ebola_bodybag2 with fade
  
  "The bodies accumulated quickly."
  "They were removed from the hospital as soon as possible."
  
  scene bg ebola_funeral2 with fade
  
  "The primitive burial practices of the natives didn't help matters."
  "They would kiss the deceased, getting infected themselves."
  
  scene bg ebola_funeral1 with fade
  
  "To prevent this the hospitals started to encase the victims bodies in concrete."
  "This angered the people."
  "It wasn't the way things were done there, it was viewed as sinful."
  
  scene bg ebola_hazmat2 with fade
  
  "The health care workers came under attack."
  "8 were murdered, their bodies discovered in a latrine."
  
  scene bg ebola_funeral3 with fade
  
  "The containment efforts failed."
  "Many health workers fled."
  "The deaths continued regardless."
  
  scene bg ebola_hazmat1 with fade
  
  "My father called to say that he was coming home."
  "He had enough, he did his part."
  
  scene bg ebola_funeral4 with fade
  
  "A few weeks ago he made his journey home."
  "All seemed well, he showed no symptoms."
  
  scene bg ebola_bodybag1 with fade
  
  "Little did he know that death was stalking him."
  "It would follow him home from Africa."
  
  scene bg black with fade
  return