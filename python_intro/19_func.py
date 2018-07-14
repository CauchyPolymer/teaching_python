#Java는 컴파일 언어이고, py는 interpreted언어라 작동하는 과정이 다름.
#특정한 목적을 하는 코드를 모아서 관리하기 위하여 f를 만듬. 모은다면 재사용이 될 수 있음.
#보통 연관되어 있는 것들을 모아놓은것을 procedure 이나 subroutine이라고 한다. 내가 옵션을 주고 결과값을 받아오는 것을 f라고 부름.
# 셋이 지금은 비슷한 의미로 쓰임. oop의 f = method. 거의 다 비슷한 개념. p,s는 그냥 실행되어 결과값을 돌려주는 것들.

print('Hello')

def my_function():#py에서 함수는 def로 시작함. compound statement
    #아래에서 할 일을, my_function이라는 이름으로 정의(define)해 준다. -> ACTION
    #실행 -> call, run time
    #ACTION이지 실행이 아님. 그래서 여기서는 실행이 되지 않음! defintion time -> 이 시점에서는 정의만 하겠다.
    pass #아무것도 안하는 것.
    print ('Alo')

print('Bye')

my_function() #괄호 꼭 해줘야함 -> 함수 실행 function call or function invokation
my_function()
print(my_function)
print('-' * 40)

print(type(my_function()))
print(type(my_function)) #default function은 NONE이다.
#변수와 함수의 경계가 모호한 JS와 PY => 요새 개발 대세. ***function도 데이터처럼 처리하기!*** 이게 자바랑 완전 다른 포인트.
#python function == first class'일등석 function = 함수도 차별하지 않고 똑같이 데이터처럼 처리하기 때문!

print('-'*40)
func = my_function
print(type(func))
func
print('-' * 40)

#x = my_random()

def my_random():
    import random #IMPORT
    # r = random.randrange(1, 101)
    # returen r
    return random.randrange(1,101) #여기선 정의 하는거 그래서 이 안에 에러가 있어도 돌아감. 실제로 실행이 안되기 때문에

x = my_random()
print('my random is {}'.format(x))
print('-' * 40)

def func_1() :
    #pass#문법적으로 뭔가 있어야 하는데 아직 뭐가 없다 할때 써주는거. 한줄이 있어야 에러가 안남.
    print('In func 1')
    func_2()

def func_2() :
    print('In func 2')

func_1()

print('-'*40)

import random

def func_3():
    print('In func 3')
    return random.randrange(1, 10) * 100 + func_4()

def func_4():
    print ('In func 4')
    return random.randrange(1,10)

r = func_3()
print(r)
