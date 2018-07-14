#Data Type 리뷰.
#여태까진 '하나'의 데이터 타입을 공부함 (숫자(int, float), 문자(string - 하나이자 여러개))
#지금부터는 여러개의 데이터 타입. (순서 기준Sequence = LIST, 키 기준)

#JAVA에서의 array와 비슷. 여러가지 정보를 넣을 수 있지만 같은 종류의 정보여야 함. int array는 int만 들어가는 식으로
#array도 데이터 타입이 있지만, list에는 item type 제한이 없다. (list도 컬렉션이기 떄문에 길이 가 말이 됨)

#array는 미리 크기를 설정하고 크기가 변할 수 없는데, list는 크기 변경이 가능하다.
l = []
l2 = list()# 둘다 empty list

print(type(l))
print(type(l2))

l3 = ['apple', 'banana', 'cranberry']
l4 = [2, 3, 5, 7]
l5 = ['apple', 2, 'banana', 3.0, '3.0']

print(l3)
print(l4)
print(l5)

print('Length of the 3rd list is {}'.format(len(l3))) # 리스트 아이템의 가지 수 가 나옴.
###################################
# py에서 list 는 가변(mutable) 이다. list 와 str의 결정적인 차이점. in place change 가 가능하다!
l3[2] = 'blueberry' #cranberry를 바꾸겠다!

print('The 3rd itme in the 3rd list is {}.'.format( l3[2]))
print(l3)

l3[2] = 4.5 #str을 전혀 다른 타입으로 바꾸는 것 도 가능.
print(l3)

l5[3] = 33.33
print(l5)
l5[3] = '33.33'
