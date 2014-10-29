label introAfrica:
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
    
    return

label introLab:    
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
    pr "I hate to speak in such an unprofesional way, but are you high? Hhat was a total fluke, I couldn't pull that off again."
    bsg "I don't know for sure, but I have my suspisopns. Would you mind if you showed us your work? We'd like to know how you made these things."
    pr "Sure, come over here to my desk and I'll show you what I have"
    "Fuck Fuck Fuck Fuck Fuck Fuck Fuck..."
    pr "So this is something I've been playing with recently, I'm trying to work out how I can stop the HIV from turning into AIDS, it's been tricky but I'm making progress"
    bsg "I heard about that, we want to know how the hell you reached these answeres"
    pr "Oh they're nothing, I'm nowhere close to a cure"
    bsg "But what you worked out was so brilliant, so complex, I can't begin to understand how you came up with it"
    pr "Well, to be honest, I'm not the one resposible for these works."
    bsg "Plagorism? Elaborate"
    pr "No, not that. You see, rather than bashing my brain on working out solutions to problems I just let evolution do its thing and study the results."
    pr "My finding are based on the most fit cells that fight the issue, I reverse engineer them from there, compare the changes."
    bsg "That's not how it works you little shit, but fuck it, why not? We're getting kinda desperate."
    bsg "Tell me, how on earth do you make so many permutations? That would take years, you've fixed thing thrown at you in a couple of days! Small as they may have been, they where somewhat groundbreaking none the less. How do you do this?"
    pr "Well, I use something I created ages ago, it's a very basic thing that promotes changes in every single offspring, nothing too fancy, I found it by pot luck. But when I apply it to some of the more common cells in humans, expose the relults to viruses the good cells literally just sit there, waiting for me to notice them"
    bsg "How much of this mutagen have you got? Have you tried using it on Ebola?"
    pr "I-I'm sorry, what?"
    bsg "Have you applied the resulting cells to ebola samples to see if anything will hurt it?"
    pr "Oh, sorry. Um, no. Not yet. Not recently, at least."
    bsg "Coudl we run through it now? We have all day, and it's what the world needs right now."
    pr "Sure, we can do it now. Nye, grab that incubator over there, Sian, get me a Ebola sample pack"
    bn "This one?"
    pr "No, grab the one on the end, the rest aren't clean"
    si "Here Sir"
    pr "Shit, this is the airborne batch"
    bsg "The airborne what? What you got over there?"
    pr "Nothing! Um, I-I'll get an ebola sample."
    bsg "Ain't that an Ebola sample? It says ebola."
    pr "Nah, it's just an old experiment I did years ago, what I made killed the cells, sure, but so would sulfuric acid"
    bsg "Heh..."
    pr "Great, we're good to go!"
    bn "Wait, didn't you say something about those being airborne?"
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
    $ renpy.pause(0.5, hard=True)
    "Cough Cough"
    ug "Pathetic... another one"
    
    
    
    return



label ChapterCover:

    scene bg black with fade
    scene bg river with fade
    centered "Love is life"
    scene bg black with fade
    return

label nurgyboo1:
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
    nur "You'll already understand by the time I've finished explaining, so I won't bother"
    menu:
        "What the hell are you on about?":
            nur "As I said, you'll find out soon enough"
        "Where am I?":
            nur "As I said, you'll find out soon enough"
        "Who are you?":
            nur "As I said, you'll find out soon enough"
    scene bg black with fade
    return









