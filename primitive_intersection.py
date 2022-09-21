from audioop import lin2adpcm
from typing import List
from line import Line2D
from point import Point2D

def is_line_intersect_2d(line1: Line2D, line2: Line2D) -> bool:
    x1 = line1.x0
    y1 = line1.y0
    x2 = line1.x1
    y2 = line1.y1

    x3 = line2.x0
    y3 = line2.y0
    x4 = line2.x1
    y4 = line2.y1

    den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

    if(den == 0): return False

    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
    u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den

    if(t > 0 and t < 1 and u > 0 and u < 1):
        return True
    
    return False

def get_line_intersection_2d(line1: Line2D, line2: Line2D) -> Point2D:
    intersection = None
    x1 = line1.x0
    y1 = line1.y0
    x2 = line1.x1
    y2 = line1.y1

    x3 = line2.x0
    y3 = line2.y0
    x4 = line2.x1
    y4 = line2.y1

    den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    
    if(den == 0): return False

    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
    u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den

    if(t > 0 and t < 1 and u > 0 and u < 1):
        intersec_x = x1 + t * (x2 - x1)
        intersec_y = y1 + t * (y2 - y1)
        intersection = Point2D(intersec_x, intersec_y)

    return intersection

def get_all_line_intersections_2d(lines: List[Line2D]) -> List[Point2D]:
    
    return []


