a = 1 # + - * / ** // % 같은 것들을 arithmatic operator라고 부른다.
b = 2 # > >= ==(=와의 다른점 숙지..) 같은 아래 것들은 relational(=comparison) operator.

c = (a>b)
print('c is of type {} and value {}'.format(type(c),c))

c = (a>=b)
print('c is of type {} and value {}'.format(type(c),c))

c = (a<b)
print('c is of type {} and value {}'.format(type(c),c))

c = (a<=b)
print('c is of type {} and value {}'.format(type(c),c))

c = (a==b)
print('c is of type {} and value {}'.format(type(c),c))

c = (a!= b)
print('c is of type {} and value {}'.format(type(c),c))

print('-'*40)

d = 10
e = 100
#and or not - logical operator
#자바에서는 boolean이 확실이 분리가 되어있지만 파이썬은 다름.
#and좌항을 boolean으로 바꾼게 F면 전체가 boolean이 아닌 좌항이 된다. ㄱ
#or은 우항 좌항에 어떤것이 와도 상관이 없다
#not은 값의 종류가 상관이 없다.
c = a>b and d>e
print('c is of type {} and value {}'.format(type(c),c))

c = a>b or d>e
print('c is of type {} and value {}'.format(type(c),c))

c = not a>b
print('c is of type {} and value {}'.format(type(c),c))

c = 'app' and 'ba' #둘다 T기 떄문에 결과적으로 ba가 나옴
print('c is of type {} and value {}'.format(type(c),c))

c = '' or '' #둘다 F라 ㅎ
print('c is of type {} and value {}'.format(type(c),c))

c = not 'apple' #not은 무조건 boolean
print('c is of type {} and value {}'.format(type(c),c))

#이렇게 해놓은 이유는 나중에 재활용 하기 편함. a가 T면 b를 보지도 않아서 b에 오류가 있어도 아예 안봄 = short circuit
