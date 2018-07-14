fruits = ['apple', 'banana', 'cherry', 'durian', 'eggfruit', 'fig']

for i in fruits: #반목문 for loop! JAVA는 C랑 똑같이 되어있음. py는 enhanced for loop!
#for (새로운 변수) in (iterable collection expression) :
#여기서 i 는 str
    print('fruit: {}'.format(i))
print('-' * 40)

#i = fruits[0] 이것들이랑 똑같은 말임.
#print('Fruit: {}'.format(i))
#i = fruits[1]
#print('Fruit: {}'.format(i))
#i = fruits[2]
#print('Fruit: {}'.format(i))
#i = fruits[3]
#print('Fruit: {}'.format(i))

my_list = ['apple', 'banana', 'cherry']
for fruit in my_list:
    print(fruit)

my_str = 'apple'
for c in my_str:
    print(c)

my_dict={'name':'hong', 'age':25, 'weight':85}
for key in my_dict:
    print(key)
    print(my_dict[key])

print('-' * 40)

for x in range(0,10):
    print(x,end=' -*- ') #줄바꿈을 하지 않고 끝에 뭔가를 end=''로 바꿀 수 있음. 프린트가 10번실행 됐지만 한줄에 다 나옴.
print()

for x in range (0,10,2):
    print(x, end=' -*- ')

l = [0,1,2,3,4,5,6,7,8,9]
print()
print(type(l))
r = range(0,10)
print(r)
print(list(r)) #range를 list로 만들어 줘야 함
print(type(r))
print('-'*40)

for x in range(0, 10, 2): #range에 세번째 숫자는 몇번째 것을 가져올 것인가.
    print(x,end=' -*- ') # 위와 같은 경우 두개씩 건너 뜀
print()

for x in range(9, -1, -1): #뒤로 세는것.
    print(x,end=' -*- ')
print()

for x in range(10):
    print(x,end=' ')
print()

print('-' * 40)

numbers = [2,3,5,7]
summed = 0

for x in numbers:
    summed = summed + x
    print('x is {} and subtotal is {}'.format(x, summed))

print('Sum is {}'.format(summed))

print()

product = 1 #곱의 첫 값이 1로 시작해야함.

for x in numbers:
    product = product * x
    print('x is {} and subtotal is {}'.format(x,product))

print('Product is {}'.format(product))
print('{}'.format(x))

print()

for f in fruits:
    if len(f) % 2 == 0 : #짝수 구하기
        print('Even length fruit! {}'.format(f))

numbers = [2, 3, 5, 7, 10, 13,17,20,23,27]

summed = 0
for n in numbers:
    if n %2 == 0:
        summed += n #짝수의 합 구하기
print('Sum of the even numbers is {}'.format(summed))

print('-' * 40)

my_fruits = ['apple', 'banana', 'cherry', 'durian', 'eggfruit', 'fig']

for i, fruit in enumerate(my_fruits): #enumerate 안에 컬렉션을 넣어주면 결과가 두 세트로 나눠져 나옴
    print('{}\t{}'.format(i,fruit)) # 컴마를 이용해서 두개를 받아줌. 앞에는 해당하는 인덱스가 나옴.
# 번호와 실제 아이템 두개를 얻을 수 있다!
print('-' * 40)

for t in enumerate(my_fruits): #똑같은 방법이다. 하나로 받았다고 하면
    print(t)
    print('{}\t{}'.format(t[0], t[1])) # 이런식으로 나눠서 받을 수 있다. 이게 가능한 이유는 TUPLE이 가능해서 임.
    # Tuple 은 list 랑 똑같은데 불변이다!
