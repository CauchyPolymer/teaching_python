#개개인 역시 module을 만들 수 있다.
a = 1
b = 'hello'

def pi():
    c = 234
    return 3.14

my_list = ['apple', 'banana']

print('in lib_module')

print('My name : {}'.format(__name__))

if __name__ == '__main__': #앞뒤로 언더바가 붙은 특별 변수들은 - 다른 곳에서 import로 부를때 값이 달라짐.
    print('in lib_module - main')

if a > 0:
    d = 56
