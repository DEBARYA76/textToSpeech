from gtts import gTTS
import os
from pygame import mixer
import time
speech=input("Enter the text you want to convert to speech: ")
tts = gTTS(text=speech, lang='en')
tts.save('speech.mp3')
mixer.init()
mixer.music.load('speech.mp3')
mixer.music.play()
while mixer.music.get_busy():
    time.sleep(1)
os.remove('speech.mp3')