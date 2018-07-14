class Sedan():
    no_of_doors = 4
    def __init__(self, owner='Unknown', plate_no = '', mileage=0):
    #__init__이라는 이름의 메소드가 정해지면 저 클래스를 통해서 **인스턴스가 만들어질때 실행이 됨.**
        self.owner = owner #obj.이니까 attr라서 attr룰을 따르고 = owner은 그냥 변수 이름이다. 아예 다른 애들임
        self.plate_no = plate_no
        self.mileage = mileage #별도의 특수한 메소드 관리 - 이것은 constructor or initialize라고 한다
        #이 self는 지금 만들어지고 있는 과정에 있는 instance를 지칭한다.
        # 사용자가 값을 안줬으면 저렇게 기본값을 준다.

    def set_owner(self, owner):
        self.owner = owner

    def set_plate_no(self, plate_no):
        self.plate_no = plate_no

    def set_mileage(self, mileage):
        self.mileage = mileage

new_sedan = Sedan()
print(new_sedan.owner)
print(new_sedan.plate_no)
print(new_sedan.mileage)

old_sedan = Sedan(mileage=20000) #func쓸때 arg룰이랑 const쓸때 룰이랑 똑같다. 뭔가 바꿔주고 싶을땐 이렇게
alice_sedan = Sedan('Alice', 'ABCED', 10000) #혹은 이렇게 다 쎄팅 가능. 이럴땐 이렇게 positional args 만 가지고 해도 된다.
