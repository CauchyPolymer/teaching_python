#sequence assignment
#a , b =1, 2 interacting mode
a, b = (1, 2) # Tuple 입니다. - 괄호가 기본적으로 있지만 생략이 될 수 있는 부분이 있다. Tuple assignment
print(a, b)
c, d = [3, 4] # List assignment
print(c, d)
e, f = 'xy'
print(e, f)

a, b, *c = 1, 2, 3, 4 #특수한 형태. 오른쪽과 왼쪽의 아이템 개수가 맞지 않으면 에러가 난다. 하지만 별을 붙이면 나머지 전부라는 뜻.
print(a, b, c) #나머지 모은건 무조건 리스트. 튜플이 될 수 없다.

a, *b, c = 1, 2, 3, 4
print(a)
print(b) #첫과 끝 값이 정해져 있기 떄문에 나머지가 모두 b가 되는 것.
print(c)

a, *b, c = 'apple'
print(a,b,c)
print(a, ''.join(b),c) # 리스트 ['p', 'p', 'l'] 을  str로 꺠끗히 처리 할 떄.

my_list = [2,4,6,8,10] #처리하고자 하는 데이터
rest = my_list # 맨 앞과 나머지를 잘라버린다. (나눈다)
while rest: #나머지가 있을 경우에만 while loop을 돌린다.
        head, *rest = rest #head와 rest로 쪼갠다.
        print(head, head**2) #아이템이 하나씩 줄은만큼 하나씩 진행하는 것. 그래서 rest가 없어질 때 까지.

print('-' * 40)

def func_1(a,b,*args,c): #positional argument packing
    print('Function 1')
    print(a,b)
    print(args)
    print(c)

func_1(1,2,3,4,5, c=6) #이런식으로 콜 했을때 알아서 찾아서 들어가게 됨. a = 1, b = 2 이런식
print('-' * 40)#그리고 모든 남은 args가 모두 *agrs에 들어감. 그런데 sequence로 묶여서 tuple이 됨.

def func_2(a,b,*args,c=60): #c에 값을 주려면 무조건 파라미터 다음에 키워드로 설정해줘야 함.
    print(a,b)
    print(args)
    print(c)

func_2(1,2,3,4,5,6)

def func_3(a,b, **kwargs):
    print('Function 3') # **는 키워드 args를 모아준다.keyward args packing
    print('a is {}'.format(a))
    print('b is {}'.format(b))
    print('kwargs is {}'.format(kwargs))

#func_3(1,2,3,4,5) # a=1 , b=2 하지만 나머지 3,4,5가 갈 곳이 없음.
func_3(1,2, first=3, second =4, third=5) #fist부터 묶여서 dict로 kwargs에 들어감.
func_3(1, b=3, second=4, third=5)
#func_3(1, b=3, second=4, a=5) #positional적으로 1 = a인데 다시 a=5가 나와서 안됨~
print('-'*40) #dJango같은거 할때는 이런 문법을 많이써서 잘보자~

def func_4(a, b, *args, **kwargs): #파라미터 단어 앞에 *을 붙여서 의미가 있는거지 뒤의 단어는 딱히 의미없음.
    print('Function 4')
    print('a is {}'.format(a))
    print('b is {}'.format(b))
    print('args is {}'.format(args))
    print('kwargs is {}'.format(kwargs))

func_4(1,2,3,4,5, #포지셔널 이후 3,4,5가 args로 가고, 나머지가 kwargs로 감.
    fruit='apple', beverage='apple juice')
print('-' * 40)

def func_5(a,b, *args, c=60, **kwargs):
    print('Function 5')
    print('a is {}'.format(a))
    print('b is {}'.format(b))
    print('c is {}'.format(c))
    print('args is {}'.format(args))
    print('kwargs is {}'.format(kwargs))

func_5(1,2,3,4,5, fruit='a', beverage='aj')
func_5(1,2,3,4,c=5,
    fruit='a', beverage='aj')
print('-' * 40)

def func_6(a ,b=30, *args, c=60, **kwargs):
    print('Function 6')
    print('a is {}'.format(a))
    print('b is {}'.format(b))
    print('c is {}'.format(c))
    print('args is {}'.format(args))
    print('kwargs is {}'.format(kwargs))

func_6(1,2,3,4,c=5, fruit='a', beverage='aj')
func_6(1,3,4,c=5, fruit='a', beverage='aj')
func_6(1, c=5, fruit='a', beverage='aj')
print('-'*40)

def func_7(a ,b=30, *args, c, **kwargs): #어떤 파리미터를 *,**사이에 있는데 디폴트 값이 없으면, 모든 arg에서 kwarg로 콜을 해줘야함.
    print('Function 7')#python is so flexible!
    print('a is {}'.format(a))
    print('b is {}'.format(b))
    print('c is {}'.format(c))
    print('args is {}'.format(args))
    print('kwargs is {}'.format(kwargs))

func_7(1,2,3,4,c=5, fruit='a', beverage='aj')
#func_7(1,2,3,4, fruit='a', beverage='aj') #c가 없어서 실행 불가!
func_7(1,c=5, fruit='a', beverage='aj')
print('-'*40)
