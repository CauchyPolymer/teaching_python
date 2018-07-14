import random #import statement random이름을 가진 기능을 그대로 쓸 수 있다.

x = random.random() #0.0 <= x < 1.0
print(x)
print(type(x))
print(int(10*x))

y = random.randrange(0,10) #0부터 9까지 임의의 정수.
print(y)
print(type(y))

z = random.randrange(10) #이것도 리스트처럼 생략할 경우 0부터 시작.
