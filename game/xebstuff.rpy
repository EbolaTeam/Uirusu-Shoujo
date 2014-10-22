label Xebstuff:
    
$place=""
$day= 1
$time = ""

$ebby_affection = 0
$sars_affection = 0
$aids_affection = 0
$malaria_affection = 0

$bestgirl=""

call intro
call day1_morning

$time = "morning"



menu:
    "Well, what should I do?"

    "Stay at the dorm a while longer.":
        $place="dorm"
    "Take a look around school grounds.":
        $place="grounds"
    "Study at the library.":
        $place="library"
    "Head straight to class.":
        $place="class"
    
$destination="day"+str(day)+"_"+time+"_"+place
$renpy.call(destination)

call day1_lunch

$time = "lunch"

scene bg xebclass with fade
show ebby normal:
    zoom 1.0
    xalign 0.1
    yalign 1.0

menu:
    "What to do?"

    "Have lunch outside.":
        $place="grounds"
    "Have lunch on the roof.":
        $place="roof"
    "Go the corridor and think.":
        $place="corridor"
    "Have lunch in the library.":
        $place="library"

$destination="day"+str(day)+"_"+time+"_"+place
$renpy.call(destination)

call day1_afternoon

$time = "afternoon"

scene bg xebclass with fade
show ebby normal:
    zoom 1.0
    xalign 0.1
    yalign 1.0

menu:
    "What to do?"

    "Stay in class a while.":
        $place="class"
    "Drop by the gym hall.":
        $place="gym"
    "Head home alone.":
        $place="gate"
    "Visit the Dock":
        $place="dock"

$destination="day"+str(day)+"_"+time+"_"+place
$renpy.call(destination)

call day1_evening

$time = "evening"

scene bg xebdorm with fade
show ebby normal:
    zoom 1.0
    xalign 0.1
    yalign 1.0

menu:
    "What do do?"

    "Go help out in the kitchen.":
        $place="kitchen"
    "Sit in the garden a while.":
        $place="garden"
    "Have a shower.":
        $place="shower"
    "Stay in room.":
        $place="room"

$destination="day"+str(day)+"_"+time+"_"+place
$renpy.call(destination)

call day1_end

call decision

$renpy.call(str(bestgirl)+"_end")

jump done


label intro:
    
    scene bg xebcult3 with fade

    nn "Being a cultist isn't all its cracked up to be you know"
    nn "sure you get the cool robes, the swag ritual jewellry and the sense of belonging
    body and soul to an other-worldly being"

    nn "but do the recruiting pamphlets mention mucking out the sacrificial animal pens every day?{p}
    or spending hours trying to scrub pus and ectoplasmic residue off of a hardwood floor only to
    be berated in front of the entire cell because Mr adhd-prick-brains-coven-leader thought they
    weren't clean enough for a phlegm imp summoning?"

    nn "No."

    nn "Well, not that the Cult of Pestilence Reborn had any recruiting pamphlets when I joined,{p}
    but I'm sure the wouldn't have mentioned it if they did."

    nn "What really got my sacrificial goat up was the drama."
    nn "I’d clawed my way up the cult hierarchy, putting up with all the bullshit and backstabbing for over a decade,{p}
    until I finally had my own coven."

    nn "I honed them like a well oiled machine, ceremonies exact and on time like clockwork,{p}
    all in service of the disease lord, it was truly a thing of beauty."
    nn "I ruled it with a rod of iron - 100%% Drama free."

    nn "Then I was invited to attend the high symposium"
    "Finally!\" I thought, \"the big league!\"{p}
    \"No more pissing around with petty coven politics.  Now I can work with real professionals all in service of Pestilence Reborn!"

    nn "Oh, how naive I was."

    scene bg xebcult5 with fade

    nn "Ten fucking days of drama."
    nn "Four hour long presentations on what sacrificial dagger designs were ‘in’ this season,{p}
    talks on modern vestment embroidery techniques,"
    nn "motivational courses - MOTIVATIONAL COURSES!"
    nn "The only motivation my cultists needed was that if they didn’t do as they were fucking told they would be the next volunteer
    for the fucking holy slab!"
    nn "And the bickering, I could hear it everywhere, the whispering"
    "did you see that robe deacon Rhiyobe was wearing? Scandalous! that design is definitely from last year!
    how could he possibly show his face here wearing that?"
    "Oh yes, such a thing as that wouldn’t be tolerated in MY coven!"

    scene bg xebcult3 with fade

    nn "I returned a broken man."

    nn "Fuck it, fuck the coven, fuck cults and fuck the Prince of Pestilence."
    nn "Before the week was out I’d embezzled the covens far from insignificant funds and fled the country"

    scene bg xebcompound with fade

    nn "No doubt they sent assassins after me, they do take apostasy very seriously"
    nn "or at least they do when millions of cult dollars are involved,{p}
    but I led them a merry chase around europe, asia and finally Africa."

    nn "Holed up in some shithole Liberian stockade I spent a year waiting on them, but they never came."
    nn "Probably too busy attending a fucking motivational course to chase me that far."

    nn "Tired of the heat I snuck back into the US and settled down quietly in a non-descript out of the way town,
    intending to live a cult free life of leisure and debauchery."
    nn "Unfortunately it seems I brought something unexpected back with me."

    scene bg xebhospital with fade

    nn "Ebola."
    nn "Oh the fucking Irony."
    nn "So here I lie, in the best isolation room stolen money can buy,{p}
    blood seeping through my skin and soaking the silk sheets - a disease ridden disease cultist."
    nn "I’d laugh but I think I’d bring up some liquified lung if I did."

    nn "Do I have regrets?{p}
    Sure, a boatload, buying into the whole cult thing to begin with."
    nn "I can’t believe I actually swallowed all that bullshit, not like it matters{p}
    I’m dying and that’s that"
    nn "no afterlife to look forward to, no ‘pus-heaven’ or whatever that crap was, just oblivion."
    nn "Oh well, at least I had time to write my will{p}
    the look on the faces of the coven leaders when they realise I’ve left their remaining funds to the WHO will be fucking priceless..."

    scene bg black with fade
    

    scene bg xebpop with fade

    "Ho ho ho! So my errent little mortal, you think that was it do you?{p}
    You thought, that you could escape me that easily?"
    "My precious apostate - you offered your soul to me and unlike most of my pathetic supposed followers, you actually meant it!"
    "No"
    "I have use for you yet,{p}
    You might claim you do not believe in the Prince of Pestilence, but he certainly believes in YOU…"

    scene bg black with fade

    scene bg xebriver with fade
    show joki normal:
        zoom 1.8
        xalign 0.1
        yalign 1.0
    joki "This is my scene where I tell the protag a bit about the universe!"

    show joki evil

    joki "Don't talk shit about my boat-fu tho"
return


label day1_morning:

scene bg xebdorm_room with fade

nn "I wake to sunlight streaming in the window and give a stretch."
nn "mmmm this is nice - when was the last time waking up in the morning felt so damn good?"

scene bg xebshower with fade

nn "After getting washed and dressed I give myself a look over in the mirror.{p}
so this is how I look in a school uniform?{p}
Not half bad If I say so myself.{p}"
nn "Laughing I head down for breakfast."

scene bg xebdorm with fade

show sars notamused at left:
    zoom 1.5

sars "AHH! Its the pervert! Don’t look at him or you’ll get molested!"

show aids concerned behind sars:
    zoom 1.8
    xalign 0.3
    yalign 1.0
eidzu "ehhhh? what?!?!?"
"Good morning ladies!"
sars "Grrrrrr!"
eidzu "ah..g-good morning!"

hide sars
hide aids

show mal happy at left:
    xalign 0.1
mal "*smile* *nod*"

show ebby toastdead behind mal:
    xalign 0.3
    yalign 1.0

ec "...."

nn "Ebola-chan is nibbling on her toast, but she seems to be still asleep
I guess she isn’t good with mornings."

hide ebby
hide mal

show bp happy:
    xalign 0.1

bp "Now now, settle down and enjoy your breakfast! It’s the most important meal of the day you know!"

nn "Not one to refuse a nice homecooked meal, I get stuck in."

"Mmm! this is delicious!"

bp "I’m glad it’s to your tastes!"

"Definitly!"

nn "I could easily get used to this." 

hide bp

show sars notamused at left:
    zoom 1.5
sars "I’m done! Come on Eidzu, lets leave now, I don’t want to be around HIM any longer than I have to!"
show aids concerned behind sars:
    zoom 1.8
    xalign 0.3
    yalign 1.0
eidzu "ah! yes - we’ll be going now!"

hide sars
hide aids

nn "She barely has time to call out as she is dragged out the door"

show mal notmal at left:
    xalign 0.1

mal "I should be going too, I want to study a little before class while it’s quiet."
mal "Thank you for the meal."

show bp happy behind mal:
    xalign 0.3

bp "Have a good day!"
mal "I’ll see you two in class."

hide mal
hide bp

show ebby toastdead:
    xalign 0.1
    yalign 1.0
ec "..."

hide ebby

return


label day1_morning_dorm:
    nn "Well there is no sense in being too early on my first day, but I don’t want to be late either."
    nn "I head back to my room and double check that I have everything I need for the day."
    scene bg xebdorm_room with fade
    nn "Ok, looking good."
    scene bg xebdorm_door with fade
    nn "All right, time to go.{p}
    I’m actually starting to feel a bit nerv-"
    ec "AAAAAAAHHHHHHHHHHHHHHHHHHHHHH!!!!!!!!!"
    nn "With a toast-muffled cry Ebola-chan bursts out of into the hall."
    show ebby toastsad at left
    ec "Mfff mff! Mfff mfffff mff mff mffff!"
    nn "Years of cultist experience in understanding the esoteric utterances of summoned other-worldly entities kick in instantly."
    ec "{color=#57bab7}(Oh no! I'm going to be late!){/color}"
    "No, no, you’re ok. We have plenty of time, it’s only half past."
    nn "I glance up at the clock over the door - it says ten to.{p}..oh no."
    nn "My watch still says half past{p}..and isn’t ticking."    
    "AHHHHH!! I’m going to be late!"
    ec "mfff mffff mfffff-mff mmmmff mffff, mfff!\"{p}
    \"{color=#57bab7}(That's what Ebola-chan already said, silly!){/color}"
    nn "Think, think think - yeah we can do this."
    "If we run we can still make it!"
    nn "I grab her hand and drag her out the door!"
    ec "mffffffff!\"{p}
    \"{color=#57bab7}(Kyaaaaa!){/color}"
    "We’ll be heading out!"
    bp "Have a good day!"


    hide ebby
    show bg xebstreet with fade
    show bg xebstreet2 with fade
    show bg xebstreet3 with fade
    nn "It’s actually quite exhilarating.{p}
    Running along like this, I’d almost forgotten this feeling, legs pounding, wind in my hair."
    nn "I feel...alive."
    nn "Being hand in hand with a cute girl is not unpleasant either."
    nn "Although her status as ‘girl’ is perhaps open to debate, she certainly measures up to cute in my book."
    show ebby toastjoy at left
    nn "I turn to look at her, twintails streaming she runs along beside me earnestly."
    nn "She flashes me a smile and gives my hand a friendly squeeze."
    ec "mfff mf mf! mf mfff mf mf!\"{p}
    \"{color=#57bab7}(Keep it up! We can do it!){/color}"
    hide ebby
    nn "Giving her hand a squeeze back I run on.{p}
    Why the hell she still has the toast in her mouth is beyond me."

    show bg xebstreet4 with fade
    show bg xebstreet5 with fade
    show bg xebgate with fade
    nn "We skid to a stop in front of the school gate."
    "I don't know the way from here!"
    show ebby toastjoy at left
    ec "mmff mffff, mmfff-mfff mfff!\"{p}
    \"{color=#57bab7}(Don't worry, Ebola-chan does!){/color}"
    hide ebby
    nn "pulling me along she dashes off towards the main building."
    show bg xebgrass with fade
    show bg xeblockers with fade
    show bg xebstairs with fade
    show bg xebcorridor with fade
    show bg xebclass with fade

    show ebby toastjoy at left
    ec "MFFF!!\"{p}
    \"{color=#57bab7}(SAFE!!){/color}"
    hide ebby
    show sars stars at left:
        zoom 1.5
    sars "WHAT THE HELL ARE YOU DOING WITH MY EBOLA-CHAN!!!"
    with vpunch
    sars "PERVERT!"
    with hpunch
    sars "MOLESTER!"
    with vpunch

    nn "Before I can even catch my breath I’m assaulted by a manic sars-chan."

    show ebby toastsad
    ec "mfff mf mfff-mfff! mff mmmfffff mfff mfff!\"{p}
    \"{color=#57bab7}(Stop it Sars-chan!  It's nothing like that!){/color}"
    show sars concerned at left:
        zoom 1.5
    sars "What? Take that toast out of your mouth, I can't understand a word!"
    show sars stars at left:
        zoom 1.5
    sars "or did he force it on you?"
    with hpunch
    sars "TOAST FETISHIST!"
    ec "mffff! mf mmmffff.\"{p}
    \"{color=#57bab7}(Ohh! I forgot.){/color}"
    nn "finally she takes it out of her mouth."
    show ebby rape
    ec "%(player_name)s-kun didn’t do anything like that! Stop being so mean!{p}
    He was very kind and ran with me all the way here so that I wouldn’t be late!"
    show sars concerned at left:
        zoom 1.5
    sars "hmph! I dont care how kind he is, he shouldn’t be holding your hand with such familiarity!"
    show ebby concerned
    ec "eh?"
    nn "She looks down as if suddenly realising we’re still holding hands."
    show ebby joy
    ec "oh! hehe"
    nn "she gives my hand a last friendly squeeze before letting go and giving me a quick bow."
    ec "Thank you %(player_name)s-kun, I wouldn't have made it on time without you!"
    nn "Now I actually start to feel embarrassed."
    "We both made it in time, that’s the important thing."
    teach "All right! Settle down and get to your seats everyone!"
    nn "And here is the teacher now, looks like we really did make it just in time."
    nn "Ebola-chan flashes me a quick smile and heads to her seat."
    hide ebby
    sars "I'm watching you, toast-fetishist!"
    hide sars
    "Yes, this is going to be an experience indeed."

    scene bg black with fade
    $ebby_affection+=1
    return


label day1_morning_grounds:
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


label day1_morning_library:
    scene bg xeblibrary with fade
    show ebby concerned:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    show aids sad:
        zoom 1.8
        xalign 0.9
        yalign 1.0
    ec "Visit the library and see Aids reading a naughty book!"
    $aids_affection+=1
    return

label day1_morning_class:
    scene bg xebclass with fade
    show ebby joy:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    ec "Malaria is such a good girl! She is early to class and studying!"
    $malaria_affection+=1
    return

label day1_lunch:
    scene bg xebclass with fade
    show ebby joy:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    ec "They have morning classes!"

    return

label day1_lunch_grounds:
    scene bg xebgrass with fade
    show ebby normal:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    ec "Having lunch in the sun with Ebby! Lucky!"
    $ebby_affection+=1
    return

label day1_lunch_roof:
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

label day1_lunch_corridor:
    scene bg xebcorridor with fade
    show ebby sad:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    show aids sad:
        zoom 1.8
        xalign 0.9
        yalign 1.0
    ec "Poor Aids wanted to have lunch with Hiv but he is not around so she ate with protag instead."
    $aids_affection+=1
    return

label day1_lunch_library:
    scene bg xeblibrary with fade
    show ebby normal:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    ec "Having a quiet lunch with malaria in the library."
    $malaria_affection+=1
    return

label day1_afternoon:
    scene bg xebclass with fade
    show ebby joy:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    ec "They have afternoon classes!"    
    return

label day1_afternoon_class:
    scene bg xebstreet with fade
    show ebby joy:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    ec "Ebby asks to walk home with you! Lucky!"
    $ebby_affection+=1
    return

label day1_afternoon_gym:
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

label day1_afternoon_gate:
    scene bg xebgate with fade
    show ebby sad:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    show aids sad:
        zoom 1.8
        xalign 0.9
        yalign 1.0
    ec "Poor Aids wanted to walk home with Hiv but he is off to bang a floozy."
    $aids_affection+=1
    return

label day1_afternoon_dock:
    scene bg xebdock with fade
    show ebby sad:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    ec "Malaria is reading poetry aloud to herself.  She is a bit funny that way."
    $malaria_affection+=1
    return

label day1_evening:
    scene bg xebdorm with fade
    show ebby joy:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    ec "Everyone is at home in the dorm!"
    return

label day1_evening_kitchen:
    scene bg xebkitchen with fade
    show ebby joy:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    ec "Ebby is helping Bubonic Plague in the kitchen! I'm such a good girl!"
    $ebby_affection+=1
    return

label day1_evening_garden:
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

label day1_evening_shower:
    scene bg xebshower with fade
    show ebby rape:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    show aids joy:
        zoom 1.8
        xalign 0.9
        yalign 1.0
    ec "Aids walks in on protag naked in the shower! What a perverted girl!"
    $aids_affection+=1
    return

label day1_evening_room:
    scene bg xebdorm_room with fade
    show ebby normal:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    ec "Malaria brings protag some books to read!"
    $malaria_affection+=1
    return

label day1_end:
    scene bg xebnight with fade
    show ebby normal:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    ec "The end of Day 1 - everyone goes to sleep! Nighty Night!"
    return

label decision:
    scene bg black with fade
    show ebby normal:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    ec "Decision Time!"

    "Affection Points:\n
    Ebola       [ebby_affection]\n
    Sars        [sars_affection]\n
    Aids        [aids_affection]\n
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

label ebby_end:
    scene bg black with fade
    show ebby joy:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    ec "You got the Ebby ending! Lucky!"
    return

label sars_end:
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

label aids_end:
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

label malaria_end:
    scene bg black with fade
    show ebby rape:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    ec "You got the Malaria ending! Boring!"    
    return


label none_end:
    scene bg black with fade
    show ebby sad:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    ec "You got the bad end! Nobody loves you!"    
    return

label done:

    scene bg xebfin with fade

    show ebby excited:
        zoom 1.0
        xalign 0.1
        yalign 1.0

    ec "All done!"

jump start