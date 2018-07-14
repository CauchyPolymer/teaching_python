def func_1(a, b, c=0): # c 가 기본 값. defualt arguemnt
    print(a, b, c, sep=' -*- ')

func_1(1, 2, 3)
func_1(1, 2) #function overloading

def func_2(a, b, c=0, d=1, e=2):
    print(a, b, c, d, e, sep= ' -*- ')

func_2(1,2,3,4,5)
func_2(1,2,3,4)
func_2(1,2,3)
func_2(1,2, e=5) #키워드 arg는 한군데에 몰려있어야 작동 가능.
#func_2(a=1, 2)
func_2(a=1, b=2)

#def func_3(a, b, c=0, d=1, e): 아예 안됨 ㅎ
#   print(a, b, c, d, e, sep=' -*- ')
#func_3(1,2,3,4,5)
#func_3(1,2,5)
