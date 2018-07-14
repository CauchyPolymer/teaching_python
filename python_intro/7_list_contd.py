fruits = ['apple', 'banana', 'cranberry']
print(fruits[1])
#print(fruits[3])
fruits[2] = 'blueberry'
print(fruits)

empty_list = []
#empty_list[0] = 'first item' 설정되어 있지 않은 값에는 replace가 불가능 하다. 자바스크립트에서는 됨. jc는 말이 안되는게 되서 문제임
#second_list = empty_list.append('first item') #WRONG 리스트의 메소드는 굳이 이렇게 변수지정 해 줄 필요 없음. 자바에서는 가능.
#print('second list is {}'.format(second_list))
empty_list.append('first item') #append 메소드를 사용해야 넣을 수 있음. 맨 끝 부터 순서대로 들어감! 가변형일때 걍 이렇게 쓰면됨 ㅎ
#empty_list = empty_list.append('second item') #가장 하지 말아야 할 실수.. 왜 다시 똑같은 변수에 assign함?? 만들었던 리스트 없어짐.
print(empty_list)

#STRING은 불변타입이기 때문에 아래와 같이 변수 지정해줘야 함. 스트링과 리스트에 따라서 코딩 스타일이 달라짐.
#first_string = 'apple'
#second_string = first_string.replace('pp', 'b')
#print(first_string)
#print(second_string)

l3 = [1,2]
l3.append(3)
print(l3)

l3.append(['a','b','c']) #list안에 list가 들어갈 수 있다.
print(l3)
print(len(l3))

l3.extend([4,5,6])
print(l3)

del l3[3] #list에 해당하는 아이템 지우기.
print(l3)


print('-' * 40)

_2d_list = [[11,15,19],[24,29,51,99]]
print(_2d_list)
print(len(_2d_list))
print(_2d_list[0])
print(type(_2d_list[0]))
print(_2d_list[0][1]) #첫번째 아이템[의 두번쨰 아이템]
print('-' * 40)

l = ['apple','banana','cranberry','donut','eclair']
#print(l[1:3])
#slicing

l2 = l#리스트 두개생김 위에서 같다고 해도. 리스트는 mutable이라 in-place change가 된다.
l = l[1:3]#하지만 이렇게 slicing 하게 되는 경우에는 두개가 생김. 바꾸는게 목적이 아닌 읽기라.. 이렇게 복사가 되는거.
print('l is {}'.format(l))
print('l2 is {}'.format(l2))

#string slicing

s = 'computer'
print(s[0:7])
print('-'*40)

l = ['apple','banana','cranberry','donut','eclair']

print(l[2:4]) #기본적인 형태
print(l[-3:-1])#뒤에서 부턴 1임

print(l[0:2]) #2는 포함 안함
print(l[:2]) #생략 되어 있으면 0으로 간주됨됨

print(l[3:5])
print(l[3:]) #끝이 생략되면 끝까지

print(l[0:5])
print(l[:]) #이건 0부터 끝까지지. 슬라이스는 리스트를 복사하는 거기때문에

l3 = l[:] #이런게 가능해짐. L을 복사하게 된다!
l3[1] = 'Pomegranade'

print('l3 is {}'.format(l3)) #여기선 바뀌겠지만
print('l is {}'.format(l)) #여기선 안바뀌겠지? 복사한거니까
print('-'*40)

# l3[5] = 'fronzen yogurt' #error append써줘야함 ㅋ

l4 = l3 #복제해주는거지
l5 = l3.append('froyo') #WRONG append의 결과가 none이라.. ㅠㅋ 그냥 l3.append로 써야함. 기억하기. 변수 서로지정 안하기.
#l3 = ;3.append('froyo') #WRONG
print('l3 is {}'.format(l3))
print('l4 is {}'.format(l4))
print('l5 is {}'.format(l5))

l3.append([1,2,3])
l3.append([4,5,6])
del l3[0]
print('l3 is {}'.format(l3))

l4 = l3 + ['mango', 'peach'] #리스트끼리도 붙일 수 있다.
print('l3 is {}'.format(l3))
print('l4 is {}'.format(l4))
l4 = l4 * 2 #리스트 곱하면 그 수 만큼 두번 나옴.
print('l4 is {}'.format(l4))

##EXERCISE
