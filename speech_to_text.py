import speech_recognition as sr
import subprocess
import os


r = sr.Recognizer()
mic = sr.Microphone()

while True:
    with mic as source:
        print("Please wait. Calibrating microphone...")
        r.adjust_for_ambient_noise(source, duration=3)
        print("Ready")
        audio = r.listen(source)
    try:
        print(r.recognize_google(audio))

    except sr.UnknownValueError or sr.RequestError:
        print('Sorry, I didn\'t understand that, please speak again')
        with mic as source:
            print("Please wait. Calibrating microphone...")
            r.adjust_for_ambient_noise(source, duration=3)
            print("Ready")
            audio = r.listen(source)

