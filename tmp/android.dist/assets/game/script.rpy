# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
image bg black = Solid((0, 0, 0, 255))

image bg sunset = "images/backgrounds/tt1.png"
image bg ashes = "images/backgrounds/tt2.png"

image tam1a = "images/sprites/tamamo_st01.png"
image tam1b = "images/sprites/tamamo_st01a.png"
image tam1c = "images/sprites/tamamo_st01b.png"
image tam1d = "images/sprites/tamamo_st01c.png"

image tam2a = "images/sprites/tamamo_st03a.png"
image tam2b = "images/sprites/tamamo_st03b.png"

image tam3a = "images/sprites/tamamo_st04a.png"
image tam3b = "images/sprites/tamamo_st04b.png"
image tam3c = "images/sprites/tamamo_st04c.png"

image ctc_tball = anim.Filmstrip("images/tballstrip3.png", (30,30), (8,1), 0.1, xpos=1840, ypos=1020, xanchor=0, yanchor=0)

define t = Character(name='Tamamo', what_color="#efdea4", who_color="#c49f76", what_prefix='"', what_suffix='"', ctc="ctc_tball", ctc_position="fixed", ctc_pause="ctc_tball", ctc_timedpause=Null())
define tq = Character(name='Tamamo', what_color="#bd8cbf", who_color="#c49f76", what_prefix='"', what_suffix='"', ctc="ctc_tball", ctc_position="fixed", ctc_pause="ctc_tball", ctc_timedpause=Null())

define centered = Character(name=' ', what_style="centered_text", window_style="centered_window")

# The game starts here.
label start:

    scene bg black with fade
    
    centered "{i}After the end of the great war and her partial sealing, Tamamo takes a husband,{p=2}badly injured fighting on the monster side during the last stages of the war,{p=2}
   and they begin living quietly in a remote lakeside fishing village.{/i}"
    
    centered "{i}9 years later.{/i}"
    
    scene bg sunset with fade
    
    pause 3.0
    
    show tam1b:
        zoom 1.3
        xalign 0.5
        yalign 1.0
        
    t "I was there you know.{p=2}
    On this day{w=0.5}, ten years ago.{p=2}
    The last real battle of the Great War.{p=2}
    The Battle of the Ashen Fields,{w=2} the day your face was ruined."
    
    t "High in the clouds,{w=0.25} hidden by magic{w=2} - I watched it all."
    
    t "I watched your charge break the Pontiffs Elite Guard.{p=2}
    The 1st Reminan Mixed{w=2}{nw}"
    
    hide tam1b
    show tam1d:
        zoom 1.3
        xalign 0.5
        yalign 1.0
    extend " - You were magnificent."
    
    hide tam1d
    show tam1c:
        zoom 1.3
        xalign 0.5
        yalign 1.0
    t "And I watched you all burn as the war machines of Ilias rained unquenchable fire down on you."
    
    t "She knew{w=0.5} - The Monster Lord I mean.{p=2}
    She knew days{w=0.5}, perhaps weeks before{w=2} - she knew what they were and what they could do."
    
    hide tam1c
    show tam2a:
        zoom 1.3
        xalign 0.5
        yalign 1.0
    
    t "They were a breach of the agreements on large scale battlefield magics,{p=1}but still she let them be brought up unopposed."
    
    tq "Should they use them our response must be swift and overwhelming{w=1} - a show of force.{p=2}
    We must leave them in no doubt as to where that path will lead,{p=1}
    and our willingness to follow them on it should they choose to walk it.{p=2}
    But it will not be us that takes the first step."
    
    t "Thats what she said."
    
    hide tam2a
    show tam2b:
        zoom 1.3
        xalign 0.5
        yalign 1.0
    
    t "She needed someone powerful and trustworthy.{p=2}
    Someone who would not shirk from{w=1}, nor revel in{w=2}, what had to be done."
    
    t "She chose me.{p=4}
    And I did my duty."
    
    hide tam2b
    show tam1b:
        zoom 1.3
        xalign 0.5
        yalign 1.0
        
    t "Five Thousand souls{w=4} - mostly humans{w=1} with some monsters spared to act as beasts of burden.{p=3}
    With one spell I snuffed them out.{p=4}
    The entire siege line vaporized in the blink of an eye.{p=3}
    Five Thousand."
    
    hide tam1b
    show tam3a:
        zoom 1.3
        xalign 0.5
        yalign 1.0
    
    t "As to how many more I maimed and blinded that day{w=2} - I still don't know."
    
    hide tam3a
    show tam3b:
        zoom 1.3
        xalign 0.5
        yalign 1.0
    
    t "That evening I went down there.{p=2}
    To see what I had done.{p=2}
    I didn't want to remember it in some abstract way.{p=2}
    I had to see with my own eyes."
    
    hide tam3b
    show tam2b:
        zoom 1.3
        xalign 0.5
        yalign 1.0

    t "Ash.{p=4}
    All was ash.{p=4}
    No bodies{w=2}, no bones.{p=2}
    Just ash{w=3} - turned red in the glow of the setting sun."
    
    hide tam2b
    show tam1b:
        zoom 1.3
        xalign 0.5
        yalign 1.0
    
    t "That's the real reason I didn't let myself be fully sealed.{p=2}
    To let myself be hidden away after that would have been wrong.{p=2}
    It would have been running away from the truth."
    
    t "I know what I did.{p=2}
    I should live knowing{w=2} - I should die knowing."
    
    hide tam1b
    show tam1c:
        zoom 1.3
        xalign 0.5
        yalign 1.0
    
    t "I have no God to ask for absolution.{p=3}
    The one who created me was the one who asked me to bear this burden."
    
    t "The only one who can forgive me is myself.{p=2}{nw}"
    
    hide tam1c
    show tam2b:
        zoom 1.3
        xalign 0.5
        yalign 1.0
        
    extend "And that's something I am not yet prepared to do."
    
    hide tam2b
    show tam1b:
        zoom 1.3
        xalign 0.5
        yalign 1.0
    
    t "Maybe in the years,{w=0.5} decades{w=0.5} or centuries to come.{p=2}
    I have to see for myself that one day this world truely does become a better place.{p=2}
    That what I did really does make a difference.{p=2}
    Untill that day I'll just wait{w=1}, and watch {w=1.5}- as long as it takes."
    t "Perhaps then I'll be able to sleep soundly.{p=2}{nw}"
    hide tam1b
    show tam3a:
        zoom 1.3
        xalign 0.5
        yalign 1.0
    
    extend "And not keep dreaming of endless{w=2}, blood red ash."
    
    hide tam3a
    show tam1d:
        zoom 1.3
        xalign 0.5
        yalign 1.0
        
    t "So now you know.{p=4}
       I'm a mass murdering old fox."
    
    hide tam1d
    show tam1b:
        zoom 1.3
        xalign 0.5
        yalign 1.0
        
    t "Even so{w=4} - can you still love me?"
    
    pause 5.0
    
    scene bg black with fade
    
    
    

    
    
    
    return
