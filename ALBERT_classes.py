import speech_recognition as sr
import subprocess
import pyttsx3
import pygame
import time
import os


#######################################PyGame Setup#####################################################################
os.environ['SDL_VIDEO_WINDOW_POS'] = '100,50'

pygame.init()

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 500
font_size = 18

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
basicFont = pygame.font.SysFont(None, font_size)
pygame.display.set_caption('Test')

white = (255, 255, 255)
black = (0, 0, 0)

screen.fill(white)
pygame.draw.rect(screen, black, (5, 5, 290, 999999))
pygame.draw.rect(screen, white, (7, 7, 286, 999999))

pygame.display.update()
#################################################Defining Variables#####################################################

r = sr.Recognizer()
mic = sr.Microphone()

engine = pyttsx3.init()
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')
voices = engine.getProperty('voices')

rate_input = 125
volume_input = 0.8

engine.setProperty('rate', rate_input)
engine.setProperty('volume', volume_input)
engine.setProperty('voice', voices[0].id)

pixels_from_top = 10

################################################Functions###############################################################
pygame.event.clear()


def pygame_text(string, pixels_from_top):
    pygame.event.clear()
    if pixels_from_top > 400:
        pygame.draw.rect(screen, white, (295, 5, 5, 999999))
        pygame.event.clear()
        pygame.Surface.scroll(screen, dx=0, dy=-20)
        pygame.event.clear()
        pygame.display.update()
        pixels_from_top -= 16

    pygame.draw.rect(screen, white, (295, 5, 5, 999999))
    pygame.event.clear()
    text = basicFont.render(string, True, black)
    text_rect = text.get_rect()
    pygame.event.clear()
    text_rect.update((10, pixels_from_top, text_rect.width, text_rect.height))
    screen.blit(text, text_rect)
    pygame.event.clear()
    pygame.display.update()

    pixels_from_top += 16
    pygame.event.clear()
    return pixels_from_top

###########################################Main Loop####################################################################

pygame.event.clear()
pixels_from_top = pygame_text('Albert initialization sequence activated...', pixels_from_top)
time.sleep(2)
pixels_from_top = pygame_text('Firing start enzymes...', pixels_from_top)
time.sleep(0.3)
pixels_from_top = pygame_text('Creating new virtual environment...', pixels_from_top)
time.sleep(0.3)
pixels_from_top = pygame_text('Warming up servers...', pixels_from_top)
time.sleep(0.4)
pixels_from_top = pygame_text('Fetching cookie jar...', pixels_from_top)
time.sleep(1)
pixels_from_top = pygame_text('Extracting HTML elements...', pixels_from_top)
time.sleep(0.5)
pixels_from_top = pygame_text('Extracting CSS stylesheets...', pixels_from_top)
time.sleep(0.5)
pixels_from_top = pygame_text('Rendering new Python ide...', pixels_from_top)
time.sleep(0.6)
pixels_from_top = pygame_text('Rendering new Javascript console...', pixels_from_top)
time.sleep(0.4)
pixels_from_top = pygame_text('Initialization 95% complete...', pixels_from_top)
time.sleep(0.8)
pixels_from_top = pygame_text('Starting up Albert\'s back messaging chair...', pixels_from_top)
time.sleep(1)
pixels_from_top = pygame_text('Fetching iced oolong tea...', pixels_from_top)
time.sleep(1)
pixels_from_top = pygame_text('Initialization complete', pixels_from_top)
pixels_from_top = pygame_text('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~', pixels_from_top)
pixels_from_top = pygame_text('ALBERT', pixels_from_top)

pygame.event.clear()

while True:
    pygame.event.clear()

    try:
        text = ''

        while 'Albert' not in text:
            with mic as source:
                pygame.event.clear()
                r.adjust_for_ambient_noise(source, duration=1)
                pygame.event.clear()
                pixels_from_top = pygame_text("Waiting for wake-up call...", pixels_from_top)
                pygame.event.clear()
                audio = r.listen(source)
                pygame.event.clear()
                text = r.recognize_google(audio)
                pygame.event.clear()

        with mic as source:
            pixels_from_top = pygame_text('AWAKE', pixels_from_top)
            pixels_from_top = pygame_text('Please wait. Calibrating microphone...', pixels_from_top)
            engine.say("Please wait. Calibrating microphone...", pixels_from_top)
            pygame.event.clear()
            engine.runAndWait()
            pygame.event.clear()
            r.adjust_for_ambient_noise(source, duration=1)
            pixels_from_top = pygame_text('Listening', pixels_from_top)
            pygame.event.clear()
            engine.say("Listening")
            engine.runAndWait()
            pygame.event.clear()
            audio = r.listen(source)
            pygame.event.clear()
            text = r.recognize_google(audio)
            pygame.event.clear()

        pixels_from_top = pygame_text(text, pixels_from_top)

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
                    if check1 or check2 or check3 or check4:
                        word_indexes.append(index + 1)

                search_content = words[word_indexes.pop():]
                search_string = ''

                if search_content[len(search_content) - 1] == 'please' or search_content[len(search_content) - 1] == 'Albert':
                    search_content.remove(search_content[search_content.index(search_content[len(search_content) - 1]):])

                for word in search_content:
                    search_string += word
                    search_string += ' '

                pygame.event.clear()
                engine.say('Searching results for ' + search_string + 'on Google...')
                engine.runAndWait()
                pixels_from_top = pygame_text('Searching results on Google...', pixels_from_top)

                pygame.event.clear()
                subprocess.Popen(['C:\Program Files (x86)\Google\Chrome\Application\chrome.exe', 'https://www.google.com/search?q=' + search_string])
                pygame.event.clear()

            else:
                engine.say('Opening a new browser tab...')
                pygame.event.clear()
                engine.runAndWait()
                pixels_from_top = pygame_text('Opening a new Chrome browser tab...', pixels_from_top)
                pygame.event.clear()
                subprocess.Popen(['C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'])
                pygame.event.clear()
            executed = 1

        if 'Spotify' in text:
            engine.say('Opening Spotify...')
            engine.runAndWait()
            pixels_from_top = pygame_text('Opening Spotify...', pixels_from_top)
            pygame.event.clear()
            os.startfile(r'C:\Users\Mason Choi\Desktop\Spotify.lnk')
            pygame.event.clear()
            executed = 1

        if 'OneNote' in text:
            engine.say('Opening OneNote...')
            engine.runAndWait()
            pixels_from_top = pygame_text('Opening OneNote...', pixels_from_top)
            pygame.event.clear()
            os.startfile(r'C:\Users\Mason Choi\Desktop/OneNote for Windows 10.lnk')
            pygame.event.clear()
            executed = 1

        if 'settings' in text:
            engine.say('Opening settings...')
            engine.runAndWait()
            pixels_from_top = pygame_text('Opening settings...', pixels_from_top)
            pygame.event.clear()
            os.startfile(r'C:\Users\Mason Choi\Desktop\Settings.lnk')
            pygame.event.clear()
            executed = 1

        if 'pycharm' in text:
            engine.say('Opening PyCharm...')
            engine.runAndWait()
            pixels_from_top = pygame_text('Opening PyCharm...', pixels_from_top)
            pygame.event.clear()
            os.startfile(r'C:\Users\Mason Choi\Desktop\PyCharm Community Edition 2020.3.3.lnk', pixels_from_top)
            pygame.event.clear()
            executed = 1

        if 'cmd' in text or 'command prompt' in text or 'shell' in text:
            engine.say('Opening your Windows Command Prompt...')
            engine.runAndWait()
            pixels_from_top = pygame_text('Opening the your Windows Command Prompt...', pixels_from_top)
            pygame.event.clear()
            os.startfile(r'C:\Users\Mason Choi\Desktop\Command Prompt.lnk')
            pygame.event.clear()
            executed = 1

        if 'files' in text or 'file explorer' in text:
            engine.say('Opening Your File Explorer...')
            engine.runAndWait()
            pixels_from_top = pygame_text('Opening your File Explorer...', pixels_from_top)
            pygame.event.clear()
            os.startfile(r'C:\Users\Mason Choi\Desktop\File Explorer.lnk')
            pygame.event.clear()
            executed = 1

        if 'camera' in text or 'picture' in text:
            engine.say('Opening Camera...')
            engine.runAndWait()
            pixels_from_top = pygame_text('Opening camera...', pixels_from_top)
            pygame.event.clear()
            os.startfile(r'C:\Users\Mason Choi\Desktop\Camera.lnk', pixels_from_top)
            pygame.event.clear()
            executed = 1

        if 'calculator' in text:
            engine.say('Opening Calculator...')
            engine.runAndWait()
            pixels_from_top = pygame_text('Opening calculator...', pixels_from_top)
            pygame.event.clear()
            os.startfile(r'C:\Users\Mason Choi\Desktop\Calculator.lnk')
            pygame.event.clear()
            executed = 1

        if 'quit' in text or 'exit' in text or 'stop' in text:
            pygame.event.clear()
            engine.say('Ok, see you later!')
            engine.runAndWait()
            engine.stop()
            pixels_from_top = pygame_text('Ok, see you later!', pixels_from_top)
            break

        if executed == 0:
            pygame.event.clear()
            engine.say('Sorry, I did not understand that.')
            pixels_from_top = pygame_text('I\'m sorry, I didn\'t understand that.', pixels_from_top)

    except:
        pygame.event.clear()
        pixels_from_top = pygame_text('Error occurred', pixels_from_top)
        pixels_from_top = pygame_text('Error message suppressed', pixels_from_top)
        pygame.event.clear()
        pass
