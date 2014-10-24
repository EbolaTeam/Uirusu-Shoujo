label rydeasPureAids:

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




show ebby normal:
    xalign 0.1
    yalign 0.7
ec "Hello!"
show ebby joy
ec "Wanna know something fun?"
show ebby excited
ec "You thought you where talking to some cute little virus?"
show ebby rape 
ec "Well think again fucker!"
hide ebby
show ry:
    xalign 0.1
    yalign 0.7
"Ryan" "IT'S RYAN TIME!"
"Ryan" "I know you'd just skip this bit if you saw this shitty drawing, so I constructed an elaborate ruse!"
"Ryan" "Anyway, This is just the Aids story I've been working on, all else stripped away"
"Ryan" "All desisions directly affect the ending, of which there are 3. One is filler allowing for another girl."
"Ryan" "Not so much Aid's bad route, just what happens when you don't score enough points with her."
"Ryan" "If everyone did this sort of thing merging would be a brease"
"Ryan" "Anyway, enjoy the show!"

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

    "Do something unrelated to Aids":
        $place="ElseAids"
    "Get Ebby to show you around the classrooms.":
        $place="libraryRy"
    
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

        "Do something unrelated to Aids":
            $place="ElseAids"
        "Go the corridor and think.":
            $place="corridorRy"

else:
    menu:
        "What to do?"

        "Do something unrelated to Aids":
            $place="ElseAids"
        "Go find Eidzu":
            $place="corridorRy"


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

    "Do something unrelated to Aids":
        $place="ElseAids"
    "Head home alone.":
        $place="gateRy"

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

    "Do something unrelated to Aids":
        $place="ElseAids"
    "Have a shower.":
        $place="showerRy"


$destination="day"+str(day)+"_"+time+"_"+place
$renpy.call(destination)

if AidsCount >= 4:
    if AidsMetFulfilled == 0:
        jump day1_NightRy_BedRy
call day1_endRy

call decisionRy

$renpy.call(str(bestgirl)+"_endRy")

jump doneRy





