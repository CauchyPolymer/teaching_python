class Sedan():
    #print('hi')
    no_of_doors = 4 #class attributes

print(Sedan)
print(type(Sedan))

print('도어 수 :',Sedan.no_of_doors)

#파이썬의 모든 데이터는 다 오브젝트 이다. myclass.xyz 형식으로 점(attribute access)이 찍혀 있을떄 오브젝트에 속성을 찾아줌
# Sedan.no_of_doors = 5 #attribute 변환 가능. 하지만 권장되지는 않는다.
# print('도어 수 :',Sedan.no_of_doors)

#instantiations

alice_sedan = Sedan() #인스턴스가 생긴다.
bob_sedan = Sedan() #

print(alice_sedan)
print(bob_sedan)

print(alice_sedan.no_of_doors)

alice_sedan.owner = 'Alice' #권장되는 방식은 아님. 
alice_sedan.plate_no = 'ABCDE'
alice_sedan.mileage = 10000

#클래스는 실제 오브젝트가 생긴다 인스턴스를 여러개 만들 수 있다.
#클래스를 통해서 인스턴스를 만들게 되면 항상 연결이 생긴다. ***** 중요
#인스턴스에 attr이 없으면 클래스 오브젝트 안에서 찾는다. attr을 access 라고 하는데 거기에 read(fetch) write가 있다.

print('Alice의 번호', alice_sedan.plate_no)
print('Bob의 번호', bob_sedan.plate_no)
print('클래스 번호', Sedan.plate_no)
