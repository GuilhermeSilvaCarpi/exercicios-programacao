import pygame

pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play(1, 1, 1)
pygame.event.wait()
