class Grandparent():
    def __init__(self):
        self.car = 'Great Car'

class Father(Grandparent):
    def __init__(self):
        Grandparent.__init__(self)
        self.house = 'Big house'

class Mother(Grandparent):
    def __init__(self):
        Grandparent.__init__(self)
        self.land = 'Big Land'

class ChildOne(Father, Mother):
    pass

class ChildTwo(Mother, Father):
    pass

if __name__ == '__main__':
    one = ChildOne()
    print(one.house, one.car)

    two = ChildTwo()
    print(two.land, two.car)

    print(one.car, one.house, one.land)
    print(two.car, two.house, two.land)

##
