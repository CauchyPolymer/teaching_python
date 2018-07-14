#n! = n * (n - 1)!
# 문제 자체를 식으로 먼저 풀고 코드로 옮긴다.
n = input('Enter a positive integer:')
n = int(n)

#점화식 == recurrnece relation
# 수열을 코드로 옮기는 연습 하기.
def factorial(n): #어떤 식이 자기 스스로를 통하여 문제를 풀 수 있음.
    if n == 1: #n 이 1이면 ? = 1
        return n
    else: #아니면 ? = n * factorial(n-1) ***** 1번줄을 그대로 코드로 옮긴 것
        return n * factorial(n-1) #

x = factorial(n)
print(x)

#FIBONACCI
#F(n) = F(n-1) + F(n-2)
def fibo(n): #recursion버전은 facto와다르게 overlapping이 심함. loop에 비해서 엄청 오래걸림
    if n==1 or n==2:
        return 1
    return fibo(n-1)+fibo(n-2)

y = fibo(n)
print(y)

#recursion을 사용할때는 overlap이 없는 설계에 사용해야함.
#만약 그 상황에서 사용하려면 중간중간 저장해 줘서 memoization를 더해줘서 dynamic programing을 한다. 동적 계획법.
