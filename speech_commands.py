import speech_recognition as sr
import subprocess
import time


r = sr.Recognizer()
mic = sr.Microphone()

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

        while 'hey Albert' not in text:
            with mic as source:
                r.adjust_for_ambient_noise(source, duration=3)
                print("Waiting for wake-up call...")
                audio = r.listen(source)
                text = r.recognize_google(audio)
        with mic as source:
            print('AWAKE')
            print("Please wait. Calibrating microphone...")
            r.adjust_for_ambient_noise(source, duration=3)
            print("Listening")
            audio = r.listen(source)
            text = r.recognize_google(audio)

        print(text)

        words = text.split()
        word_indexes = []
        keyword1 = 'Google' in text
        keyword2 = 'called' in text
        keyword3 = 'search' in text
        keyword4 = 'for' in text

        if 'Google' in text:
            if keyword1 or keyword2 or keyword3 or keyword4:
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

                print('Searching results for ' + search_string + ' on Google...')

                subprocess.Popen(['C:\Program Files (x86)\Google\Chrome\Application\chrome.exe', 'https://www.google.com/search?q=' + search_string])

            else:
                print('Opening a new Chrome browser tab...')
                subprocess.Popen(['C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'])

        elif 'quit' in text or 'exit' in text or 'stop' in text:
            print('Ok, see you later!')
            break

        elif 'Spotify' in text:
            print('Opening Spotify...')
            subprocess.Popen(['C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'])

        elif 'OneNote' in text:
            print('Opening OneNote...')
            subprocess.Popen(['C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'])

        elif 'settings' in text:
            print('Opening settings...')
            subprocess.Popen(['C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'])

        elif 'pycharm' in text:
            print('Opening PyCharm...')
            subprocess.Popen(['C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'])

        elif 'cmd' in text or 'command prompt' in text or 'shell' in text:
            print('Opening the your Windows Command Prompt...')
            subprocess.Popen(['C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'])

        elif 'files' in text or 'File Explorer' in text:
            print('Opening your File Explorer...')
            subprocess.Popen(['C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'])

        else:
            print('I\'m sorry, I didn\'t understand that.')

    except:
        print('Error occurred')
        print('Error message suppressed and Albert initiated program continuation')
        pass

