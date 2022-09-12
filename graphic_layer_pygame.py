import pygame
from pygame import Vector2, Vector3
from line import Line2D
from point import Point2D
from polygon import Polygon2D

def draw_point(win:pygame.Surface, 
                point_to_draw: Point2D, 
                size:float = 1, 
                color:Vector3 = (255,255,255)) -> None:
    pygame.draw.circle(win, color, center=Vector2(point_to_draw.x, point_to_draw.y), radius=size)
    #surface, color, center, radius

def draw_line(win:pygame.Surface, 
                line_to_draw: Line2D,
                width:float = 1, 
                color:Vector3 = (255,255,255)) -> None:
    start = Vector2(line_to_draw.x0, line_to_draw.y0)
    end   = Vector2(line_to_draw.x1, line_to_draw.y1)
    pygame.draw.line(win, color, start_pos=start, end_pos=end, width=width)


def draw_polygon(win:pygame.Surface, 
                polygon_to_draw: Polygon2D,
                width:float = 1, 
                color:Vector3 = (255,255,255)) -> None:
    for i in range(len(polygon_to_draw.vertices)):
        current_vert_pos = Vector2(polygon_to_draw.vertices[i].x, polygon_to_draw.vertices[i].y)
        if(i + 1 > len(polygon_to_draw.vertices) - 1):
            next_vert_pos = Vector2(polygon_to_draw.vertices[0].x, polygon_to_draw.vertices[0].y)
        else:
            next_vert_pos = Vector2(polygon_to_draw.vertices[i + 1].x, polygon_to_draw.vertices[i + 1].y)
       

        pygame.draw.line(win, color, start_pos=current_vert_pos, end_pos=next_vert_pos, width=width)