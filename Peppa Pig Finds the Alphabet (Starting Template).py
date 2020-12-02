import pygame, sys, os, random
from pygame import *

def get_path(img_name, join='\\'):
  return os.getcwd() + join + img_name

# Start up pygame
pygame.init()

#---------------------------------------#
# Game Window                           #
#---------------------------------------#
win_x = 800
win_y = 600
win = pygame.display.set_mode((win_x, win_y))
pygame.display.set_caption('Peppa Pig Finds the Alphabet')

#---------------------------------------#
# Loading Pictures                      #
#---------------------------------------#
# Image names
peppa_img_right = 'peppa_pig_right.png'
peppa_img_left = 'peppa_pig_left.png'
bg_img = 'peppa_background.png'

# Loading Images
peppa_right = pygame.image.load(get_path(peppa_img_right))
peppa_left  = pygame.image.load(get_path(peppa_img_left))
bg = pygame.image.load(get_path(bg_img))

peppa = peppa_right                        # Default Case

#---------------------------------------#
# Sound Mixer                           #
#---------------------------------------#
# File Names
bg_music = 'peppa_pig_music.mp3'
correct_music = 'approved-mission.wav'
losing_music = 'losing-or-failing.wav'

# Setting up Background Music
pygame.mixer.music.load(get_path(bg_music))
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(loops = -1)

# Success Sound Effect
success = pygame.mixer.Sound(get_path(correct_music))
success.set_volume(0.05)

# Fail Sound Effect
fail = pygame.mixer.Sound(get_path(losing_music))
fail.set_volume(0.05)

#---------------------------------------#
# Font Setup                            #
#---------------------------------------#
font = pygame.font.SysFont("Courier New Bold",48)
BLACK = (0, 0, 0)
PINK = (255, 153, 255)
letters = ['A', 'B', 'C', 'D']
current_letter = 0
graphics = font.render("LETTER!",1,PINK) # render the text as graphics
BANNER_1 = font.render("Help Peppa Pig Collect", 1, BLACK)
BANNER_2 = font.render('all the letters of the alphabet!', 1, BLACK)


#---------------------------------------#
# Main Game Loop                        #
#---------------------------------------#

while True: # main game loop
  pygame.time.delay(100)            # Game Delay
  win.blit(bg, (0, 0))              # Static background of the game
  win.blit(peppa, (0, 0))
  win.blit(BANNER_1, (200,0))
  win.blit(BANNER_2, (200, 50))
  win.blit(graphics,(200,200))      # draw the graphics on the gameWindow surface
  keys = pygame.key.get_pressed()   # Getting keys sensed
  
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

  pygame.display.update()