from pygame import mixer
mixer.init()
mixer.music.load('ringtone.mp3')
mixer.music.play()
input('Agora você escuta?')
