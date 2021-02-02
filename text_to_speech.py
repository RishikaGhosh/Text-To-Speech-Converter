from gtts import gTTS
import os

myText = "Hi! Welcome To the program."

language = 'en'

output = gTTS(text=myText,lang=language,slow=True)

output.save("output.mp3")

os.system("start output.mp3")
