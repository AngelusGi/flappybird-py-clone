import random # For generating random height of pipes
import sys
import pygame
from pygame.locals import *

### Global Variables for the game (480p (4:3)	640 × 480p	4:3)
window_width = 640
window_height = 480
coordinates = (window_width, window_height)
image_asset_path = 'src/assets/images'

### set height and width of window
window = pygame.display.set_mode(coordinates)
sealevel_elevation = window_height * 0.8
fps = 32
pipe_image_path = f'{image_asset_path}/pipe.png'
background_image_path = f'{image_asset_path}/background.jpg'
birdplayer_image_path = f'{image_asset_path}/bird.png'
sealevel_image_path = f'{image_asset_path}/base.jfif'
game_images = {}

# program where the game starts
if __name__ == "__main__":		
	
	# For initializing modules of pygame library
	pygame.init()
	framepersecond_clock = pygame.time.Clock()
	
	# Sets the title on top of game window
	pygame.display.set_caption('Flappy Bird Game')	

	# Load all the images which we will use in the game
	# images for displaying score
	game_images['scoreimages'] = (
		pygame.image.load(f'{image_asset_path}/0.png').convert_alpha(),
		pygame.image.load(f'{image_asset_path}/1.png').convert_alpha(),
		pygame.image.load(f'{image_asset_path}/2.png').convert_alpha(),
		pygame.image.load(f'{image_asset_path}/3.png').convert_alpha(),
		pygame.image.load(f'{image_asset_path}/4.png').convert_alpha(),		
		pygame.image.load(f'{image_asset_path}/5.png').convert_alpha(),
		pygame.image.load(f'{image_asset_path}/6.png').convert_alpha(),
		pygame.image.load(f'{image_asset_path}/7.png').convert_alpha(),
		pygame.image.load(f'{image_asset_path}/8.png').convert_alpha(),
		pygame.image.load(f'{image_asset_path}/9.png').convert_alpha()
	)
	game_images['flappybird'] = pygame.image.load(birdplayer_image_path).convert_alpha()				
	game_images['sea_level'] = pygame.image.load(sealevel_image_path).convert_alpha()
	game_images['background'] = pygame.image.load(background_image_path).convert_alpha()
	game_images['pipeimage'] = (pygame.transform.rotate(pygame.image.load(pipe_image_path).convert_alpha(),180),
								pygame.image.load(pipe_image_path).convert_alpha())

	print("WELCOME TO THE FLAPPY BIRD GAME")
	print("Press space or enter to start the game")

while True:

		# sets the coordinates of flappy bird
		horizontal = int(window_width/5)
		vertical = int((window_height - game_images['flappybird'].get_height())/2)
		
		# for selevel
		ground = 0
		while True:
			for event in pygame.event.get():

				# if user clicks on cross button, close the game
				if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
					pygame.quit()
					
					# Exit the program
					sys.exit()

				# If the user presses space or up key,
				# start the game for them
				elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
					flappygame()
				
				# if user doesn't press anykey Nothing happen
				else:
					window.blit(game_images['background'], (0, 0))
					window.blit(game_images['flappybird'], (horizontal, vertical))
					window.blit(game_images['sea_level'], (ground, sealevel_elevation))
					
					# Just Refresh the screen
					pygame.display.update()		
					
					# set the rate of frame per second
					framepersecond_clock.tick(fps)
