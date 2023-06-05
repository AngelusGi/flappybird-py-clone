import random # For generating random height of pipes
import sys
import pygame
from pygame.locals import *

### Global Variables for the game (480p (4:3)	640 × 480p	4:3)
window_width = 640
window_height = 480
coordinates = (window_width, window_height)

### set height and width of window
window = pygame.display.set_mode(coordinates)
# elevation = window_height * 0.8
fps = 32
pipe_image_path = 'src/assets/images/pipe.png'
background_image_path = 'src/assets/images/background.jpg'
birdplayer_image_path = 'src/assets/images/bird.png'
sealevel_image_path = 'src/assets/images/base.jfif'
