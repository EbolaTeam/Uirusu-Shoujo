label roisaber:

  $route=""

  # Scene: inside Protag-kun bedroom, early morning
  scene bg xebdorm_room with fade
 
  "You wake up just before dawn, but something seems wrong."
  "You can hear loud voices shouting angrily just outside the compound, and the air carries the acrid tang of heavy smoke."
 
  # Protagonist is nn
  nn "What's... what's going on?"
 
  # Scene: Clinic hallway. 
  scene bg hospital_beds3 with fade
  # WHO-chan scared sprite
  show who normal at right
 
  wc "Oh! Thank heavens you're alright!"
  nn "What's happening?"
  wc "It's the locals! They're protesting the clinic!"
  nn "But why would they be doing that? Don't they know we're here to help?"
  wc "They're blaming us for spreading the diseases. I'm going to go check on Z-MAPP-chan! You wait here!"

  # WHO-chan shifts offscreen.
  show who normal slideawayleft

  menu:
    "What should I do?"

    "Check on Ebola-chan":
        $route="A1"
    "Check on Marbug-sama":
        $route="B1"
    "Wait for WHO-chan":
        $route="C1"

  $renpy.call(route)

label A1:
  # Scene: 2nd hospital corridor. Door knocking sound
  scene bg hospital_beds3 with fade

  nn "Hey, Ebola-chan, wake up!"

  #Door open sound, sleepy Ebola-chan sprite.
  show ebby concerned at left

  ec "*yawn* Spreading love is exhausting work. What'd you wake me up for, anyway?"
  nn "The clinic might be under attack! We've got to get you to safety."
  ec "Aww, are you 'warming' up to me already? I thought you were trying to get rid of me."

  menu:
    "What should I do?"

    "Be decisive":
        $route="A1A"
    "Be irritated":
        $route="A1B"
    "Be compromising":
        $route="A1C"

  $renpy.call(route)

label A1A:
  nn "There's no time to argue! Let's get down to the laboratory; we should be safe there."
  # Small happy sound + small Ebola-chan bonus
  ec "Fine, fine. Let's get down to the laboratory."
  jump UndergroundLab
  
label A1B:
  nn "I don't have time for your stupid games! Just follow me, and don't cause any more trouble!"
  # Small sad sound + small Ebola-chan penalty
  ec "Fine, fine. Let's get down to the laboratory."
  jump UndergroundLab
  
label A1C:
  nn "Vector is waiting for you downstairs. I'm sure he'd be overjoyed to see you."
  # Medium happy sound + medium Ebola-chan bonus
  ec "Fine, fine. Let's get down to the laboratory."
  jump UndergroundLab

label B1:
  # Scene: 2nd hospital corridor. Door knocking sound
  scene bg xebcorridor with fade

  nn "Hey, Marburg-sama, wake up! It's an emergency!"

  # Door open sound, normal Marbug-sama sprite.
  show marburg normal at right
  
  marburg "What's going on?"
  nn "The clinic is under attack. Let's hurry up and get downstairs where we'll be safe!"
  #Sword sound, angry Marburg-sama sprite.
  show marburg rape at right
  
  marburg "Fleeing will not be necessary. Just leave the security of this clinic to me."

  menu:
    "What should I do?"

    "Be decisive":
        $route="B1A"
    "Be obsequious":
        $route="B1B"
    "Be compassionate":
        $route="B1C"

  $renpy.call(route)

label B1A:
  nn "No! We're trying to help these people, not hurt them. Just follow me to the laboratory; we'll be safe down there."
  # Sword sheath noise
  show marburg annoyed at right
  marburg "Very well. Just don't expect me to forget this."
  # Small happy sound, small Marbug-sama bonus
  nn "Come on, let's hurry!"
  jump UndergroundLab
  
label B1B:
  nn "Marburg-sama, it's more important to protect your friends than attack your enemies! The equipment in this clinic can be replaced, but the people we love are irreplaceable."
  nn "Please follow me to the laboratory. You can't do anything if you're dead."
  # Sword sheath noise
  show marburg annoyed at right
  marburg "I'll agree to it just this once. Next time, we try it my way."
  # Small unhappy sound, small Marbug-sama penalty
  nn "Come on, let's hurry!"
  jump UndergroundLab
  
label B1C:
  nn "Marburg-sama, I know it's not easy to put yourself aside for others, but that's how you learn if you're truly strong!"
  nn "Let's make sure that everyone gets downstairs safely. If you fight now, you'll never know how strong you can really become."
  # Sword sheath noise
  show marburg annoyed at right
  marburg "*sigh* Fine. I'd rather fight at a time and place of my own choosing, anyway."
  # Medium happy sound, medium Marbug-sama bonus
  nn "Come on, let's hurry!"
  jump UndergroundLab
   
label C1:
  # Scene: 2nd hospital corridor.
  scene bg xebcorridor with fade  
  # Loud crash from somewhere
 
  nn "Geeze... I hope WHO-chan gets back soon. This is getting ridiculous."
  # Worried WHO-chan sprite slides into screen
  show who concerned at right
  wc "You waited for me!"
 
  menu:
    "What should I do?"

    "Be flirtatious":
        $route="C1A"
    "Be brave":
        $route="C1B"
    "Be professional":
        $route="C1C"

  $renpy.call(route)
  
label C1A:
  nn "Of course I did! I could never leave a pretty girl like you all alone."
  # WHO-chan blush sprite
  show who joy at right
  # small happy sound, small WHO-chan bonus
  wc "You sound like a character from a bad visual novel." 
  # WHO-chan determined sprite.
  show who normal at right  
  wc "Come on, we have work to do!"
  jump UndergroundLab
  
label C1B:
  nn "Of course I did! I had to make sure you got downstairs safely."
  wc "Oh! Thank you, Protagonist-kun."
  # WHO-chan happy sprite
  show who joy at right
  # medium happy sound, medium WHO-chan bonus
  nn "Is everyone downstairs yet?"
  wc "Yes, everyone's fine. Come on, let's hurry up and join them!"
  jump UndergroundLab
  
label C1C:
  nn "Of course I did, Miss Director. I want you to know you can always trust me to follow your orders."
  # WHO-chan distracted/uneasy sprite
  
  # small unhappy sound, small WHO-chan penalty
  wc "Oh, I see. Well, that's very helpful of you. It's good to know I have someone I can depend on."
  # WHO-chan determined sprite.
  show who normal at right
  wc "Come on, we have work to do!"
  jump UndergroundLab


label UndergroundLab:
  # Scene: Underground laboratory
  scene bg xebriver with fade 
  
  wc "Okay, everyone's in side! Protag-kun, hurry up and shut the door!"
  #Heavy door close sound.
  wc "Good, that should keep us safe from the rioters. The laboratory has been reinforced to Level V secure facility standards."
  #Loud crash sound
  wc "Of course, that won't protect our equipment in the clinic above..."
  show marburg normal at right
  marburg "Look at them! They're all bunched up and their flanks are totally exposed. What a bunch of amateurs!"
  marburg "I'll bet I could kill half of them with one well-placed mortar shell..."
  # WHO-chan shocked sprite
  show who suprised at center
  wc "A-a-a-absolutely not! We're here to help these people, not hurt them."
  # Ebola-chan akanbe sprite
  show ebby wink at left
  ec "Speak for yourself, WHO-sama."
  wc "I told you not to call me that!"
  # Z-MAPP-chan sprite from left.
  show zmapp normal at left
  zmapp "WHO-chan, I estimate I possess a 12.3 percent chance of eliminating these miscreants immediately. Of course, I would be destroyed in the process, but that seems like an acceptable sacrifice to keep them from spreading further."
  wc "Nobody is sacrificing anything! Ugh, why don't you all shut up and let me think!"
  # Tick-tock sound
  # Bing sound
  show who joy at center
  wc "I've got it! I'll just call the police."
  # All others sweatdrop sprite
  # Phone sound
  wc "Hello, police? I'm calling from the World Health Organization Reconnaissance and Eradication Squad. That's right, W.H.O.R.E.S.. What? Look I didn't decide on the acronym, okay!? Stop laughing! We have a real emergency on our hands here."
  ec "Stop taking things so seriously, WHO-sama."
  wc "You shut up! No, not you officer. No please, look, there's a riot at our facility! If you don't send help right away, the rioters might destroy the whole clinic."
  wc "Not only would that set our efforts to eradicate these diseases back by six months, but it would be a public relations disaster for Equatorial Leone on the world stage!"
  # Loud crash sound
  wc "Well, as soon as you can!"
  # Phone hangup noise
  wc "Whew. The police are on their way."
  marburg "What a pity. I was hoping to get a chance to try out my new mutation."
  show who angry at center
  wc "Don't you have any sense of decorum?! We wouldn't even have to fight at all if you could just live with the human race peacefully. Why can't you be more like your cousin, Lactobacillus-san? He's been helping us digest food for thousands of years."
  marburg "I'm only acting out my metabolic destiny. It's not my fault that humans are so weak."
  # Ebola-chan hugging Vector sprite
  show ebby joy at left
  ec "And I'm only trying to fill the world with LOVE!"
  # Loud crash sound
  # Devastated WHO-chan sprite
  show who suprised at center
  wc "How did this happen to me? Go to med school, they said. It'll be great, they promised. I'd drive a Lexus home from the office every day to my big house, where I could relax in an Olympic-sized swimming pool and think about retiring at age 30..."

  menu:
    "What should I do?"

    "Comfort Ebola-chan":
        $route="D1"
    "Comfort Marburg-sama":
        $route="D2"
    "Comfort WHO-chan":
        $route="D3"

  $renpy.call(route)
  
label D1:
  nn "I know that the human race would be happy to live side-by-side with you, Ebola-chan; you just have to learn to change your approach."
  show ebby sad at left
  ec "All I ever wanted was to share my LOVE with the world. Why does everyone fight me so hard?"
  nn "It's okay, Ebola-chan. I'll help you show people the kind, gentle goddess behind your fearsome exterior. You've just got to let me treat you."
  show ebby joy at left
  # small happy noise, small Ebola-chan bonus
  jump UndergroundLab2
  
label D2:
  nn "Don't listen to her, she's just bitter that she didn't marry a lawyer when she was still an undergraduate."
  wc "Hey! That's rude!"
  nn "If you really put your mind to it, I know you could find a place in this world, Marburg-sama."
  # Marburg-sama angry sprite
  show margburg annoyed at right
  marburg "I don't need your pity."
  # Small unhappy sound, small Marbug-sama penalty
  jump UndergroundLab2
  
label D3:
  nn "There, there, WHO-chan. You're helping people, and isn't that worth more than the nicest car or the biggest mansion? You should live life without regrets!"
  wc "That's nice of you to say, but do you know that I haven't even had a slice of pizza since I got here. Two years! Two years in this stupid clinic and I feel like I haven't accomplished a thing."
  show ebby sad at left
  nn "I think you've done a lot here at W.H.O.R.E.S."
  show who angry at center
  show ebby rape at left with Pause(2)
  # then laughing WHO-chan sprite
  show who joy at center
  wc "Thanks for trying anyway, Protag-kun."
  # Small happy sound, small WHO-chan bonus
  jump UndergroundLab2

label UndergroundLab2:
 
  show zmapp normal at right
  zmapp "My long range sensors are detecting approaching sirens. I believe the police will soon be here to disperse the rioters."
  # Loud crash
  wc "It couldn't happen a moment too soon. Okay, let's just sit tight until they get the clinic cleared out."
 
  # Scene: destroyed treatment room
  scene bg ebola_bodybag1 with fade 
  show who angry at center
  wc "I can't believe this! They destroyed thousands of dollars of equipment! I'll never get the World Health Organization to give me the necessary funding to replace all this! It's going to come out of my salary..."
  show marburg normal at right
  marburg "What a bunch of primitives. No wonder they can't stand their ground against me."
  show ebby joy at left
  ec "That's okay, Oni-sama! That just means that WHO-chan is farther than ever from finding a cure for us!"

jump start