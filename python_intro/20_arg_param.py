import random

def print_random_numbers():
    r = random.randrange(1,101)
    print(r)

for _ in range(10): #10번 돌리는거 이렇게 사용하지 않는 변수들은 for _ 라고 쓸 수도 있음.
    print_random_numbers

print('-' * 40)

def cube(n): #함수 def안에 들어가는 n 을 parameter variable라고 함.
    #print(n*n*n)
    return(n*n*n) # return 다음 코드는 실행 될 수 없는 unreachable code
    #print('hi')

def power(a, b):
    return a**b

c = cube(2) # 이값이 input인데 각각 연결이 되어서 함수 내부에서 쓸 수 가 있음. 여거서 2를 argument = value 라고 함.
print('cube of 2 is {}'.format(c))
# n = 2
# c = (n*n*n)

n = 3
c = cube(n)
print('Cube of {} is {}'.format(n, c))

n = 4
c = cube(n)
print('Cube of {} is {}'.format(n, c))
print('-' * 40)

def return_nothing():
    pass
    return #리턴 다음에 아무것도 없으면 사실상 생략 하는것과 같음. 기본값으로 none을 리턴하도록 세팅이 됨.

r = return_nothing #그래서 r이라는 변수와 연결 시켜주면 r도 none이 되는 것
print(r)

r = print('Hello')
print(r)

l = [1,2,3]
l.append(4)
print(l)

s = 'apple'
s2 = s.replace('pp', 'b')
print(s)
print(s2)
print('-' * 40)

def my_power(n, x):
    return n ** x

for i in range(5):
    print(my_power(2,i))

print('-' * 40)

# local scope
a = 1 #global scope를 가진 global variable

def func_1(): #왼쪽이 붙어있는 코드를 top level code라고 함.
    a = 2 #탑레벨에 이렇게 정의가 된 변수는 이 레벨의 scope다. = local variable, local scope
    return a #얘네는 func의 끝까지 작동함. 위의 a = 1 과는 다른 값.

result = func_1()
print('result of func_1: {}'.format(result))

a = 1 #이런식으로 변수를 세팅하고 나면 쓸수 있음. 이렇게 변수와 값을 연결시키는 걸 binding이라 함.
b = 2

print(a,b) # 이렇게 변수 바인딩을 참조(reference) 할 수 있다. 변수 지정 아래는 그 변수의 scope
print('-' * 40)
#z = 3

def func_2():
    z = 3
    return z

#print(z) global variable z임 func_2 아래 z랑은 참조가 안됨.

def func_3(): #global 에서 func안쪽은 못쓰지만 그 반대는 가능!
    return [a,b]

result = func_3()
print('func_3 result: {}.'.format(result))

def func_4():
    return [xx, yy] #func4 입장에서는 xx와 yy가 뭔지 찾지를 못함.

#result = func_4()
#print(' func_4 result: {}'.format(result))

#LEGB Rule(Local, Enclosing Function, Global, Built-in) ***읽을때만!
#local scope에서 변수를 찾으면 그 값을 사용 > EF> Global> Built-in

xx = 10
yy = 20

def func_5(): #5번 함수 콜 Local
    xx = 1000
    yy = 2000
    return [xx, yy] #xx yy를 어디서 찾는가 -> LEGB룰에 따라서 찾음. Local 함수 있어서 바로 끝

result = func_5() #binding이 되고나면 이름만 쓰면 그 값을 읽어 옴.
print('func_5 result: {}'.format(result))

print(xx,yy)
print('-' * 40)

def func_6(xyz): #func헤더 - parameter에 xyz라고 있다고해서 GS에서 볼수 있는게 아님.
    return xyz + 100

#print(xyz)

a=1

def func_7(n):
    n+=100
    return n

b = func_7(a)

print(a, b, sep = ' -*- ')
print('-' * 40)

a = 1
b = 2

def swap(a,b):
    temp

def func_8():
    print('Func 8')
    v = func_9()
    return v + 9

def func_9():
    print('Func 9')
    return 9

r = func_8()
print(r)
print('-' * 40)

xx = 10

def func_10():
    print('Func 10')
    xx = 1000

func_10()
print('xx',xx) #global을 그냥 읽는다. 쓰기는 scope을 넘어가지 않음.

def func_11():
    print('func 10')
    return 1000 #주어진 값을 변화시키고 싶으면 return을 사용하라. 권장사항!

xx = func_11()
print('xx after 11 :', xx)

def func_12():
    print('Func 12')
    global xx #func안에 global이라는 명령을 쓰고 변수를 쓰면 이 함수 안에서는 xx가 글로벌 이라고 fix시키는 함수.
    #부자연스러운 문법이지만 종종 사용됨. 하지만 권장되지 않는 코드.
    xx = 100000

func_12()
print('xx after 12:', xx)
