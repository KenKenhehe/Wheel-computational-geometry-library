from point import Point2D
from polygon import Polygon2D
import numpy as np
from typing import List

def compute_convex_hull_2d(points: List[Point2D]) -> Polygon2D:
    #Convex hull "candidate" vertex, used to construct a convex hull polygon 2d
    convex_hull_candidate = Polygon2D([])
    #Find the most left point
    left_most_point = points[0]
    for v in points:
        if(v.x < left_most_point.x):
            left_most_point = v
    #current vertex that's finding the next closest vertex
    current_point = left_most_point
    
    next_point_selected = points[1]

    convex_hull_candidate.add_vert(current_point)
    should_add = False
    
    index = 2
    while(index < len(points)):
        vectorCurrent = np.array([current_point.x, current_point.y]) - np.array([points[0].x, points[0].y])
        should_add = False
        for j in range(2, len(points)):
            if j + 1 >= len(points):
                break
            vectorChecking = np.array([current_point.x, current_point.y]) - np.array([points[j].x, points[j].y])
            
            if(np.cross(vectorCurrent, vectorChecking) < 0 and points[j] not in convex_hull_candidate.vertices):
                next_point_selected = points[j]
                vectorCurrent = vectorChecking
                should_add = True

        #vectorCurrent = np.array([next_point_selected.x, next_point_selected.y]) - np.array([points[0].x, points[0].y])
        current_point = next_point_selected

        if(should_add):
            convex_hull_candidate.add_vert(current_point)
        index += 1
    print(convex_hull_candidate)
    return convex_hull_candidate

    