import sys

import pygame

# Импорт класса планеты из файла
from planet_class import Planet

# Импорт дополнительной информации: скорости движения планет и цветов
from planets_info import *
import colors

# Определение размеров окна программы
size = width, height = 760, 760

# Инициализация pygame
pygame.init()

# Настройка окна программы
pygame.display.set_caption('Solar System Model')
screen = pygame.display.set_mode(size)

# Определение центра экрана
center = (width/2, height/2)

# Определение часов для частоты смены кадров
clock = pygame.time.Clock()

# Скорость воспроизведения, по умолчанию равна 1
speed = 1

# Переменные для контроля воспроизведения
run = True
move = True

# Определение Солнца
sun = Planet(radius=20, distance_from_sun=0, color=colors.sun_color, speed=0)

# Список расстояний планет от Солнца
distances = [50, 90, 130, 170, 210, 250, 300, 350]

# Создание планет
mercury = Planet(distance_from_sun=distances[0],
                 speed=mercury_s,
                 color=colors.mercury_color)
venus = Planet(distance_from_sun=distances[1],
               speed=venus_s,
               color=colors.venus_color)
earth = Planet(distance_from_sun=distances[2],
               speed=earth_s,
               color=colors.earth_color)
mars = Planet(distance_from_sun=distances[3],
              speed=mars_s,
              color=colors.mars_color)
jupiter = Planet(distance_from_sun=distances[4],
                 speed=jupiter_s,
                 color=colors.jupiter_color)
saturn = Planet(distance_from_sun=distances[5],
                speed=saturn_s,
                color=colors.saturn_color)
uran = Planet(distance_from_sun=distances[6],
              speed=uran_s,
              color=colors.uran_color)
neptun = Planet(distance_from_sun=distances[7],
                speed=neptun_s,
                color=colors.neptun_color)

# Список планет
planets = [mercury, venus, earth, mars, jupiter, saturn, uran, neptun]

# Цикл программы
while run:
    clock.tick(60)

    # Обработка входящих событий
    for event in pygame.event.get():

        # Закрытие программы
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()

        # События с клавиатуры
        if event.type == pygame.KEYDOWN:

            # Приостановка движения планет при нажатии пробела
            if event.key == pygame.K_SPACE:
                if move:
                    move = False
                elif not move:
                    move = True

            # Ускорение в два раза
            if event.key == pygame.K_2:
                speed = 2

            # Обнуление скорости
            if event.key == pygame.K_0:
                speed = 1

            # Замедление в два раза
            if event.key == pygame.K_5:
                speed = 0.5

            # Замедление в 10 раз
            if event.key == pygame.K_1:
                speed = 0.1

    # Заливка экрана
    screen.fill(colors.black)

    # Прорисовка орбит
    for dist in distances:
        pygame.draw.circle(surface=screen, color=colors.grey, center=center, radius=dist, width=1)

    # Прорисовка Солнца
    sun.draw(screen=screen, screen_width=width, screen_height=height)

    # Прорисовка планет
    for planet in planets:
        planet.move(screen=screen, screen_width=width, screen_height=height)

    # Обновление экрана
    pygame.display.flip()

    # Смещение планет на следующий цикл, если воспроизведение не приостановлено
    if move:
        for planet in planets:
            planet.angle += planet.speed * speed

