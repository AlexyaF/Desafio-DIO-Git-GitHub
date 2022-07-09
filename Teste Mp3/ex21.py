# tocar MP3
from time import sleep
import pygame
print('\033[1;47;30m=== BTS-Fake Love ===\033[m')
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('sound.mp3')
pygame.mixer.music.play()
sleep(14.5)
print('\033[1;31mLOVE YOU SO BAD\033[m')
sleep(1.3)
print('\033[1;35mLOVE YOU SO BAD \033[m')
sleep(1.6)
print('\033[1;36mLOVE YOU SO BAD \033[m')
sleep(3.5)
print('\033[1;32mLOVE YOU SO BAD \033[m')
pygame.event.wait()
