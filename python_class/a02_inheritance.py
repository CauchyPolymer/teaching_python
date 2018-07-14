class Parent():
    common = 'parent class attribute' #단순 str
#class에 이름을 적고 ()하면 컨스트럭터라는 객체 하나가 만들어진다.
#init이 실행 된다.
    def __init__(self): #function(method)
        self.parent_data = 'parent instance attribute'

    def get_name(self):
        return 'parent class'

class Child(Parent): #scope rule 위에 존재해야함
    def __init__(self):
        Parent.__init__(self)
        self.child_data = 'child instance attribute'

c = Child() #child가 인스턴스로 만들어지는 것 -> init 이 실행
print(Child.common)
print(c.parent_data)
#컴퓨터가 c를 알아야 하고, parent_data를 알아야 한다.
#c를 찾아야 할때, .이 없으면 c는 변수이고, 얘h네는 scoping rule의 적용을 받는다
#.을 찍은 이후는 scoping rule 적용을 받지 않는다. c안에 parent_data 있는지만 확인 하는 것
#메타프로그래밍 circle.PI2 = 3.1415..
print(c.child_data)
print(c.get_name()) #인스턴스에는 그냥 실행 가능
print(Child.get_name(c))#클래스에는 인스턴스를 넣어줘야 한다. 위랑 같은 모형이고 정식 문법인데 귀찮아서 간소회 시킴
print(isinstance(c, Child)) #isinstance? child가 c의 인스턴스 인가? 
print(isinstance(c, Parent))
