def func_1(a, b, c): #function def (parameter variable)
    print(a,b,c, sep=' -*- ') #func body

func_1(1,2,3) #positional argument
#func_1(1,2)
func_1(a=1,b=2,c=3)#function call(argument value)
func_1(c=1,b=2,a=3)#keyword argument -> 최대한 활용하기.

print('-' * 40)

def func_2(name, age):
    print('Name: {}'.format(name))
    print('Age: {}'.format(age))#로컬이라 밑의 프린트와는 관계없음.

name = 'Max'
age = 4
func_2(name, age)
func_2(age, name) #func(4,'Max')
print('-' * 40)

def func_3(name, age):
    print('Name: {}'.format(name))
    print('Age: {}'.format(age))

func_3(name='Benji', age=3)
func_3(age=3, name='Benji')
#func_3(n='Benji', a=3)
print('-' * 40)

#mixing positional and keyword arguments

def func_4(a, b, c, d, e):
    print(a, b, c, d, e, sep=' -*- ')

func_4(1,2,3, d=4, e=5)
#func_4(1, e=5, d=4 ,2, 3) 이런건 금ㅈ
func_4(1,2,3, e=5, d=4)
