
#backgrounds, images, and character definitions have been moved to definitions.rpy

# The game starts here.
label start:
    stop music
    scene bg black
    jump final
    menu:
        "Final":
            jump final
        "Origins":
            jump Origins
        "Shrines":
            jump Shrines
        "Africa":
            jump Africa
        "Xebs Stuff":
            jump Xebstuff
        "Rydeas":
            jump rydeas
        "Linder":
            jump linderstuff
        "Ebola Rat":
            jump EbolaRat
        "Alike API Test":
            jump alike
        "roisaber":
            jump roisaber
        "Ryan's Aids route":
            jump rydeasPureAids
    return
