import sys
import pygame

from planet_class import Planet  # import class from external file 
from planets_info import *  # import planets' speed and colors from external file 
import colors  # import colors setup 

# Define window's dimensions 
size = width, height = 760, 760  

# Initialize pygame 
pygame.init()
# Setup the program window
pygame.display.set_caption('Solar System Model')  # window title 
screen = pygame.display.set_mode(size)  # create scren object with the dimensions 

center = (width/2, height/2) # calculate the screen center 
clock = pygame.time.Clock()  # create clock object (for fps)
speed = 1  # default play speed is 1

# Playback controls 
run = True  # program is active and running 
move = True  # playback control, or pause planets' movement 

# Create Sun as Planet object 
# As the science says, the Sun is in the center of the Solar System
sun = Planet(radius=20, distance_from_sun=0, color=colors.sun_color, speed=0)
# Define planets' distances from sun 
distances = [50, 90, 130, 170, 210, 250, 300, 350]

# Create planets 
mercury = Planet(distance_from_sun=distances[0], speed=mercury_s, color=colors.mercury_color)
venus = Planet(distance_from_sun=distances[1], speed=venus_s, color=colors.venus_color)
earth = Planet(distance_from_sun=distances[2], speed=earth_s, color=colors.earth_color)
mars = Planet(distance_from_sun=distances[3], speed=mars_s, color=colors.mars_color)
jupiter = Planet(distance_from_sun=distances[4], speed=jupiter_s, color=colors.jupiter_color)
saturn = Planet(distance_from_sun=distances[5], speed=saturn_s, color=colors.saturn_color)
uran = Planet(distance_from_sun=distances[6], speed=uran_s, color=colors.uran_color)
neptun = Planet(distance_from_sun=distances[7], speed=neptun_s, color=colors.neptun_color)
# Collect the planets into a list 
planets = [mercury, venus, earth, mars, jupiter, saturn, uran, neptun]


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
                    if move:
                        move = False
                    elif not move:
                        move = True

                # Speed configuration and change 
                if event.key == pygame.K_0:
                    speed = 1  # default speed 
                if event.key == pygame.K_2:
                    speed = 2  # speed x2
                if event.key == pygame.K_5:
                    speed = 0.5 # speed x0.5
                if event.key == pygame.K_1:
                    speed = 0.1  # speed x0.1

        # Draw everything on the screen in the order of layout: BG - orbits - Sun & planets 

        # Fill BG color 
        screen.fill(colors.black)
        # Draw orbit circles 
        for dist in distances:
            pygame.draw.circle(surface=screen, color=colors.grey, center=center, radius=dist, width=1)
        # Draw the Sun
        sun.draw(screen=screen, screen_width=width, screen_height=height)
        # Draw the planets 
        for planet in planets:
            planet.move(screen=screen, screen_width=width, screen_height=height)

        # Update the screen 
        pygame.display.flip()

        # Move planets on the next cycle run, if playback isn't paused 
        if move:
            for planet in planets:
                planet.angle += planet.speed * speed

