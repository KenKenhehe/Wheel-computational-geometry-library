class Point2D():
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Point2D: ({self.x}, {self.y})"

class Point3D():
    def __init__(self, x: int, y: int, z:int) -> None:
        self.x = x
        self.y = y
        self.z = z
