import pygame
from graphic_layer_pygame import *
import random
from line import Line2D
from point import Point2D
from polygon import Polygon2D
from typing import List
from convex_hull import compute_convex_hull_2d_gw
import time

WIDTH = 900
HEIGHT = 500

MAX_FPS = 120

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255,255,255)
DARK = (25, 20, 25)

line_to_draw = Line2D(0, 0, 200, 300)
point_to_draw = Point2D(300, 200)

polygon_vert = [Point2D(100, 100),  Point2D(150, 100), Point2D(150, 150), Point2D(100, 150)]

polygon_to_draw = Polygon2D(polygon_vert)

RAND_GEN_BUFFER = 50

def generate_random_points() -> List[Point2D]:
    points_to_generate = []
    for i in range(10000):
        points_to_generate.append(
            Point2D(random.randint(RAND_GEN_BUFFER, WIDTH - RAND_GEN_BUFFER), 
            random.randint(RAND_GEN_BUFFER, HEIGHT - RAND_GEN_BUFFER))
            )
    
    return points_to_generate
start = time.time()
points_to_generate = generate_random_points()
convex_hull = compute_convex_hull_2d_gw(points_to_generate)
print(f"processing time for convex hull: {time.time() - start}")

def update():
    WIN.fill(DARK)
    #graphic_layer_pygame.draw_point(WIN, point_to_draw=point_to_draw, size=5)
    #graphic_layer_pygame.draw_line(WIN, line_to_draw, width=2)
    #draw_polygon(WIN, polygon_to_draw=polygon_to_draw)
    for p in points_to_generate:
        draw_point(WIN, point_to_draw=p, size=2)
    draw_polygon(WIN, polygon_to_draw=convex_hull)
    pygame.display.update()

def main():
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(MAX_FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        update()

    pygame.quit()

if __name__ == "__main__":
    main()