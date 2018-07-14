class Sedan(): #class안에 함수가 들어가면 - method라고 부른다!**
#얘네가 클래스에 들아갈 때 부터 context가 생기기 때문에 문맥이 생긴다.
#메소드는 항상 아래와 같은 형태로 쓰인다.
    no_of_doors = 4 #attr은 오브젝트 안의 오브젝트라고 한다. class attr!
    #보통 액션은 class attr이다 왜냐하면 행동의 아웃풋을 달라지지 않기 때문이다.

    def set_owner(self, owner): #self 파라미터는 항상 처음에 콜을 해줘야한다. (instance attr)
        self.owner = owner #이런 액션에 해당하는 것들도 attr이다.

    def set_plate_no(self, plate_no):
        self.plate_no = plate_no

    def set_mileage(self, mileage):
        self.mileage = mileage

#매소드와 펑션의 다른점
#펑션 args(파라미터) 0개라도 괜찮
#메소드는 항상 1개를 포함을 시킨다. 컨벤션에 따라서 self라고 이름을 붙여줌.


alice_sedan = Sedan() #세단이라는 클래스에 엘리스세단을 어사인 해줌. 셀프에 alice_sedan을 넣었고
#print(alice_sedan.owner) #에러뜸 attr fetch rule때문에
Sedan.set_owner(alice_sedan,'Alice') #owner에 엘리스를 넣음.
alice_sedan.set_owner('Alice')
#instanceobj.attr(method) 을 가지고 온다. 셋오너를 찾는다, 클래스에서는 셋오너가 있으니까 아까와 같이 셋오너가 실행됨
#그런데 원래 셋 오너에 args를 두개 넣어줘야 한다. 하지만 앞에 instanceobj가 있으면 첫번째 args에 넗어준다. 그래서 26,29번 같은거임
Sedan.set_plate_no(alice_sedan, 'ABCDE')
alice_sedan.set_mileage(10000) #=alice_sedan.set_mileage(1000)


print(alice_sedan.owner)
print(alice_sedan.plate_no)
print(alice_sedan.mileage)

#객체를 중심으로 관리를 잘 하는게 목적인데 위를 보면 class attr부터 보이고 method도 직관적인 모형이다.
#코드도 간단하고 메소드 수가적으니까 직관적이게 보이는데, 나중가면 instanceobj만들어주는 코드가 퍼져있으면 관리가 어렵다.
#그래서 이 형식도 이상적인 형식은 아님.
