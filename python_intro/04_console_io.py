print('Hello')

a = input('please enter the first number: ') #우항의 값을 먼저 실행시킴 -input:사용자가 터미널에 한줄을 입력하고 엔터를 누를떄까지 기다림.
#input(''<- 값을 넣기전에 출력되는 prompt)
print('you entered: ' + a) # a = input() 항상 str
a = int(a) # str이라서 int형으로 캐스팅

b = input('please enter the second number: ')
print('you entered: ' + b)
b = int(b)

print('Sum = ' + str(a+b))
#str로 캐스팅을 안해주면 'sum =' + a + b인데, 'sum='+a를 먼저 계산하기 때문에, str + int가 되어서 오류가 생김

print('Bye')

# print - 출력을 할 떄 쓰는 function - System.out.print
# inpit - 터미널로 부터 키보드로 받아오는 function - Scanner
# BUILT - IN FUCTION(=static method) (int, float, str) 다른 라이브러리 필요없이 바로 사용가능.
# 특정한 목적을 가진 코드들을 재활용하기 쉽게 만든 그룹.
