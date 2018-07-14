def sum(n): #built in func이긴 한데 선언 해주면 overide해주기 떄문에 상관 없지만, built-in을 변수로 쓰는건 지양.
    if n == 1:
        return 1
    else:
        return n + sum(n - 1)

y = sum(10)
print(y)
print('-' * 40)

user_input = input('Enter : ')
def reverse(i):
    if len(i) == 1:
        return i
    else:
        return i[-1] - reverse(s[0:len(s)-1])
        #return i[-1] - reverse(s[:-1])
#맨 마지막 한글자를 뒤집는다 = i[-1] - 그리고 마지막 index가 이미 뒤집어져 있으니까 그 다음 뒤부터 나열
print(user_input)
print('-' * 40)
