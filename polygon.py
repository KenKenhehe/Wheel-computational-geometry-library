from point import Point2D
class Polygon2D():
    def __init__(self, vertices:list[Point2D]) -> None:
        self.vertices = vertices
        

    def __repr__(self) -> str:
        str = "polygon: \n"
        for v in self.vertices:
            str += v
        return str