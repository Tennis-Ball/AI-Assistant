import speech_recognition as sr
import pyttsx3
import subprocess
import os
import time


r = sr.Recognizer()
mic = sr.Microphone()

engine = pyttsx3.init()
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')
voices = engine.getProperty('voices')

engine.setProperty('rate', 125)
engine.setProperty('volume', 0.8)
engine.setProperty('voice', voices[0].id)

print('Albert initialization sequence activated...')
time.sleep(2)
print('Firing start enzymes...')
time.sleep(0.3)
print('Creating new virtual environment...')
time.sleep(0.3)
print('Warming up servers...')
time.sleep(0.4)
print('Fetching cookie jar...')
time.sleep(1)
print('Extracting HTML elements...')
time.sleep(0.5)
print('Extracting CSS stylesheets...')
time.sleep(0.5)
print('Rendering new Python ide...')
time.sleep(0.6)
print('Rendering new Javascript console...')
time.sleep(0.4)
print('Initialization 95% complete...')
time.sleep(0.8)
print('Starting up Albert\'s back messaging chair...')
time.sleep(1)
print('Fetching iced oolong tea...')
time.sleep(1)
print('Initialization complete\n')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
print('ALBERT\n')
while True:
    try:
        text = ''

        while 'Albert' not in text:
            with mic as source:
                #print('Current ambient energy: ' + r.energy_threshold)
                r.adjust_for_ambient_noise(source, duration=1)
                print("Waiting for wake-up call...")
                audio = r.listen(source)
                text = r.recognize_google(audio)
        with mic as source:
            # print('AWAKE')
            # time.sleep(1)
            # engine.say("Please wait. Calibrating microphone...")
            # engine.runAndWait()
            # print('Please wait. Calibrating microphone...')
            r.adjust_for_ambient_noise(source, duration=1)
            # time.sleep(1)
            # engine.say("Listening")
            # engine.runAndWait()
            print('Listening')
            audio = r.listen(source)
            text = r.recognize_google(r.listen(source))
            #text = 'Open Google'

        print(text)

        words = text.split()
        word_indexes = []
        executed = 0

        if 'Google' in text or 'tab' in text or 'search' in text:
            if 'called' in text or 'search' in text or 'for' in text:
                for index in range(len(words)):
                    check1 = words[index] == 'Google'
                    check2 = words[index] == 'called'
                    check3 = words[index] == 'search'
                    check4 = words[index] == 'for'
                    if check1 or check2 or check3 or check4: #returning true on all for some reason
                        word_indexes.append(index + 1)

                search_content = words[word_indexes.pop():]
                search_string = ''

                if search_content[len(search_content) - 1] == 'please' or search_content[len(search_content) - 1] == 'Albert':
                    search_content.remove(search_content[search_content.index(search_content[len(search_content) - 1]):])

                for word in search_content:
                    search_string += word
                    search_string += ' '

                engine.say('Searching results for ' + search_string + 'on Google...')
                engine.runAndWait()
                print('Searching results for ' + search_string + 'on Google...')

                subprocess.Popen(['C:\Program Files (x86)\Google\Chrome\Application\chrome.exe', 'https://www.google.com/search?q=' + search_string])

            else:
                engine.say('Opening a new Chrome browser tab...')
                engine.runAndWait()
                print('Opening a new Chrome browser tab...')
                subprocess.Popen(['C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'])
            executed = 1

        if 'Spotify' in text:
            engine.say('Opening Spotify...')
            engine.runAndWait()
            print('Opening Spotify...')
            os.startfile(r'C:\Users\Mason Choi\Desktop\Spotify.lnk')
            executed = 1

        if 'OneNote' in text:
            engine.say('Opening OneNote...')
            engine.runAndWait()
            print('Opening OneNote...')
            os.startfile(r'C:\Users\Mason Choi\Desktop/OneNote for Windows 10.lnk')
            executed = 1

        if 'settings' in text:
            engine.say('Opening settings...')
            engine.runAndWait()
            print('Opening settings...')
            os.startfile(r'C:\Users\Mason Choi\Desktop\Settings.lnk')
            executed = 1

        if 'pycharm' in text:
            engine.say('Opening PyCharm...')
            engine.runAndWait()
            print('Opening PyCharm...')
            os.startfile(r'C:\Users\Mason Choi\Desktop\PyCharm Community Edition 2020.3.3.lnk')
            executed = 1

        if 'cmd' in text or 'command prompt' in text or 'shell' in text:
            engine.say('Opening your Windows Command Prompt...')
            engine.runAndWait()
            print('Opening the your Windows Command Prompt...')
            os.startfile(r'C:\Users\Mason Choi\Desktop\Command Prompt.lnk')
            executed = 1

        if 'files' in text or 'file explorer' in text:
            engine.say('Opening Your File Explorer...')
            engine.runAndWait()
            print('Opening your File Explorer...')
            os.startfile(r'C:\Users\Mason Choi\Desktop\File Explorer.lnk')
            executed = 1

        if 'camera' in text or 'picture' in text:
            engine.say('Opening Camera...')
            engine.runAndWait()
            print('Opening camera...')
            os.startfile(r'C:\Users\Mason Choi\Desktop\Camera.lnk')
            executed = 1

        if 'calculator' in text:
            engine.say('Opening Calculator...')
            engine.runAndWait()
            print('Opening calculator...')
            os.startfile(r'C:\Users\Mason Choi\Desktop\Calculator.lnk')
            executed = 1

        if 'quit' in text or 'exit' in text or 'stop' in text:
            engine.say('Ok, see you later!')
            engine.runAndWait()
            engine.stop()
            print('Ok, see you later!')
            break

        if executed == 0:
            engine.say('Sorry, I did not understand that.')
            print('I\'m sorry, I didn\'t understand that.')

    except:
        print('Error occurred')
        print('Error message suppressed and Albert initiated program continuation')
        pass

exit()
