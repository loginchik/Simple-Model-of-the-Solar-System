import math
import pygame
import colors


class Planet:
    """Planet class that is used to draw and move the planet during the program run
    
    To create an object, speed and distance_from_sun are required. 
    Color and raduis are optional; defaults are color=grey and raduis=15.
    """
    def __init__(self, speed: float, distance_from_sun: int, 
                 color: tuple[int, int, int] = colors.grey, radius: int = 15) -> None:
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
        self.speed = speed

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
