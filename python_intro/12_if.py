#분기 와 반복
#분기 : if문을 bool바꾸었을때 참 이면 실행 됨. expression식:계산하면 값이 나옴// statement문: 명령어 한줄
# expression이 statement에 포함 됨. simple statment다 여러개 섞여 있는게 compound statement. if자체는 cs임.
#반복 :

if True:
    x = 1 + 2
    print(x)

if False:
    print('cherry')

a = 1
b = 2
if a < b:
    print('mango')

if 'hello':
    print('hello back')

if []:
    print('My list')

if 5-5:
    print('zero')
print('-' * 40)

my_list = ['coke']
if my_list:
    print('pepsi')

fruit = 'apple'
if fruit == 'apple':
    print('apple please')

a = True
if a and b:
    print('a and b')
else:
    print('not(a and b)')

c = 10
if c > 5:
    print('big')
elif c > 8: #else if -> if가 거짓일때
    print('very big')
else: #elif가 거짓 일때. else 마지막에 한번 올 수 있음.
    print('small')

d = 50

if d > 5: #하나의 if statement
    print('large')

if d > 25: #별개의 if compound statement!
    print('very large')
    print('thank you')
elif d > 25:
    print('extra large')
elif d > 45:
    print('2x large')
else:
    print('small')

    print('not interested')

e = 200

if e > 0:
    print('positive')
    if e > 1000:
        print('4 digit')

else:
    print('negative')
