label Day1:


$place=""
$day= 1
$time = ""

$ebby_affection = 0
$sars_affection = 0
$aids_affection = 0
$malaria_affection = 0

$bestgirl=""

call day1_morningFin

call day1morningwakeFin

$time = "morningFin"

scene bg xebdorm with fade
show ebby normal:
    zoom 1.0
    xalign 0.1
    yalign 1.0

menu:
    "What to do?"

    "Stay at the dorm a while longer.":
        $place="dorm"

$destination="day"+str(day)+"_"+time+"_"+place
$renpy.call(destination)

$time = "SnackFin"

scene bg xebclass with fade
show ebby normal:
    zoom 1.0
    xalign 0.1
    yalign 1.0

menu:
    "What to do?"

    "Get Ebby to show you around the classrooms.":
        $place="libraryFin"
    "Stay in class a while longer":
        $place="classFin"
        
        
    
$destination="day"+str(day)+"_"+time+"_"+place
$renpy.call(destination)

call day1_lunchFin

$time = "lunchFin"

scene bg xebclass with fade
show ebby normal:
    zoom 1.0
    xalign 0.1
    yalign 1.0

if AidsMeet == 0:
    menu:
        "What to do?"
        "Walk around the corridors":
            $place="corridorFin"
        "Explore outside the school":
            $place="explore"
else:
    menu:
        "What to do?"
        "Stay in class a while longer":
            $place="classFin"
        "Go find Eidzu":
            $place="corridorFin"
        "Go exploring.":
            $place="explore"

$destination="day"+str(day)+"_"+time+"_"+place
$renpy.call(destination)

call day1_afternoonFin

$time = "afternoonFin"

scene bg xebclass with fade
show ebby normal:
    zoom 1.0
    xalign 0.1
    yalign 1.0

menu:
    "What to do?"

    "Head home alone.":
        $place="gateFin"

$destination="day"+str(day)+"_"+time+"_"+place
$renpy.call(destination)

call day1_eveningFin

$time = "eveningFin"

scene bg xebdorm with fade
show ebby normal:
    zoom 1.0
    xalign 0.1
    yalign 1.0

menu:
    "What to do?"

    "Have a shower.":
        $place="showerFin"

$destination="day"+str(day)+"_"+time+"_"+place
$renpy.call(destination)

if AidsCount >= 4:
    if AidsMetFulfilled == 0:
        jump day1_NightFin_BedFin
call day1_endFin

call decisionFin

$renpy.call(str(bestgirl)+"_endFin")

jump doneFin










label day1_lunchFin:
    scene bg xebclass with fade
    show ebby joy:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    ec "They have morning classes!"

    return

    
    
    
    
    


label day1_afternoonFin:
    scene bg xebclass with fade
    show ebby joy:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    ec "They have afternoon classes!"    
    return


label day1_eveningFin:
    scene bg xebdorm with fade
    show ebby joy:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    ec "Everyone is at home in the dorm!"
    return





label day1_endFin:
    scene bg xebnight with fade
    show ebby normal:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    ec "The end of Day 1 - everyone goes to sleep! Nighty Night!"
    return

label decisionFin:
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

label ebby_endFin:
    scene bg black with fade
    show ebby joy:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    ec "You got the Ebby ending! Lucky!"
    return

label sars_endFin:
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

label aids_endFin:
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

label malaria_endFin:
    scene bg black with fade
    show ebby rape:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    ec "You got the Malaria ending! Boring!"    
    return


label none_endFin:
    scene bg black with fade
    show ebby sad:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    ec "You got the bad end! Nobody loves you!"    
    return

label doneFin:

    scene bg xebfin with fade

    show ebby excited:
        zoom 1.0
        xalign 0.1
        yalign 1.0

    ec "All done!"

jump start

label end: