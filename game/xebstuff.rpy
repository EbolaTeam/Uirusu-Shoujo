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

scene bg xebdorm with fade
show ebby normal:
    zoom 1.0
    xalign 0.1
    yalign 1.0

menu:
    "What to do?"

    "Stay at the dorm a while longer.":
        $place="dorm"
    "Take a look around school grounds.":
        $place="grounds"
    "Study at the library before classes.":
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


label day1_morning:
    scene bg xebdorm_room with fade
    show ebby joy:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    ec "Here the protag wakes up in the morning!"

    return


label day1_morning_dorm:
    scene bg xebstreet with fade
    show ebby normal:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    ec "They are late! Ebby runs to school with protag with toast in her mouth!"
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