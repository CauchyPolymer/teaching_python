# check = [False] * 365
# check = [False, False, ... 365개]
import random


# def birthdaycall():
#     check = [] #check이라는 birthday list만듬
#     for i in range(365): #false라는 index를 365개 만든다.
#         check.append(False)
#     go = True
#     while go: #
#         birthday = random.randrange(365)
#         if check[birthday] == True:
#             go = False
#         else:
#             check[birthday] = True
#     result = sum(check)
#     return result
#
# sum0 = 0
# for y in range(10000):
#     count = birthdaycall()
#     sum0 = sum0 + count
#
# avg = sum0/10000
# print(avg)

def birthdaycall2():
    check = [False] * 365

    count = 0
    while True:
        birthday = random.randrange(0,365)
        count += 1 #count = count + 1
        if check[birthday]:
            break
    else:
        check[birthday] = True

    return count

n = int(input('enter : '))
_sum =0
for i in range(n):
    _sum = _sum + birthdaycall2()

print(_sum/n)
