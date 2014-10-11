label Shrines:

  $shrinecount=73
  $counter=1

  scene bg black with fade
  centered "{i}TRIGGER WARNING{/i}"
  centered "{i}This is the Ebola-chan Cult{/i}"
  centered "{i}Some images may be disturbing{/i}"

  $renpy.music.set_volume (1.0, channel="music")
  play music "O_Fortuna.mp3" noloop

  while counter <= shrinecount:
    $renpy.scene()
    $renpy.show("bg s"+"%02d" % counter)
    pause(1)
    $counter+=1
  pause(3)

  stop music

  return