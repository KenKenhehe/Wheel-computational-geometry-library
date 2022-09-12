from point import Point2D
from typing import List
class Polygon2D():
    def __init__(self, vertices:List[Point2D]) -> None:
        self.vertices = vertices
        
    def add_vert(self, vert: Point2D) -> None:
        self.vertices.append(vert)

    def __repr__(self) -> str:
        str = "polygon: \n"
        for v in self.vertices:
            str += f"{v.__str__()}\n"
        return str