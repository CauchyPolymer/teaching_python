#comprehension중 가장 대표적인 list comprehension
#list = 순서가 있고 중복 가능 [1,3,3,1] mutable
#dict = 순서가 없고 key(unique)와 value. {'k1':1,'k2':2} mut
#set = 순서가 없는 집합 {1,2,3} mut 공집합을 만드려면 s=set() 해줘야함. 그냥 s=[]는 리스트

my_list = [] #java같은 일반적인 언어에서 사용하는 방식.
for x in range(1,11): #list comprehension 1부터 10까지의 제곱값들을 채워넣는 가정.
    my_list.append(x ** 2) #기본적으로는 이런식으로 for loop을 쓰면 가능함. x^2한후 list에 append
print(my_list) #이런 패턴이 너무 많아서 이것의 전용 문법이 생겨버림
#아래 문법과 같음

my_list = [x ** 2 for x in range(1,11)] #list comprehention 문법 [ __ for _ in ___]
print(my_list) # 위에 for 뒤의 x를 그 앞에 사용 할 수 있고, 맨 앞의 x값이 결과가 됨

my_list =   [x ** 3
            for x in range(1,11)
            if x % 2 == 0] #이 다음에 if조건이 또 들어갈 수 있음.
print(my_list)

# my_list = []
# for x in range(1,11):
#     if x % 2 == 0:
#         my_list.append(x ** 3)
#
# print(my_list)

_2nd_list = [x % 3 for x in my_list] #3으로 나눈 나머지가 결과
print(_2nd_list)

falses = [False for x in range(5)] #false 5개만듬
print(falses)
print('-' * 40)

import random #하나의 statement이기 때문에 어디든 갈 수 있음.
randoms = [round(random.random(),3)
            for _ in range(5)] #list 5 안에 있는 유한소수들.
print(randoms)

#2 dementional (nested) list comprehention
my_list = []
for x in range(3): #for loop 안에 for loop이 들어가 있으면 nested for loop
    for y in range(4): # 3*4 = 12번 처리 됨.
        my_list.append((x,y)) #x,y를 묶어서 tuple로 append가 12번 일어난게 보임.
print(my_list)

my_list = [(x,y)
            for x in range(3) #위 nested와 똑같은 문법
            for y in range(4)]

my_list = [(x,y)
            for x in range(5) #nested 와 if까지 다 섞을 수 있음. 25개의 순서쌍.
            for y in range(5)
            if x != 0 and y !=0 and #둘다 0이 아닌 짝수 (둘다 홀수 혹은 짝수인 경우만 삼)
            ((x+y)%2 == 0)]
print(my_list)
print('-' * 40)
##
my_str = 'applejuice'
my_list = [c.upper()
            for c in my_str
            if c in ('a','e','i','e','u')] #if 조건에는 lowercase가 안걸리기 때문에 AEUIE만 나옴.
my_str = ''.join(my_list) #list 'a','b'이런식의 글자들을 ab로 붙여주는 패턴. (list -> str)
print(my_str)
print('-' * 40)
##
my_list = [x % 5 for x in range(10)] #5로 나눈 수 0,1,2,3,4,0,..., 가나오지만
print(my_list)

my_set = [x % 5 for x in range(10)] #set comprehention
print(my_set) #set은 unique해서 값이 겹칠 수 가 없음 그래서 0,1,2,3,4만 나옴 (알아서 중복 없애줌)

my_dict = {str(n): n**2 #dit는 키와 밸류를 둘다 적어줘야 함.
            for n in range(10)} #키 0~9, value는 0,1,4,9,..,81까지 제곱수
print(my_dict)

my_tuple = tuple(x % 5 for x in range(10))#tuple comp는 괄호로 만드는게 아니라 tuple()이라 적어줘야함
print(my_tuple)

g = (x % 5 for x in range(10)) #괄호치면 이런상황 : generator expression 이 나옴! 나중에하는거
print(g) #이게 더 많이 쓰이기 때문에 간편한 문법을 여기에 배정한 것이지어

print('-' * 40)

el = []
for xx in range(10): #variable의 scope가 다름.
    el.append(xx) #for loop이 끝나면 마지막 같이 남아있음.
print(xx)

el = [yy for yy in range(10)]
#el이라는 리스트 안에 yy가 들어있음.

print('-')

my_list[]
for c in 'applejuice':
    if x in ('a','e','i','o','u'):
        my_list.append(c.upper())
    else:
        my_list.append(c)
    print('',join(my_list))

#x = 100
#a = 'big' if x>50(조건) else 'small' : ternary if법
my_list = [c.upper() if c in ('a','e','i','o','u') #값이 들어가기 때문에 statement가 들어갈 수 없음
                        else c for c in 'applejuice']

print(''.join(my_list))
