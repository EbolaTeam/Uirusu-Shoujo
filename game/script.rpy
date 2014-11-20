
#backgrounds, images, and character definitions have been moved to definitions.rpy

# The game starts here.
label start:
    stop music
    scene bg black
    menu:
        "Demo":
            jump final
        "Skeleton":
            jump actI
    return
