label roisaber:

  $route=""
  $stay_flag = 0
  $who_affection = 0

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
  show who normal at right

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
  wc "You two... this is all your fault!"

  menu:
    "What should I do?"

    "Agree with WHO-chan":
        $route="E1"
    "Disagree with WHO-chan":
        $route="E2"

  $renpy.call(route)
  
label E1:
  nn "If you two would just learn to get along with humanity, we could let you guys outside the compound!"
  show ebby sad at left
  ec "I didn't do anything wrong. I just wanted to share my LOVE with the world."
  show marburg annoyed at right
  marburg "Don't blame me for the failings of your own species."
  # Medium unhappy sound + medium Marburg-sama penalty
  jump Biohazard_quarantine_door

label E2:
  nn "This isn't their fault, WHO-chan, and it isn't your fault either. This is the fault of the rioters who allowed themselves to be controlled by fear. Rebuilding is going to be a lot of work, but let's not give up so easily!"
  # Ebola-chan akanbe sprite
  show ebby wink at left
  ec "That's right! You've got another thirty years of failure ahead of you."
  # Angry WHO-chan sprite
  show ebby concerned at left
  wc "What do you mean, another!? I'm only twenty four!"
  # Small unhappy sound + small WHO-chan penalty
  jump Biohazard_quarantine_door

label Biohazard_quarantine_door:
  wc "Sigh. Just make sure the facility doors are sealed, Protag-kun. We don't need these two escaping and causing any more trouble than they already are."
 
  #Scene: Biohazard quarantine door
  scene bg hospital_beds3 with fade

  nn "Well, at least the door still closes securely. I hope nobody from the town picked up any viruses while they were busy smashing our equipment."
  #'Seductive' Marburg-sama sprite
  marburg "Hey, lover. What do you think about giving me the code to the door?"
  # Sweatdrop Protag-kun sprite
  nn "Wh-what!? No way! Marburg-sama, you know you're not supposed to be lurking over here."
  marburg "*sigh* You have no right to keep me as a prisoner here."
  nn "But - you kill people!"
  marburg "So? You kill cows and chickens, don't you? I have just as much right to live in this world as you do."
  nn "That's... different."
  marburg "It is? Why?"
  nn "Because human beings matter more than chickens and cows!"
  marburg "Who decided that? Human beings, right?"
  nn "What are you trying to say, Marburg-sama?"
  # Sword draw sound
  # angry Marburg-sama sprite
  show marburg annoyed at right
  marburg "I'm saying you'd better get out of my way, or I'll have to go through you!"
 
  menu:
    "What should I do?"

    "Be conciliatory":
        $route="F1"
    "Be flirtatious":
        $route="F2"
    "Be defiant":
        $route="F3"

  $renpy.call(route)
 
label F1:
  nn "I know it's hard for you to be cooped up in this facility all the time. But we're doing it for the good of everyone, you included! If we can find a vaccine for you, then we won't have to keep you contained any more. In fact, we'll need to have you around so that we're able to keep manufacturing the vaccine!"
  marburg "Why should I help an idiot like you?"
  nn "Don't help me, Marburg-sama. Help yourself by learning how to work with other people."
  # Sword sheath noise. Small happy sound, small Marburg-sama bonus
  marburg "I can buy myself more time by escaping when no one's looking..."
  # Marburg-sama sprite goes offscreen, relieved Protag-kun sprite
  nn "That was too close..."
  jump Destroyed_treatment_room

label F2:
  nn "But Marburg-sama, this place would be intolerable without seeing your lovely face every day!"
  # Medium unhappy sound, medium Marburg-sama penalty
  marburg "You idiot. Did you really think I would fall for such a cheesy line?"
  nn "I... uh..."
  marburg "I'll be back. Sooner or later you'll let your guard down, and when you do, just remember who it was that defeated you."
  # Sword sheath sound. Marburg-sama sprite goes offscreen
  nn "Is she serious? I'd better watch my back..."
  jump Destroyed_treatment_room

label F3:
  nn "I'm not letting you out of this facility! Even if I have to lay down my life, I'll protect the people of this world!"
  # Medium happy sound, medium Marburg-sama bonus, happy Marburg sprite
  marburg "Seriously? Baka... fine, you win this round. After all, you have to sleep sometime..."
  # Marburg-sama sprite goes offscreen.
  nn "Whew! That was way too close..."
  jump Destroyed_treatment_room

label Destroyed_treatment_room:
  nn "I'd better go check up on WHO-chan and make sure everything's okay back in the treatment room."

  # Scene: Destroyed treatment room
  scene bg hospital_beds3 with fade
  show zmapp normal at center
  nn "Hey, ZMAPP-chan. Where's WHO-chan?"
  zmapp "My sensors are picking her up in her office. She appears to be on the phone with the World Health Organization. She's also crying. Would you like me to repeat their conversation for you?"
  nn "Uh, no... thank you... that won't be necessary. What are you doing here?"
  zmapp "Per WHO-chan's orders, I am sterilizing and disposing of all potentially biohazardous material in the treatment room. Do you wish to add an additional task to my queue?"
  nn "No, you're doing more than enough already."

  menu:
    "What should I do?"

    "Don't offer to help":
        $route="G1"
    "Offer to help":
        $route="G2"

  $renpy.call(route)

label G1:
  # Don't offer to help
  jump lab_teamwork

label G2:
  nn "Could you use a hand, ZMAPP-chan?"
  zmapp "I estimate I would be 21.6%% more efficient with an additional appendage. What time should I schedule the surgery?"
  nn "That's... not what I meant! I'm asking you if you want any help cleaning the room."
  zmapp "Oh. You would not hinder my progress."
  "Does that mean yes...?"
  # Sound of stacking or cleaning (somehow? Like the sound of broken glass being set down in a box?)
  nn "Are you upset or anything? I mean, the riot must have frightened you, right?"
  zmapp "I don't think so. What do you mean by fear?"
  # More stacking/cleaning sound
  nn "Well, fear is when your heart starts beating faster, and your breaths come shorter and shallower, and your stomach muscles tighten, and you can feel a surge of adrenaline in your bloodstream..."
  zmapp "Really? That sounds complicated. How do you humans manage to experience so many different feelings at once?"
  nn "Ugh. It's hard to explain. I have an idea! Tell me how that flask you're picking up feels."
  # ZMAPP-chan pensive sprite
  zmapp "Well, it's cool to the touch, and the surface is very smooth."
  nn "Compare that feeling to something."
  zmapp "It feels like glass."
  nn "No, compare it to something different from what it is! Compare it to something like the night sky or the ocean!"
  zmapp "I do not understand. The feeling of glass is like... the appearance of a duck's bill on the third Saturday of the month when the moon is full and three birds are chirping 250 degrees to my rear."
  # Protag-kun long sweatdrop sprite
  nn "That's... great, ZMAPP-chan. I think you're on your way to getting it."
  # Protag-kun neutral sprite
  # ZMAPP-chan happy sprite
  zmapp "Will this improve my efficiency in combating the viruses?"
  nn "...Probably?"
  # Medium happy sound, medium ZMAPP-chan bonus
  zmapp "That is excellent to hear."
  nn "Does that make you happy?"
  zmapp "Happy...."
  jump lab_teamwork

label lab_teamwork: 

  # Loud door sound
 
  wc "Okay everyone, huddle up!"
  # Grumble sound, all neutral sprites on screen
  wc "I've got good news and bad news. The good news is, the World Health Organization has agreed to send us an emergency shipment of replacement supplies. Of course, we won't be able to operate at full capacity for several months, but we'll still be able to treat patients in the interim with the supplies they're dispatching from regional HQ."
  nn "What's the bad news?"
  show who sad at center
  wc "They said my yearly bonus is going to be folded into the clinic's operating expenses for the next three years..."
  # Determined WHO-chan sprite
  show who excited at center
  wc "But that's no excuse to give up!"
  show ebby joy at left
  ec "Are you sure? This is the perfect opportunity to usher in a new paradise full of peace and LOVE!?"
  # WHO-chan sprite shakes
  wc "Get... her... out of here... before... I... strangle... her..."
  show who normal at center
  nn "So, what's next?"
  wc "Let's get this place cleaned up and ready for new patients. The chief of police said he'd station a guard outside around the clock, so hopefully we won't run into any more problems with angry locals."
  # WHO-chan determined sprite
  wc "Alright everyone, let's get to work! And that includes you virus girls too."
  show marburg annoyed at right
  marburg "Me? Why should I have to do anything?"
  ec "Yeah! You've been trying to cure us this whole time! Why should we help you?"
  # Furious WHO-chan sprite
  show who angry at center
  wc "I swear if you two don't start helping out I'll stick you both in a vial and lock you in the freezer!"
  # Scared/shivering Ebola-chan sprite
  show ebby sad at left
  ec "S-s-s-so cold."
  marburg "And scary."
  # Threatening ZMAPP-chan sprite
  show zmapp normal at center
  zmapp "You heard the Director! Everyone get to work!"

  
  # Start WHO-chan ending
  # WHO-chan Romance Scene
  scene bg hospital_beds3 with fade
 
  # Location: 2nd hospital corridor
 
  # WHO-chan sprite enters screen
  show who normal at center
  wc "Hey, Protag-kun, do you have some time?"
  nn "I was just on my way to fill out the last of the closure paperwork. What do you need?"
  # Nervous WHO-chan sprite
  show who shy at center
  wc "I was actually wondering if you wanted to come back to my room and get a drink."
  nn "You've got alcohol?"
  show who annoyed at center
  wc "I am an adult, you know! I've just been hiding it from all the other girls so they don't drink all of it. I guess it doesn't really matter, now..."
  nn "You miss them, don't you?"
  wc "I know the world is better off without them, but I can't pretend I'm not a little lonely now that they're gone. This place used to be so lively, but now we're closing down."
  nn "Now you can go back to the States and earn your Lexus and a big mansion!"
  wc "I guess so... well, are you coming, or not?"
 
  menu:
    "What should I do?"

    "Brush her off":
        $route="H1"
    "Kiss her":
        $route="H2"

  $renpy.call(route)
 
label H1:
  nn "Sorry, but I really have to get this paperwork done. My flight leaves tomorrow at noon, and if I miss it, it'll be another five days before I can get another connection to Brussels."
  wc "Oh... okay, I understand. Well, it's been great working with you, Protag-kun. We saved the world and we're probably the only people who will ever know it or care."
  nn "It's been an honor."
 
  # Scene: Protag-kun poring over paperwork late into the night
  # Scene: Protag-kun in airplane looking down on the African coast
  # Scene: Protag-kun back in the states, tired but relieved
 
  jump Credits
 
label H2:
 
  wc "Mmph...!? ....Mmm...."
  nn "S-s-sorry! I didn't mean to -"
  # WHO-chan kiss back sprite?
  show who kiss at center
  # Scene: WHO-chan bedroom
 
  nn "Yikes! You weren't kidding about the alcohol collection, were you?"
  wc "What!? Is there something wrong if a girl likes to have a drink after work?"
  nn "Of course not... I just didn't imagine you to be the type."
  wc "There's a lot you don't know about me."
  nn "There's a lot I'd like to learn about you."
  # Laughing WHO-chan sprite
  show who joy at center
  wc "You really are a total goof."
  # Serious WHO-chan sprite
  show who rape at center
  wc "So, what do you want to drink?"
 
  menu:
    "What should I drink?"

    "Water":
        $route="J1"
    "Vodka":
        $route="J2"
    "Gin":
        $route="J3"
    "Whiskey":
        $route="J4"

  $renpy.call(route)
  
label J1:
  nn "Just a glass of water, please."
  wc "Water!? Are you crazy!? You're still willing to drink the water here after everything that happened? You'd better make another choice before I get mad."

  menu:
    "What should I drink?"

    "Vodka":
        $route="J2"
    "Gin":
        $route="J3"
    "Whiskey":
        $route="J4"

  $renpy.call(route)
 
label J2:
  nn "I'll take a vodka rocks."
  wc "Sorry, I don't have any ice. Warm vodka tastes like the Devil's armpit so try again."
  
  menu:
    "What should I drink?"

    "Gin":
        $route="J3"
    "Whiskey":
        $route="J4"

  $renpy.call(route)
 
label J3:
  nn "I'd like a gin and tonic please."
  wc "Sorry Protag-kun, no tonic."
  nn "How about a martini?"
  wc "Uh... about that..."
  nn "What?"
  wc "I drank all the vermouth one night. I'm all out."
  nn "You drank straight vermouth?"
  wc "I'm not proud of all my life choices, alright! Anyway, you'll have to pick something else."

  menu:
    "What should I drink?"

    "Whiskey":
        $route="J4"
    "Whiskey":
        $route="J4"
    "Whiskey":
        $route="J4"

  $renpy.call(route)
 
label J4:
  nn "How about a glass of whiskey?"
  wc "Ahh, whiskey, the drink of sophisticates. I knew you'd make the right choice."
  # Pouring sound, tinkle
  nn "So what are you planning to do next?"
  wc "You know, I honestly don't know. I was hoping that a drink and a conversation with a good friend would help sort me out."
  nn "Well, what is your heart telling you?"
  wc "You know you talk like a total dork, right?"
  # Protag-kun sweatdrop sprite
  wc "But I think it's cute."
  # Happy WHO-chan sprite, happy Protag-kun sprite
  show who joy at center
  wc "I guess I should probably return to the States and take up a normal practice like I planned all along. But you know, despite everything, this place has kind of grown on me. Sure it's hot and humid and the people here can be totally crazy, but it feels like every day is a new adventure. If I went back home now, I would always wonder what I missed if I stayed. My head is telling me to do the smart thing, and my heart is telling me to do the exciting thing. What do you think I should do?"
 
  menu:
    "What should I do?"

    "Be rational":
        $route="K1"
    "Be spontaneous":
        $route="K2"

  $renpy.call(route)
 
label K1:
  nn "You should probably return to the States. You're not going to be young forever, and if you stay here in Equatorial Leone, it'll be hard to save up enough money to retire someday and take care of yourself in old age."
  wc "I suppose you're right."
  show who sad at center 
  # small unhappy sound, small WHO-chan penalty
  $stay_flag = 0
 
label K2:
  nn "The most important thing in life is doing what you believe in! If you really want to stay, you should stay. It's not as if spending another year or two in Equatorial Leone would keep you from doing other things in the future, right?"
  wc "You're right, Protag-kun!"
  show who joy at center 
  # small happy sound, small WHO-chan bonus
  $stay_flag = 1
 
  nn "H-hey! There's no need to pour so much!"
  # Tinkle noise
  nn "Not more for me, too..."
  wc "Drink up! It'll put hair on your chest!"
  nn "I'm not sure I need-"
  wc "I said drink up!"
  nn "*sigh* There's just no arguing with her when she's like this..."
 
  # Scene WHO-chan's room, later
 
  wc "Hic!"
  nn "WHO-chan, I think you've had enough."


  # Route 1: Not enough points to romance WHO-chan
 
  wc "Yeah, I guess you're right. I'm totally exhausted."
  nn "And more than a little drunk..."
  wc "What was that!?"
  nn "Oh, nothing!"
  wc "Well, it was nice knowing you, Protag-kun. It'll be awfully lonely with both you and the girls gone, but sooner or later I just know I'll find the right person for me. Hic! Go to bed, and I'll drive you hic! to the airport first thing in the morning."
  nn "Thanks, WHO-chan."
  # Scene: WHO-chan driving a jeep like a maniac and terrifying Protag-kun
  # Scene: Protag-kun in airplane looking down on the African coast
  # Scene: Protag-kun back in the states, tired but relieved
  jump Credits
 
  # Route 2: Enough points to romance WHO-chan
  wc "Enough? Enough?! I'll tell enough when I've had you!"
  # Blushing WHO-chan sprite
  show who shy at center
  wc "You're such a pain, Protag-kun."
  nn "Hey, what did I do?"
  show who angry at center
  wc "I'm going to ask you a question, and you'd better answer honestly!"
  nn "What's with you all of a sudden?"
  wc "Do you like me?"
  nn "Like you?"
  wc "That's right! Do you like me? Like, like like me?"
 
  menu:
    "What should I say?"

    "Say no":
        $route="L1"
    "Say yes":
        $route="L2"

  $renpy.call(route)
 
label L1:
 
  nn "Sorry. You're just not my type."
  wc "What!? Seriously!? After leading me on all this time? You're the worst, Protag-kun. Get out of here! I don't ever want to see your face again!"
  # Scene: Protag-kun fleeing an angry WHO-chan throwing a bottle
  # Scene: Protag-kun in airplane looking down on the African coast
  # Scene: Protag-kun back in the states, tired but relieved
 
  jump Credits

label L2:

  nn "Of course I do!"
  wc "Wait, really?"
  nn "I think you're amazing! You're studious, hardworking, honest, and beautiful."
  # Blush WHO-chan sprite
  show who shy at center
  wc "You really think I'm pretty?"
  nn "I do!"
  wc "I guess you're not so bad yourself. You know, it's really warm in here... I wonder if the air conditioning is on the fritz again."
  nn "Hey, what are you doing with your shirt!?"
  show who kiss at center
  wc "Well, it's not my fault if the tropical heat is getting to my head."
  nn "WHO-chan..."
 
  # ROMANCE STUFF
 
  # Scene: Next morning. 
  # Underwear WHO-chan sprite
  show who pantsu at center
 
  wc "I guess it's time for me to drive you to the airport, right? I'm really going to miss having you around."
  nn "Especially after last night?"
  # Blushing WHO-chan sprite
  show who shy at center
  wc "Geeze. Well, I guess this is it...."
  # Hopeful WHO-chan sprite
  show who joy at center
 
  menu:
    "What should I do?"

    "Time to return home":
        $route="M1"
    "Maybe I should stay":
        $route="M2"

  $renpy.call(route)
 
label M1:
  nn "Yeah. This is it."

  if stay_flag = 1:
    jump M1_Stay
  else:
    jump M1_Going

label M1_Stay:
  wc "It's too bad, you know. I wish you would stay with me, here."
  nn "My family's waiting for me back home. Plus, I've already got a job at a clinic in my home town. I can't turn my back on the people who depend on me."
  wc "I guess you're right. You're so responsible, Protag-kun."
  nn "But, if you're ever in the area... be sure to drop by."
  wc "I'd like that."
  show who sad at center
  nn "Oh, crap! My flight leaves in less than an hour!"
  # Shocked WHO-chan sprite
  show who suprised at center with Pause(2)
  show who excited at center
  wc "Oh no! We're going to have to hurry!"
  # Scene: WHO-chan driving a jeep like a maniac and terrifying Protag-kun
  # Scene: Protag-kun in airplane looking down on the African coast
  # Scene: Protag-kun back in the states, tired but relieved
  jump Credits
 
label M1_Going:
  wc "Well, I guess it's time to get to the airport. When does your flight leave?"
  nn "I'm supposed to be at the airport by noon."
  wc "My plane leaves at four o'clock so we might as well go together."
  nn "I'd like that."
  wc "Hey... we don't actually live that far apart, do we?"
  nn "Back in the States? No, only a couple hundred miles."
  wc "You know... if you wanted to come over on the weekend, once in awhile..."
  nn "You'd like that?"
  show who annoyed at center with Pause(2)
  show who joy at center
  wc "Maybe."
  # Scene: WHO-chan and Protag-kun at the airport waving passports angrily
  # Scene: Protag-kun in airplane looking down on the African coast
  # Scene: WHO-chan and Protag-kun at a Thanksgiving dinner, arguing in front of a family
  jump Credits

label M2:

  if stay_flag = 1:
    jump M2_Stay
  else:
    jump M2_Going

label M2_Stay:
  nn "I think I'm going to miss my flight."
  wc "What do you mean? We've got plenty of time to get to the airport."
  nn "I actually think I want to stay."
  wc "You mean with me?"
  nn "Well... that's part of it."
  show who angry at center
  nn "A big part of it! But I was thinking about what you said about every day being an adventure, and you know what? I think you're right. And I want to share that ongoing adventure with you."
  show who joy at center
  wc "That's so sweet... I mean... fine, you dork!"
  # Scene: WHO-chan and Protag-kun running around in lab coats
  # Scene: WHO-chan and Protag-kun eating off each others' plates under traditional West African regalia
  jump Credits
 
label M2_Going:
  nn "I think I'm going to miss my flight."
  wc "What do you mean? We've got plenty of time to get to the airport."
  nn "I actually think I want to stay."
  wc "Really? I thought you hated it here."
  nn "I changed my mind. You're right - this place really is a new adventure every day."
  wc "Well, it's your choice, I guess..."
  nn "You're still planning on returning to the States, right?"
  wc "Yeah. I've got to be practical and plan for the future."
  nn "Just in case..."
  wc "Hmm?"
  nn "If you ever get assigned to Equatorial Leone again, be sure and look me up!"
  wc "I will. I promise."
  # Nature sounds
  wc "Will you at least see me off to the airport?"
  # Scene: WHO-chan driving a jeep like a maniac and terrifying Protag-kun
  # Scene: Protag-kun in front of a small but modern and freshly painted African clinic surrounded by children
  jump Credits

label Credits:
  jump start