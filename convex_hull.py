from point import Point2D
from polygon import Polygon2D
import numpy as np
from typing import List


def compute_convex_hull_2d_gw(points: List[Point2D]) -> Polygon2D:
    """Gift wrapping convex hull algorithm 

    Args:
        points (List[Point2D]): List of points to generate convex hull

    Returns:
        Polygon2D: the convex hull as a polygon object
    """
    #Convex hull "candidate" vertex, used to construct a convex hull polygon 2d
    convex_hull_candidate = Polygon2D([])
    #Find the most left point
    left_most_point = points[0]
    for v in points:
        if(v.x < left_most_point.x):
            left_most_point = v
    #current vertex that's finding the next closest vertex
    current_point = left_most_point
    current_next = points[0]
    if(left_most_point == points[0]):
        current_next = points[1]
    convex_hull_candidate.add_vert(current_point)
    
    index = 0
    while(index < len(points)):        
        for j in range(len(points)):          
            vectorCurrent = np.array([current_next.x, current_next.y]) - np.array([current_point.x, current_point.y])
            vectorChecking = np.array([points[j].x, points[j].y]) - np.array([current_point.x, current_point.y]) 
            if(vectorChecking[0] == vectorCurrent[0] and vectorChecking[1] == vectorCurrent[1]):
                continue
            if(np.cross(vectorCurrent, vectorChecking) < 0):
                current_next = points[j]

        current_point = current_next
        convex_hull_candidate.add_vert(current_point)
        if(current_next == left_most_point and index > 1):
            break
        index += 1
        if(index < len(points)):
            current_next = points[index]
    return convex_hull_candidate

    