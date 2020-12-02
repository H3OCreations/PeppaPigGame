import pygame, sys, os, random
from pygame import *
'''
Peppa to move around the map using the keyboard (DONE)
Peppa cannot cross the boundaries of the map (DONE)
Peppa should be able to collect the letters on the map that are randomly placed
1. Generate a letter in a fixed place
2. Generate a letter from my list in a fixed place
3. Generate a letter in a random place
4. Peppa should be able to collect the letter
Display the letters that she's collected in the top left corner
'''

# Joins the image name with the working directory path
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
font_size = 48
font = pygame.font.SysFont("Courier New Bold",font_size)
BLACK = (0, 0, 0)
PINK = (255, 153, 255)
LETTERS = ['A', 'B', 'C', 'D']
current_letter = 0
graphics = font.render("A",1,PINK) # render the text as graphics
letter_x = random.randint(0, win_x-font_size)
letter_y = random.randint(0, win_y-font_size)


# In Game Variables
peppaX = 0
peppaY = 0
peppa_length = 102
vel = 20

#---------------------------------------#
# Main Game Loop                        #
#---------------------------------------#

while True: # main game loop
  pygame.time.delay(100)                                    # Game Delay
  win.blit(bg, (0, 0))                                      # Static background of the game
  win.blit(peppa, (peppaX, peppaY))
  
  
  # END GAME
  if current_letter >= len(LETTERS):
    letter = font.render("CONGRATULATIONS",1,PINK)  
    letter_x = win_x/3
    letter_y = win_y/2
  # Generate the letter of the alphabet
  else:
    letter = font.render(LETTERS[current_letter],1,PINK)    # render the text as graphics
  
  win.blit(letter,(letter_x, letter_y))                     # draw the graphics on the gameWindow surface
  
  keys = pygame.key.get_pressed()                           # Getting keys sensed
  
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  
  # Keyboard interaction to move Peppa
  # Window is 800x600
  if keys[pygame.K_UP]:
    if peppaY > 0:
      peppaY = peppaY - vel
  if keys[pygame.K_DOWN]:
    if peppaY < win_y - peppa_length:
      peppaY = peppaY + vel 
  if keys[pygame.K_RIGHT]:
    if peppaX < win_x - peppa_length:
      peppaX = peppaX + vel
  if keys[pygame.K_LEFT]:
    if peppaX > 0:
      peppaX = peppaX - vel        
      
  # Collision with the letter

  # Approaching from the right has issues AND from below have abnormally large ranges
  if abs(letter_x - peppaX) < font_size + vel and abs(letter_y - peppaY) < font_size:
    # abs(-10) --> 10
    # abs(10) --> 10
    success.play()
    letter_x = random.randint(0, win_x-font_size)
    letter_y = random.randint(0, win_y-font_size)
    current_letter = current_letter + 1
    

  pygame.display.update()