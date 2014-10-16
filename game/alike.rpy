label alike:
    
    scene bg xebgrass
    show ebby joy:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    ec "Hiya, MC!"
    nn "Oi, wassup Ebby?"
    
    like ec black pudding
    like ec pizza
    like ec lolita
    dislike ec harry potter
    
    ec "I just wanted to ask you..."
    show ebby joy:
        zoom 1.3
        xalign 0.1
        yalign 1.0
    ec "DO YOU LIKE BLACK PUDDING?"
    show ebby joy:
        zoom 1.0
        xalign 0.1
        yalign 1.0
    
    menu:
        nn "Err..."
        "Sure, I do.":
            like nn black pudding
            call ec_yea
        "Not really.":
            dislike nn black pudding
            call ec_aww
        "Uh... I don't know.":
            ""
        
    ec "Okay."
    ec "But... what's your favourite meal?"
    
    menu:
        nn "I'm going to say..."
        "Err... pizza?":
            like nn pizza
            call ec_yea
            ec "Me too!"
        "Definitely sauerkraut.":
            like nn sauerkraut
        "I'm not sure, but the one thing I don't like is pizza.":
            dislike nn pizza
            call ec_aww
            ec "I like pizza, though."
    
    ec "Huh."
    ec "What about your favourite book?"
    menu:
        nn "Hm..."
        "Probably just Harry Potter":
            like nn harry potter
            call ec_aww
            show ebby sad
            ec "I {i}hate{/i} Harry Potter."
        "Lolita.":
            like nn lolita
            call ec_yea
            show ebby rape
            ec "That's my favourite too!"
        "Mein Kampf.":
            like nn mein kampf
            show ebby concerned
            ec "Uhh..."
            ec "That's... pretty special."
    
    $ score = relations(ec.name, nn.name)
    centered "Your score: [score]"
    
    return
    
    label ec_yea:
        show ebby excited
        ec "Yaaay!"
        show ebby joy
        return
    
    label ec_aww:
        show ebby sad
        ec "Aww..."
        show ebby normal
        return
    