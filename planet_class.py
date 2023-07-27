import math
import pygame
import colors


class Planet:
    def __init__(self, speed, distance_from_sun, color=colors.grey, radius=15):
        self.radius = radius
        self.distance = distance_from_sun
        self.color = color
        self.angle = 0
        self.speed = speed

    def move(self, screen_width, screen_height, screen):
        # Change the planet position

        # Recalculation of coordinates for circular motion
        x = int(math.cos(self.angle) * self.distance) + screen_width / 2
        y = int(math.sin(self.angle) * self.distance) + screen_height / 2

        pygame.draw.circle(surface=screen, color=self.color, center=(x, y), radius=self.radius)

    def draw(self, screen_width, screen_height, screen):
        # Display static planets 

        # Center on screen 
        x = screen_width / 2
        y = screen_height / 2

        pygame.draw.circle(surface=screen, color=self.color, center=(x, y), radius=self.radius)
