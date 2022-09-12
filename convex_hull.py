from point import Point2D
from polygon import Polygon2D
import numpy as np

def compute_convex_hull_2d(points: list[Point2D]) -> Polygon2D:
    #Convex hull "candidate" vertex, used to construct a convex hull polygon 2d
    convex_hull_candidate = []
    
    pending_point = None
    next_point = None

    #Find the most left point
    left_most_point = points[0]
    for v in points:
        if(v.x < left_most_point.x):
            left_most_point = v

    #current vertex that's finding the next closest vertex
    current_point = left_most_point
    
    for i in range(len(points)):
        
        break
        


    