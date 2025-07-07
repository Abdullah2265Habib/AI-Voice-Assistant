import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('rate', 150)
#print(voices[1].id)
for voice in voices:
    if "Zira" in voice.name:
        engine.setProperty('voice', voice.id)

#engine.setProperty('voices',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak("Good Morning!")
    elif hour >=12 and hour <17:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis!\n")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...\n")
        query=r.recognize_google(audio,language="en-in")
        print(f"User Says: {query}\n")
    except Exception as e:
        print(e)
        print("say that again please!")
        return "None"
    return query    
if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            print("Searching Wikipedia...\n")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=5)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("Youtube.com")
        elif 'open leetcode' in query:
            webbrowser.open("leetcode.com")
        elif 'play the music' in query:
            music_dir = "D:\\Songs"
            songs = [f for f in os.listdir(music_dir) if f.lower().endswith(('.mp3', '.wav', '.mp4', '.mkv', '.avi'))]
    
            if songs:
                try:
                    song_path = os.path.join(music_dir, songs[0])
                    os.startfile(song_path)
                    speak("Playing your video or music.")
                except Exception as e:
                    speak("Sorry, I couldn't play the file.")
                    print(f"Error playing file: {e}")
            else:
                speak("No playable media files found in the folder.")

        elif 'the time' in query:
            t=datetime.datetime.now().strftime("%H:%M,%S")
            speak(f"The Time is {t}")
        elif 'exit' in query or 'quit' in query:
            speak("Exiting")
            print("Exiting...\n")
            break
        else:
            speak("I don't understand!. please say it again!")
            print("I don't understand!. please say it again!\n")
            query=""
            continue
