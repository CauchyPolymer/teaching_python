my_str = 'watermaelon'
#py는 expression을 statement로 만들어 줘야한다.
#파이선에는 script mode & interactive 모드라는게 있다. terminal에 python3만 쓰면 됨. >>> interactive모드 시작 eixt()
#interative mode는 expression만 있어도 사용이 가능하다! 값이 NONE일 경우에는 아무것도 안 일어남
for s in my_str:
    print(s)
print()

my_dict = {'name':'Alice', 'age':12, 'gender':'F'}

for k in my_dict:
    print('Key is {} value is {}.'.format(k,
     my_dict[k])) #py에서 ()되어 있는건 두줄로 나눠서 써도 됨.
print()

for i in range(10):
    print('Melon')#range

for n in range(5):
    print(n)

for x in [0, 1, 2, 3, 4]:
    print(x)

r = range(10)
print(type(r))

for n in range(1,6):
    print(n)

print('-' * 40)

for n in range(1, 101, 2):
    print(n)

print('-' * 40)

for n in range (100, 0 ,-2):
    print(n)

print('-' * 40)

my_fruit = 'watermaelon'

my_list = []
for c in my_fruit:
    my_list.append(c)
print(my_list)

for i in range(len(my_list)):
    print(my_list[len(my_list)-1 -i])

print('-' * 40)

length = len(my_fruit)
for i in range(length -1, -1, -1):
    print(my_fruit[i])
