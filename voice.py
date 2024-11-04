import pyttsx3

engien = pyttsx3.init()

voices = engien.getProperty('voices')
engien.setProperty('voice', voices[2].id)

voices = engien.getProperty('rate')
engien.setProperty('rate', 140)

names = [""]

for name in names :
    engien.say(f"shoutout to all the coder")
engien.runAndWait()
