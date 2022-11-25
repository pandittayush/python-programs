import pyttsx3
import wikipedia
#hii git how are you
bhai = pyttsx3.init()
voices = bhai.getProperty('voices')
bhai.setProperty('voice', voices[1].id)  #For female voice
In = input("Search wikipedia//Google: ")
result = wikipedia.summary(In, sentences = 2)
bhai.say("According to wikipedia")
print(result)
bhai.say(result)
bhai.say("Thanks for listening me")
bhai.runAndWait()