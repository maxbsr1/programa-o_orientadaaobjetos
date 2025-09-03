from sympy import Point2D


class Ponto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    p2d1 = Point2D(5, 25)
    p2d2 = Point2D(-5, -25)

    print(p2d1.y)
    print(p2d1.x)
    print(p2d2.y)