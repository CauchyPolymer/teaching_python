# 다중 상속(자바에서는 금지 되어있음) - 대신에 Interface라는 방식을 도입함.
# 하나의 class가 두개의 상속을 가질 수 있는 경우. 상속 받는 메소드가 모든걸 설정 하는 비효율적인 경우가 많음
# 그리하여 MIX-IN 방식을 사용한다. (장고같은 경우 많이 사용)

class Grandparent():
    def __init__(self):
        self.speak()

    def speak(self):
        print('Anything')

class Father(Grandparent):
    def __init__(self):
        self.common_data = 1

    def get_paternal_data(self):
        return self._paternal_data

    def set_paternal_data(self,data):
        self._paternal_data = data

    def speak(self):
        Grandparent.speak(self)
        print('McDonals')

class Mother(Grandparent):
    def __init__(self):
        self.common_data = 22

    def get_maternal_data(self):
        return self._maternal_data

    def set_maternal_data(self,data):
        self._maternal_data = data

    def speak(self):
        Grandparent.speak(self)
        print('Burger King')

class Child(Father, Mother): #왼쪽 부터가 우선권을 가짐
    def __init__(self):
        Father.__init__(self)
        temp = self.common_data
        Mother.__init__(self)
        temp += self.common_data
        self.common_data = temp

        self.speak()

    def speak(self):
        Mother.speak(self)
        Father.speak(self)
        print('Wendy\'s')m

if __name__ == '__main__':
    child = Child()
    child.set_paternal_data('qwerty')
    #print(child.get_paternal_data())
    child.set_maternal_data('dvorak')
    #print(child.get_maternal_data())
    #child.speak()
    #print(child.common_data)
