class Line2D():
    def __init__(self, x0:int, y0:int, x1:int, y1:int) -> None:
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
    
    def __repr__(self) -> str:
        return f"Line: from ({self.x0}, {self.y0}) to ({self.x1}, {self.y1})"

class Line3D():
    def __init__(self, x0:int, y0:int, z0:int, x1:int, y1:int, z1:int) -> None:
        self.x0 = x0
        self.y0 = y0
        self.z0 = z0
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1
    
    def __repr__(self) -> str:
        return f"Line: from ({self.x0}, {self.y0}, {self.z0}) to ({self.x1}, {self.y1}, {self.z1})"