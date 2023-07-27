import math
import pygame
import json 

""" Prepare data to create planets """

# Read info file 
with open('data/info.json') as info_file: info = json.load(info_file)
# Read colors' file
with open('data/colors.json') as colors_json_file: colors = json.load(colors_json_file)
default_planets_color = (192, 192, 192)

# Define planets' names
planet_names = list(info.keys())
# The velocity of the planets relative to the velocity of the Earth
revolution_days = [info[planet]['revolution'] for planet in planet_names]
# Define custom distances from sun in the program 
planet_distances = [info[planet]['distance'] for planet in planet_names]
# Define planet colors 
planet_colors = [colors.get('planets', {}).get(planet, default_planets_color) for planet in planet_names]

""" Create the class """

class Planet:
    """Planet class that is used to draw and move the planet during the program run
    
    To create an object, speed and distance_from_sun are required. 
    Color and raduis are optional; defaults are color=grey and raduis=15.
    """
    def __init__(self, revolution_days: float, distance_from_sun: int, 
                 color: tuple[int, int, int] = default_planets_color, radius: int = 15) -> None:
        """Create a planet method.

        Args:
            speed (float): planet's default velocity.
            distance_from_sun (int): the raduius of planet's orbit. 
            color (tuple[int, int, int], optional): color in RGB format. Defaults to colors.grey.
            radius (int, optional): raduis of planet's circle to draw. Defaults to 15.
        """
        
        self.radius = radius
        self.distance = distance_from_sun
        self.color = color
        self.angle = 0
        try:
            self.speed = float(str(365 / revolution_days * 0.05))
        except ZeroDivisionError:
            self.speed = 0

    def move(self, screen_width: int, screen_height: int, screen: pygame.Surface) -> None:
        """Draws a circle on the calculated position.

        Args:
            screen_width (int): screen's, where to draw, width.
            screen_height (int): screen's, where to draw, height.
            screen (pygame.Surface): screen to draw on.
        """

        # Recalculation of coordinates for circular motion
        x = int(math.cos(self.angle) * self.distance) + screen_width / 2
        y = int(math.sin(self.angle) * self.distance) + screen_height / 2
        # Draw
        pygame.draw.circle(surface=screen, color=self.color, center=(x, y), radius=self.radius)

    def draw(self, screen_width: int, screen_height: int, screen: pygame.Surface) -> None:
        """Draws static circle, for example the Sun. 

        Args:
            screen_width (int): screen's, where to draw, width.
            screen_height (int): screen's, where to draw, height.
            screen (pygame.Surface): screen to draw on.
        """
        
        # Center on screen 
        x = screen_width / 2
        y = screen_height / 2
        # Draw
        pygame.draw.circle(surface=screen, color=self.color, center=(x, y), radius=self.radius)


""" Create planets and the Sun """

# Create Sun as Planet object 
# As the science says, the Sun is in the center of the Solar System
sun = Planet(radius=20, distance_from_sun=0, 
             color=colors.get('planets', {}).get('sun', default_planets_color), 
             revolution_days=0)
# Create planets 
planets = [Planet(distance_from_sun=dist, revolution_days=rev, color=col) 
           for dist, rev, col in zip(planet_distances, revolution_days, planet_colors)]