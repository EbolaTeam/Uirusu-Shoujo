init -12 python:
#Ebby dread normal
    autoComposite('dread ebby normal', base="images/sprites/dread/EBOLA/EbbyNormal.png",
    bases={
    'blood':"images/sprites/dread/EBOLA/EbbyBlood.png",
    'skull':"images/sprites/dread/EBOLA/EbbySkull.png",
    'bloodskull':"images/sprites/dread/EBOLA/EbbySkullBlood.png",
    },
    dict={
    'dread ebby wink':"images/sprites/dread/EBOLA/EbbyWink.png",
    'dread ebby concerned':"images/sprites/dread/EBOLA/EbbyConcerned.png",
    'dread ebby excited':"images/sprites/dread/EBOLA/EbbyExcited.png",
    'dread ebby sad':"images/sprites/dread/EBOLA/EbbySad.png",
    'dread ebby rape':"images/sprites/dread/EBOLA/EbbyRape.png",
    'dread ebby joy':"images/sprites/dread/EBOLA/EbbyJoy.png",
    }, wimg=808, himg=1929, 
    xcomp=297, ycomp=188, wcomp=259, hcomp=268,
    lcrop=1060, scrop=1350)
#Ebby dread toast
    autoComposite(base="images/sprites/EBOLA/EbbyNormal.png",
    bases={
    'blood':"images/sprites/EBOLA/EbbyBlood.png",
    'skull':"images/sprites/EBOLA/EbbySkull.png",
    'bloodskull':"images/sprites/EBOLA/EbbySkullBlood.png",
    },
    dict={
    'dread ebby toastdead':"images/sprites/dread/EBOLA/EbbyToastDead.png",
    'dread ebby toastsad':"images/sprites/dread/EBOLA/EbbyToastSad.png",
    'dread ebby toastjoy':"images/sprites/dread/EBOLA/EbbyToastJoy.png",
    }, wimg=808, himg=1929, 
    xcomp=297, ycomp=188, wcomp=259, hcomp=334,
    lcrop=1060, scrop=1350)
#Sars dread
    autoComposite('dread sars normal', base="images/sprites/dread/SARS/SarsNormal.png",
    bases={
    'point':"images/sprites/dread/SARS/SarsPoint.png"
    },
    dict={
    'dread sars notamused':"",
    'dread sars concerned':"images/sprites/dread/SARS/SarsConcerned.png",
    'dread sars grin':"images/sprites/dread/SARS/SarsGrin.png",
    'dread sars sad':"images/sprites/dread/SARS/SarsSad.png",
    'dread sars stars':"images/sprites/dread/SARS/SarsStars.png",
    'dread sars angry':"images/sprites/dread/SARS/SarsAngry.png",
    'dread sars blush':"images/sprites/dread/SARS/SarsRed.png",
    }, wimg=751, himg=1790, 
    xcomp=241, ycomp=129, wcomp=307, hcomp=284,
    lcrop=984, scrop=1200,
    sscale=0.64)