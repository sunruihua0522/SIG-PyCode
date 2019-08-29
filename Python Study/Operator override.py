class Point:
    def __init__(self, a, b):
        self.A = a
        self.B = b
    def __add__(self, other):
        return Point(self.A + other.A, self.B + other.B)
    def __mul__(self, other):
        return Point(self.A * other.A, self.B * other.B)
    def __sub__(self, other):
        return Point(self.A - other.A, self.B - other.B)

    def __str__(self):
        return '当前点坐标(%d,%d)'%(self.A,self.B)

if __name__ == '__main__':
    PointA = Point(25,36)
    PointB = Point(12,47)
    PointC = Point(98, 647)
    print(PointA + PointB + PointC)
    print(PointA - PointB + PointC)
    print(PointA - PointB*PointC)