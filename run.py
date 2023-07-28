class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.lowleft.x < self.x < rectangle.upright.x and rectangle.lowleft.y < self.y < rectangle.upright.y:
            return True
        else:
            return False

    def distance_from_point(self, point):
        return ((self.x - point.x)**2 + (self.y - point.y)**2) ** 0.5


point1 = Point(10, 20)
point2 = Point(3, 4)

point2.falls_in_rectangle((5, 6), (7, 9))

Point(3, 4).falls_in_rectangle((1, 1), (6, 6))

point1.distance_from_point(3, 3)


class Rectangle:
    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright


pointx = Point(6, 7)
rectanglex = Rectangle(Point(5, 6), Point(7, 9))

pointx.falls_in_rectangle(rectanglex)
