label rydeas:

image bg white = "images/placeholder/white.png"
image bg lab = "images/placeholder/lab.jpg"
image bg river = "images/placeholder/river.jpg"
image bg nurg = "images/placeholder/nurg.png"


image ry = "images/placeholder/ry.png"
image pro = "images/placeholder/pro.png"
image sian = "images/placeholder/sian.png"
image bsg = "images/placeholder/bsg.png"
image nye = "images/placeholder/nye.png"
image zmapp = "images/placeholder/zmapp.png"
image ebbyz = "images/placeholder/ebbyz.png"

define prin = Character(name='')
define pr = Character(name='Protag', what_prefix='"', what_suffix='"',)
define si = Character(name='Sian', what_prefix='"', what_suffix='"',)
define bsg = Character(name='Black Science Guy', what_prefix='"', what_suffix='"',)
define bn = Character(name='Bill Nye', what_prefix='"', what_suffix='"',)
define nur = Character(name='Giant Scary Blob Thing', what_prefix='"', what_suffix='"',)
define zma = Character(name='Zmapp-chan', what_prefix='"', what_suffix='"',)
define ug = Character(name='Unknown Girl', what_prefix='"', what_suffix='"',)
define ai = Character(name='Aids-chan', what_prefix='"', what_suffix='"',)

$ AidsMeet = 0
$ AidsCount = 0
$ AidsMetFulfilled = 0
$ AidsProprietary  = 0

$ EbbyBrowniePoints = 0


scene bg white

show ry:
    xalign 0.1
    yalign 0.7


"Me" "Hello!"
"Me" "Just a little pre-demo explanation thingy"
"Me" "I don't intend any specifc things here to be part of the plot..."
"Me" "But I think what we need most right now is a frame for everyone to work in."
"Me" "Xebec's thing here is a good example, a basic layot of possible events that we can go and fill in."
"Me" "For example, the little story Linder wrote about zmapp and ebby chasing eachother could fit perfectly if someone just threw it into what xebec has."
"Me" "I think it woud be good if someone make a more broader framework that we can all throw our little pieces into, potentially even something we could throw smaller little frames into"
"Me" "That is what I intend to do here."
"Me" "If anyone has any ideas please feel free to throw them inside this scrypt somewhere."
"Me" "Just find somewhere you think they'll fit and throw them in."
"Me" "Althoutgh I do have 1 request..."
"Me" "Leave at least 3 lines space between the top and bottom of what you do, like so:"






"Me" "People looking through the .rpy know what I'm talking about"
"Me" "Anyway, that's basicly it. Just lop out any 3 sequence events that look like they where written to fill space"
"Me" "However, if you see something it looks like someone wrote, or tried to wright, as a proper scene, just put your bit after it."
"Me" "Maybe say something like \"The following is what could have happened after SARS raped that mosquito\" or something, just so we know where you're coming from."
"Me" "I've thrown in bits of everyone's stuff so you can have an idea of how we could all build off the base"
"Me" "Nothing's set in stone, this is mainly just to get us all started"




scene bg black with fade
$renpy.music.set_volume (0.5, channel="music")
play music "FeelsChiptune.mp3" noloop

centered "Africa, the not too distant future"

    
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
stop music fadeout 1.0
    
centered "Present day"
centered "Present time"


scene bg lab with fade

show pro:
    zoom 1.0
    xalign 0.1
    yalign 1.0
    
pr "It's been years since I started working here."
pr "Nobody ever realy asked why, guess I'm not really the type people make chitchat with."
pr "What does suprised me is how very few people ever ask me what I'm doing"
pr "\"Million dollar equiptment? Sure. A 20 man team? Here you go. 5 billion dollars? For research? You act like you think I'm gonna say no.\""
pr "Funny, for all I've ever done they only know about a select few things, thet think that's what I'm pouring all these years into, all their money into."
pr "They don't know jack shit, but they're still impressed."
pr "I don't really know what that means, if I'm some smartass who pulls off miricals in his coffee break, the higher upps know nothing about science, or I just have the right approach..."
pr "I'd say the last, I may work for a big pharmasutical company but management aren't as dumb as most places, they know a stem cell from \"Deep fortifying face cream with progenic nanobubbles!\"."
pr "Still, supprised no-one checks up on me too much. I guess just looking at the notes I make every once in a while on what I'm supposed to be doing makes them think I'm working harder than anyone here."
pr "Which sadly isn't what I really want, I'd prefer to float in the grey, but I don't want to become nobody."
pr "Still, I guess I get the most money, who's gonna bitch?"
pr "So what do I show them you ask?"
pr "When I'm boored or my brain's just a bit worn out I work on what my paycheck says I do, cures for illnusses. Viruses. Whatever I feel like."
pr "They really don't mind, as long as I'm fixing something"
pr "It means they don't ever know exactly what we're doing, just what we give them, and that's enough"
pr "Some may say the cures I come up with are insanly brilliant, that I'd have to be some crazy genius to even work them out, they wouldn't beleive me if I told them I spent maybe 3 hours every friday making them."
pr "Although they'd be wrong, about the first thing, that is. I'm no genius, it's what I do for the rest of the week, with the rest of the money, the stuff I don't tell them about which kinda lets me come up with cures rather quickly and effortlessly."
pr "Some may say what I do then isn't really moral, that it isn't how a scientist would do things, that the payoff wasn't worth the cost."
pr "They don't know why I'm really doing it though."
pr "I'm not some delusionall scientist that thinks it's okay to take a huge risk for all the people it saves."
pr "What I'm doing is compleatly intentional. The dangerous means aren't a way of getting somewhere, they're my goal."
pr "You see, this is why I don't want the higher ups paying too much attention, if they realised what I was doing they'd wuestion why. Their first answer would be \"Off-the-books reckless but dammit you get the job done\" kinda thing, but they wouldn't beleive that."
pr "They'd soon realise why I was really doing what I'm doing, they wouldn't think for a second before firing me, risks-for-the-good-of-humanity goes out the door when they realise I don't give a shit about the good of humanity and I'm doing this specificly against that cause."
pr "Not even most of my team really knows why they're doing what their doing, they get orders from me and they do them"
pr "Those who do think reach the \"dammit you get the job done\" thing, and they thing management has the same idea's but is happy with it, so they keep quiet."
pr "It's fun being the translator man in the anti-censorship club."
pr "Anyway, more specifics. My project isn't working on anything inherintly bad, I'm not even really using it for BAD, I'm just giving it to bad to see what bad does with it."
pr "Same goes for good for a couple hours a week, and management like that."
pr "How does this shit work you ask? Well, baic evolution works by tiny changes happening when an organism recreates itself..."
pr "...and the resulting changes, mutations, affecting the oranism's chances of yet again recreating itself."
pr "Spread this over billions of years and you get, well, all living shit."
pr "For humans this process happenes once ever 20 or so years, viruses can do so in minutes."
pr "But the difference between the times is really not that big, 20 years might as well be 2 minutes, cool shit's still not gonna happen in my lifetime"
pr "Because most copies end up being too close to the original it takes ages before you even get a chace at something cool, and that chance is still probably 1 in a million."
pr "I decided to speed up this process by making each copy, each child, have a lot more changes than usuall."
pr "Radiation tends to do the same but it just shreads the DNA leaving utter destruction."
pr "What I wanted is to affect every child, but not so drasticly."
pr "I did this by using a organism of my own, a virus that lives on, or really just bondes to other viruses, changing their coppy's."
pr "Nice, non-destructive, doesn't really hurt the viruses. No need to reengineer every bloody organism I want to work on, just shake and go"
pr "The effect? Well, a medicin might kill 99.99\% of viruses, but that 1 in 10 billion retard virus babby with the genetic fuckup thatmakes it immune to penicilin's gonna be the Adam of a new race"
pr "The shit I've created in this lab out of the virus samples I'm supposed to be trying to kill scare even me, doesn't stop me from carrying a little viril of airborne Cuevavirus Lloviu around my neck."
pr "If people ask I just say it's part of a cure to cancer. Heh..."
pr "Anyway, thanks to the, well, enhancing organism I made being self-replicating I've been able to apply it to almost..."
"KNOCK KNCOK"
si "Sir, th"
pr "Dammit girl, Can't you see I'm monologing to myself?"

show sian:
    zoom 1.0
    xalign 0.3
    yalign 0.75

si "You do that every day Sir, but this is important."
pr "That's Sian, not said how it's spelt. She's my complacent assistant. I'd love to rail her some day, but she was in human testing for a bit, so..."
si "SIR, STOP THAT! At least think it to yourself."
pr "But you've never inturupted me like that before, I've never had the chance to say shit activly."
si "That's because you put HIV into the last guy who did that's sandiches!"
pr "Well you're the cute secretary, you're supposed to do that stuff."
pr "Plus, that batch of HIV only turns into AIDS in people with high Melanin count"
si "Why did we even have that? And wouldn't it still spread to those people?"
pr "They've all got it anyway, who cares?"
"KNOCK KNOCK"
si "Dammit we got distracted, Sir, the guests"
pr "What it is"    
si "They're here to see you, Sir. It's important. With what's goin on overseas, and now in texas, your reasearch is in the spotlite. They want to talk to you."
pr "Who are they?"
si "I'll let them in and you can see for yourself"
pr "Oh mein god"

show bsg:
    zoom 1.0
    xalign 0.7
    yalign 0.7

bsg "Hello, you must be the doctor. It's a pleasure to meet you"

show nye:
    zoom 1.0
    xalign 1.0
    yalign 1.0

bn "Also Hi. It's an honour"
pr "Are you kidding me, you guys are the 2 greatest minds of our generation, the pleasure's all mine!"
bsg "You might not think so now, but from what I've read your reasearch is groundbreaking. You can cure anything. Well we need a cure for Ebola, now."
pr "Are you crazy? That could take years!"
bsg "I've read through your work, you seem to doubt yourself now, but from what I've read you could do this in a week"
pr "That's crazy, that was a total fluke, I couldn't pull that off again."
bsg "I don't know for sure, but I have my suspisopns. Would you mind if you showed us your work? We'd like to know how you made these things."
pr "Sure, come over here to my desk and I'll show you what I have"
"Fuck Fuck Fuck Fuck Fuck Fuck Fuck..."
pr "So this is something I've been playing with recently, I'm trying to work out how I can stop the HIV from turning into AIDS, it's been tricky but I'm making progress"
bsg "I heard about that, we want to know how the hell you reached these answeres"
pr "Oh they're nothing, I'm nowhere close to a cure"
bsg "But what you worked out was so brilliant, so complex, I can't begin to understand how you came up with it"
pr "Well, to be honest, I didn't really do it how you'd think"
bsg "Elaborate"
pr "You see, rather than bashing my brain on working out solutions to problems I just let evolution do its thing and study the results."
pr "My finding are based on the most fit cells that fight the issue, I reverse engineer them from there, compare the changes."
bsg "That's not how it works you little shit, but I love it. But how do you make so many permutations? That would take years, you've fixed thing thrown at you in a couple of days! Small as they may have been, it was a greater acomplashement than anyone has managed before. How do you do this"
pr "Well, I use something I created ages ago, it's a very basic thing that promotes changes in every single offspring, nothing too fancy, I found it by pot luck. But when I apply it to some of the more common cells in humans, expose the relults to viruses the good cells literally just sit there, waiting for me to notice them"
bsg "How much of this mutagen have you got? Have you tried using it on Ebola?"
pr "I-I'm sorry, what?"
bsg "Have you applied the resulting cells to ebola samples to see if anything will hurt it?"
pr "Oh, sorry. Um, no. Not yet. Not recently, at least."
bsg "Coudl we run through it now? We have all day, and it's what the world needs right now."
pr "Sure, we can do it now. Grab that incubator over there, Sian, get me a Ebola sample pack"
bsg "This one?"
pr "No, grab the one on the end, the rest aren't clean"
si "Here Sir"
pr "Shit, this is the airborne batch"
bsg "The airborne what? What you got over there?"
pr "Nothing! Um, I-I'll get an ebola sample."
bsg "Ain't that an Ebola sample? It says ebola."
pr "Nah, it's just an old experiment I did years ago, what I made killed the cells, sure, but so would sulfuric acid"
bsg "Heh..."
pr "Great, we're good to go!"
bsg "Wait, didn't you say something about those being airborne?"
pr "Nah, did I?"
pr "Oh who cares, to work! We've got a virus to get rid of!"
"POP!"
"HISSSSSSSSSSSSSSSSSS"
pr "Siannn"
si "Uh, yes?"
pr "Was that what I though it was?"
si "Um, yes Sir"
pr "Fuck."





scene bg black with fade
scene bg river with fade
centered "Love is life"

show ry:
    xalign 0.1
    yalign 0.7

"Me" "(Potential boat sequence, maybe?)"
"Me" "Could be vauge, maybe this (And the following) are slowly rememberes over the course of the 1st act?"




scene bg black with fade
scene bg nurg with fade
show pro:
    xalign 0.1
    yalign 1.0
pr "h-Helo?"
pr "Where am I?"
nur "Welcome to my wourld."
pr "What? Who are you?"
nur "I'm very familure with your works. You have served me well"
pr "I don't even know you!"
nur "You don't need to. To keep this short, I am, well, how would you say..."
nur "The god of entropy I guess. I seek natural conclusion."
nur "I have many children helping me with this cause, you have been the first of human origin I have deemed worthy of direct interaction with my daughters."
nur "You will have dominion over your creation, as my daughters have domioion over their respective, well..."
nur "You'll find out soon enough"
scene bg black with fade
























$place=""
$day= 1
$time = ""

$ebby_affection = 0
$sars_affection = 0
$aids_affection = 0
$malaria_affection = 0

$bestgirl=""

call introRy
call day1_morningRy

$time = "morningRy"

scene bg xebdorm with fade
show ebby normal:
    zoom 1.0
    xalign 0.1
    yalign 1.0

menu:
    "What to do?"

    "Stay at the dorm a while longer.":
        $place="dormRy"
    "Take a look around school grounds.":
        $place="groundsRy"
    "Get Ebby to show you around the classrooms.":
        $place="libraryRy"
    "Head straight to class.":
        $place="classRy"
    
$destination="day"+str(day)+"_"+time+"_"+place
$renpy.call(destination)

call day1_lunchRy

$time = "lunchRy"

scene bg xebclass with fade
show ebby normal:
    zoom 1.0
    xalign 0.1
    yalign 1.0

if AidsMeet == 0:
    menu:
        "What to do?"

        "Have lunch outside.":
            $place="groundsRy"
        "Have lunch on the roof.":
            $place="roofRy"
        "Go the corridor and think.":
            $place="corridorRy"
        "Have lunch in the library.":
            $place="libraryRy"
        "Go exploring.":
            $place="explore"
else:
    menu:
        "What to do?"

        "Have lunch outside.":
            $place="groundsRy"
        "Have lunch on the roof.":
            $place="roofRy"
        "Go find Eidzu":
            $place="corridorRy"
        "Have lunch in the library.":
            $place="libraryRy"
        "Go exploring.":
            $place="explore"

$destination="day"+str(day)+"_"+time+"_"+place
$renpy.call(destination)

call day1_afternoonRy

$time = "afternoonRy"

scene bg xebclass with fade
show ebby normal:
    zoom 1.0
    xalign 0.1
    yalign 1.0

menu:
    "What to do?"

    "Stay in class a while.":
        $place="classRy"
    "Drop by the gym hall.":
        $place="gymRy"
    "Head home alone.":
        $place="gateRy"
    "Visit the Dock":
        $place="dockRy"

$destination="day"+str(day)+"_"+time+"_"+place
$renpy.call(destination)

call day1_eveningRy

$time = "eveningRy"

scene bg xebdorm with fade
show ebby normal:
    zoom 1.0
    xalign 0.1
    yalign 1.0

menu:
    "What do do?"

    "Go help out in the kitchen.":
        $place="kitchenRy"
    "Sit in the garden a while.":
        $place="gardenRy"
    "Have a shower.":
        $place="showerRy"
    "Stay in room.":
        $place="roomRy"

$destination="day"+str(day)+"_"+time+"_"+place
$renpy.call(destination)

if AidsCount >= 4:
    if AidsMetFulfilled == 0:
        jump day1_NightRy_BedRy
call day1_endRy

call decisionRy

$renpy.call(str(bestgirl)+"_endRy")

jump doneRy






label introRy:
    scene bg xebriver with fade
    show ebby normal:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    show joki evil:
        zoom 1.4
        xalign 0.9
        yalign 1.0
    ec "This is where the introduction goes!"

    return


label day1_morningRy:
    scene bg xebdorm_room with fade
    show ebby joy:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    ec "Here the protag wakes up in the morning!"

    return


label day1_morningRy_dormRy:
    scene bg xebstreet with fade
    show ebby normal:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    ec "They are late! Ebby runs to school with protag with toast in her mouth!"
    $ebby_affection+=1
    return


label day1_morningRy_groundsRy:
    scene bg xebtrack with fade
    show ebby rape:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    show sars grin:
        zoom 1.6
        xalign 0.9
        yalign 1.0
    ec "Meet Sars having an early morning run at the track!"
    $sars_affection+=1
    return





label day1_morningRy_classRy:
    scene bg xebclass with fade
    show ebby joy:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    ec "Malaria is such a good girl! She is early to class and studying!"
    $malaria_affection+=1
    return

label day1_lunchRy:
    scene bg xebclass with fade
    show ebby joy:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    ec "They have morning classes!"

    return

label day1_lunchRy_groundsRy:
    scene bg xebgrass with fade
    show ebby normal:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    ec "Having lunch in the sun with Ebby! Lucky!"
    $ebby_affection+=1
    return

label day1_lunchRy_roofRy:
    scene bg xebroof with fade
    show ebby joy:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    show sars grin:
        zoom 1.6
        xalign 0.9
        yalign 1.0
    ec "Eating a healthy lunch on the roof with Sars!"
    $sars_affection+=1
    return



label day1_lunchRy_libraryRy:
    scene bg xeblibrary with fade
    show ebby normal:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    ec "Having a quiet lunch with malaria in the library."
    $malaria_affection+=1
    return
    
    
    
    
    
    
label day1_lunchRy_explore:
    scene bg xebriver with fade
    show pro:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    pr "How did I end up here?"
    pr "I realy shouldn't have walked around without someone to guide me, now I'm lost"
    show zmapp:
        zoom 1.0
        xalign 0.9
        yalign 0.7
    "I think there's someone else here"
    pr "Hello?"
    ug "WHAAAAAAAAA. Don’t sneak up on me like that! I’m working here."
    pr "Working on what?"
    ug "Oh, you’ll see… Now, let me get back to work."
    ug "So… if I put this one here…"
    ug "OH SHIT"
    show ebby rape:
        zoom 1.0
        xalign 0.7
        yalign 0.7
    ec "IT'S RAPE TIME"
    ug "No, No, No!"
    ec "I GOT YOU NO-oh."
    ec "MC?"
    hide zmapp
    ec "OH GOD I’M SO SORRY. I didn’t mean to hurt you. Are you ok?"
    pr "Yes, I think."
    ec "Anyway, you didn’t happen to see someone in green run this way, did you?"
    pr "Yeah… they went that way, why?"
    ec "I’LL TELL YOU LATER."
    
    
    scene bg xebroof
    "I think I finally found them"
    show ebby sad:
        zoom 1.0
        xalign 0.7
        yalign 0.7
    show zmapp:
        zoom 1.0
        xalign 0.9
        yalign 0.7
    ug "Come on, ‘Pinky’, you’ll have to do better than that if you want your hat back."
    ec "Oh yeah?"
    hide ebby
    hide zmapp
    show ebbyz:
        zoom 1.0
        xalign 0.7
        yalign 0.7
    ug "Shit."
    ec "Wait, we're laste for class"
    hide ebbyz
    show zmapp:
        zoom 1.0
        xalign 0.7
        yalign 0.9
    ug "(Panting on the ground)"
    scene bg black with fade
    return


label day1_afternoonRy:
    scene bg xebclass with fade
    show ebby joy:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    ec "They have afternoon classes!"    
    return

label day1_afternoonRy_classRy:
    scene bg xebstreet with fade
    show ebby joy:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    ec "Ebby asks to walk home with you! Lucky!"
    $ebby_affection+=1
    return

label day1_afternoonRy_gymRy:
    scene bg xebgym with fade
    show ebby normal:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    show sars grin:
        zoom 1.6
        xalign 0.9
        yalign 1.0
    ec "Sars is playing volleyball! She is very good!"
    $sars_affection+=1
    return



label day1_afternoonRy_dockRy:
    scene bg xebdock with fade
    show ebby sad:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    ec "Malaria is reading poetry aloud to herself.  She is a bit funny that way."
    $malaria_affection+=1
    return

label day1_eveningRy:
    scene bg xebdorm with fade
    show ebby joy:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    ec "Everyone is at home in the dorm!"
    return

label day1_eveningRy_kitchenRy:
    scene bg xebkitchen with fade
    show ebby joy:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    ec "Ebby is helping Bubonic Plague in the kitchen! I'm such a good girl!"
    $ebby_affection+=1
    return

label day1_eveningRy_gardenRy:
    scene bg xebgarden with fade
    show ebby sad:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    show sars sad:
        zoom 1.6
        xalign 0.9
        yalign 1.0
    ec "Sars is stretching in the garden but has hurt her shoulder!"
    $sars_affection+=1
    return



label day1_eveningRy_roomRy:
    scene bg xebdorm_room with fade
    show ebby normal:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    ec "Malaria brings protag some books to read!"
    $malaria_affection+=1
    return

label day1_endRy:
    scene bg xebnight with fade
    show ebby normal:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    ec "The end of Day 1 - everyone goes to sleep! Nighty Night!"
    return

label decisionRy:
    scene bg black with fade
    show ebby normal:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    ec "Decision Time!"

    "Affection Points:\n
    Ebola       [ebby_affection]\n
    Sars        [sars_affection]\n
    Aids        [AidsCount]\n
    Malaria     [malaria_affection]"

    
    if ebby_affection > 2:
        $bestgirl="ebby"
    elif sars_affection > 2:
        $bestgirl="sars"
    elif aids_affection > 2:
        $bestgirl="aids"
    elif malaria_affection > 2:
        $bestgirl="malaria"
    else:
        $bestgirl="none"
return

label ebby_endRy:
    scene bg black with fade
    show ebby joy:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    ec "You got the Ebby ending! Lucky!"
    return

label sars_endRy:
    scene bg black with fade
    show ebby normal:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    show sars grin:
        zoom 1.6
        xalign 0.9
        yalign 1.0
    ec "You got the Sars ending! Fighto!"
    return

label aids_endRy:
    scene bg black with fade
    show ebby sad:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    show aids joy:
        zoom 1.8
        xalign 0.9
        yalign 1.0
    ec "You got the Aids ending! Ecchi!"
    return

label malaria_endRy:
    scene bg black with fade
    show ebby rape:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    ec "You got the Malaria ending! Boring!"    
    return


label none_endRy:
    scene bg black with fade
    show ebby sad:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    ec "You got the bad end! Nobody loves you!"    
    return

label doneRy:

    scene bg xebfin with fade

    show ebby excited:
        zoom 1.0
        xalign 0.1
        yalign 1.0

    ec "All done!"

jump start

label end: