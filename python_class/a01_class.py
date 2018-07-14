class Square():
    NO_OF_EDGES = 4
    def __init__(self, edge):
        self.edge = edge

    def area(self):
        return self.edge * self.edge

sq1 = Square(3)
sq2 = Square(7)
sq3 = Square(11)

print(sq1.area())
print(sq2.NO_OF_EDGES)

class Circle():
    PI = 3.14
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return (self.radius**2) * Circle.PI

    def circumference(self):
        return (self.radius*2) * Circle.PI

circle1 = Circle(3)
circle2 = Circle(9)

print(circle1.PI) # .class attr가져오는 걸 attr fetch 라고 함////
#print(circle.radius) 실행 안됨. Circle 위로 올라가서 찾기 때문에. circle1 = Circle(3)로 내려가지 않음 circle1.radius는 가능
print("원의 넓이 = " + str(circle1.area()))
print("원의 길이 = " + str(circle1.circumference()))
