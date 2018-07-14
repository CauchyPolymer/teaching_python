class Grandparent():
    def __init__(self):
        self.car = 'Great Car'

class Father(Grandparent):
    def __init__(self):
        super().__init__() #중복을 해겷하기 위한 문법.
        self.house = 'Big house'

class Mother(Grandparent):
    def __init__(self):
        super().__init__()
        self.land = 'Big Land'

class ChildOne(Father, Mother):
    pass #init이 실행 되어야 하는데, super에 init을 해주게 되면 윗 클래스의 왼쪽 파라미터 부터 찾는다. 하지만 father의 super은 mother, 그 위는 Grandparent!
    #쓰기가 복잡 ㅜㅜㅜㅜㅜㅜ 그래서 이런 구조 쓰지말고 MIX IN을 쓰자
class ChildTwo(Mother, Father):
    pass

if __name__ == '__main__':
    one = ChildOne()
    print(one.house, one.car)

    two = ChildTwo()
    print(two.land, two.car)

    print(one.car, one.house, one.land)
    print(two.car, two.house, two.land)
