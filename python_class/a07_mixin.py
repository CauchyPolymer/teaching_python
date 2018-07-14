class Grandparent():
    def __init__(self):
        self.car = 'Great Car'

class Parent(Grandparent):
    def __init__(self):
        Grandparent.__init__(self)
        self.house = 'Big house'
        self.land = 'Big Land'

class FoodMixIn():
    def food(self):
        print('McDonalds')

class ChildOne(Parent, FoodMixIn): #주가되는 클래스를 왼쪽, 추가적 기능을 오른쪽으로 몰아서 사용
    pass #굳이 super나, childone two에 init 안 만들어도 됨. 이것이 가장 권장되는 모습임

class ChildTwo(Parent, FoodMixIn):
    pass

if __name__ == '__main__':
    one = ChildOne()
    print(one.house, one.car)

    two = ChildTwo()
    print(two.land, two.car)

    print(one.car, one.house, one.land)
    print(two.car, two.house, two.land)
    one.food()
    two.food()
