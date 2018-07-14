def func_1(): #function은 정의를 하고 call을 하여 재활용을 한다. 중요한 개념
#일반적으로는 함수가 있고 글로벌에서 함수를 불러서 쓰는데, 함수 안에서 함수를 call 할 수 있다.
    print('hello')

def func_2():
    func_1()
    print('hello again')#func1이 끝나야 프린트 가능.

func_2
#top-level -> func_2 -> func_1
#function call chain/ function call stack
#call stack 이 넘치게 되면 에러가 남.

print('-' * 40)

import random

def func_3():
    print('in func 3')
    f = random.randrange(1, 10) * 100
    b = func_4()
    return f + b

def func_4():
    print('in func 4')
    return random.randrange(1, 10)

r = func_3()
# print(r)
# print('-' * 40)
#
# def recurse(n): #자기 스스로를 call할수가 있도록 되어있다. 그래서 재귀함수 'RECURSION' 이라고 칭한다!
#     print('hi-{}'.format(n))
#     recurse(n+1) #최대 call stack 의 깊이가 1000이다. 메모리의 최대값.

#recurse(1) #stack over flow ERROR

print('-' * 40)

def recurse_2(n): #STOFE가 안남. 이유는
    print('hi-{}'.format(n))
    if n == 25: #24까지 가고 recurse_2(25)는 n 이 25기 떄문에 끝나버림.
        return
    else: #스스로를 call 해도 상관이 없음.
        recurse_2(n + 1)

recurse_2(1)
print('-' * 40)

def recurse_3(n):
    print('hi-{}'.format(n)) #call stack 이 올라갔다가 내려기는 피라미드 순서로 진행됨.
    if n == 0:
        return
    else:
        recurse_3(n - 1)
        print('returing - {}'.format(n))

recurse_3(10)
