s = 'apple'
l = len(s)#len() - 길이나 사이즈 값을 보여줌. int 값임
print('Length of the String{} is {}'.format(s, l))
#가변하는 부분을 {} 로 묶음. string formatting = 알아서 str로 변환시켜서 들어감. str로 바꿔 줄 필요 없음.
#format = method

c = s[3] #4번째 글자. 이 방식을 subscripting 이라고 함.
print('Character at index {} is {}'.format(3, c))

c2 = s[-1] #뒤에서부터 시작하는 것. 파이썬에서만 할 수 있음. 결과값은 str
print('Character at index {} is {}'.format(-1, c2))

#c3 = s[100] index error!
#print('Character at index {} is {}'.format(100, c3))

c4 = s[len(s)-1] #이럴 필요없음. 일반적으로 10열을 다른 언어에서 사용하는 방식
print('Character at index {} is {}'.format(len(s)-1,c4))

#String of Characters의 줄임말. 개별 글자 여러개의 모임.
#Ordered Collection(=Sequence) = 아이템에 순서가 있는 콜렉션. ex) String
#Collection의 순서 - index

#s[3] = 'L'
#index를 넣어주면 그 숫자에 해당하는 글자를 가져옴. index는 0부터 시작
#str은 immutable하다. 한번 만들어지면 바꿀 수 없다 (in place change할 수 없다.)
#str이 변하는 것 처럼 보이는건 새로 만들어지는 상황이다.

#s2 = s # s = 'apple'
#s = s[0]
#print('s2 = ' + s2)
#print('s = ' + s)

s2 = s
s3 = s.replace('pp', 'b') #s를 바꾼게 아니라, 새로 생성 후, s3에 연결시켜준 것. 실질적으로 두개의 str이 생긴 것
print(s2) # 이런 속성은 어떤 언어에서나 똑같음.
print(s)
print(s3)
