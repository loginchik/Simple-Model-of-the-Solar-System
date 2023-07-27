import sys
import pygame
import json
from create_objects import sun, planets, planet_distances  

with open('data/colors.json') as colors_json_file: colors = json.load(colors_json_file)
default_planets_color = (192, 192, 192)

# Define window's dimensions 
size = width, height = 760, 760  

# Initialize pygame 
pygame.init()
# Setup the program window
pygame.display.set_caption('Solar System Model')  # window title 
screen = pygame.display.set_mode(size)  # create scren object with the dimensions 

center = (width / 2, height / 2) # calculate the screen center 
clock = pygame.time.Clock()  # create clock object (for fps)
speed = 1  # default play speed is 1

# Playback controls 
run = True  # program is active and running 
move = True  # playback control, or pause planets' movement 

if __name__ == "__main__":
    # Program cycle 
    while run:
        clock.tick(60)  # fps 

        # Processing incoming events 
        for event in pygame.event.get():

            # Program quit action 
            if event.type == pygame.QUIT:
                run = False  # break the while cycle 
                pygame.quit()  # close pygame window
                sys.exit()  # end the program 

            # Keyboard events 
            if event.type == pygame.KEYDOWN:
                # Pause/unpause, if space key is pressed 
                if event.key == pygame.K_SPACE:
                    if move: move = False
                    elif not move: move = True

                # Speed configuration and change 
                if event.key == pygame.K_0: speed = 1  # default speed 
                if event.key == pygame.K_2: speed = 2  # speed x2
                if event.key == pygame.K_5: speed = 0.5 # speed x0.5
                if event.key == pygame.K_1: speed = 0.1  # speed x0.1

        # Draw everything on the screen in the order of layout: BG - orbits - Sun & planets 

        # Fill BG color 
        screen.fill(colors.get('defaults', {}).get('black', default_planets_color))
        # Draw orbit circles 
        for dist in planet_distances:
            pygame.draw.circle(surface=screen, 
                               color=colors.get('defaults', {}).get('grey', default_planets_color), 
                               center=center, radius=dist, width=1)
        # Draw the Sun
        sun.draw(screen=screen, screen_width=width, screen_height=height)
        # Draw the planets 
        for planet in planets: planet.move(screen=screen, screen_width=width, screen_height=height)

        # Update the screen 
        pygame.display.flip()

        # Move planets on the next cycle run, if playback isn't paused 
        if move: 
            for planet in planets: planet.angle += planet.speed * speed
