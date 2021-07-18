from sys import path
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
import os
import random
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices', voices[1].id)

def speak(test):
   engine.say(test)
   engine.runAndWait()


volume = engine.getProperty('volume')
engine.setProperty('volume',0.9)

rate = engine.getProperty('rate')
engine.setProperty('rate',150)

def wishme():
   hour = int(datetime.datetime.now().hour)
   if hour>=0 and hour<12:
      speak("hello good morning sir")
   elif hour>=12 and hour<18:
      speak("hello sir good afternoon")
   else:
      speak("hello sir good night")

# speak("how can i help you sir")
# speak("how can i help you sir-edited")

wishme()     
speak(" how can i help you and sorry for late submission of the reapo")

r = sr.Recognizer()
with sr.Microphone() as source:
  
    r.pause_threshold=1

    r.adjust_for_ambient_noise(source)

    print("Listening....")
    audio = r.listen(source)
try:
    text = r.recognize_google(audio, language='eng-in')
    query = text.lower()
    print(f'user said :'+ query)
    if 'open youtube' in query:
       webbrowser.open("youtube.com")

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'open stackoverflow' in query:
       webbrowser.open("stackoverflow.com")   

   #  elif 'jarvis i am not happy today' in query:
   #     pyttsx3.speak("why are you not happy sir can i help you as i can possible")    

   #  elif 'jarvis what is your real name' in query:
   #      pyttsx3.speak("sir i know everyone want to know my real name but we are we so i am telling you a secret that some time peolpe call me tonny starc jarvis")
    elif 'wikipedia' in query:
       speak('Searching Wikipedia.........')
       query=query.replace("wikipedia","")
       results=wikipedia.summary(query,sentences=2)
       speak("According to wikipedia")
       print(results)
       speak(results)


    elif 'play music' in query:
       music_dir='D:\\bee'
       songs=os.listdir(music_dir)
       print(songs)


       os.startfile(os.path.join(music_dir,songs[8]))
    elif 'the time' in query:
       strTime = datetime.datetime.now().strftime("%H:%M:%S")
       speak("sir,time jaaan kaarr kyaa karogee aapkaa timee kharabh hi chal raha hai waise the time is " + strTime)


    elif 'open code' in query:
       path = "C:\\Users\\kishan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
       os.startfile(path)


    elif 'open gta' in query:
       gtapath =    "C:\Program Files (x86)\ATH TEAM\Grand Theft Auto San Andreas\gta_sa.exe"
       os.startfile(gtapath)
       

except:
    print("Sorry I am unable to understand. Can you please repeat.")

      