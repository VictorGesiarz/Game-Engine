class Vertex:
    def __init__(self, x: float = 1, y: float = 1, z: float = 1) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self) -> str:
        return f'(x: {self.x}, y: {self.y}, z: {self.z})'


class Polygon:
    def __init__(self) -> None:
        self.polygon = list()
        
    def __repr__(self) -> str:
        return f'{self.polygon}'
        
    def add_vertex(self, x, y, z) -> None:
        assert 0 <= len(self.polygon) < 3, 'Too many vertices in one polygon'
        
        if len(self.polygon) == 0:
            self.polygon.append(Vertex(x, y, z))
            return

        if all(i.x != x or i.y != y or i.z != z for i in self.polygon):
            self.polygon.append(Vertex(x, y, z))
            return 
    
    
P = Polygon()
P.add_vertex(5, 5, 5)
P.add_vertex(10, 5, 5)
P.add_vertex(5, 10, 5)

print(P)