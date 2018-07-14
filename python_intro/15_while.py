import random
# switch는 py에 없다.
# definite loop = for loop 횟수가 정해져 있어서! 횟수만큼 반복시킬 때.
# indefinite loop = while은 bool로 바꿨을 때 ture가 되면 항상 실행 시킴. False가 될 떄 까지. 정해져 있지 않고 조건이 나올 떄 까지.
# while loop 안에서 언젠가는 F로 만들 수 있는 조건이 있어야 함.


# go = True
# while go:
#     r = random.randrange(10)
#     if r == 5:
#         go = False
#     else:
#         print(r)

# go = True
# while go:
#     user_input = input('Please enter a word '
#     '(enter q to quit): ')
#     if user_input == 'q':
#         go = False
#     else:
#         print('You entered {}.'.format(user_input))

go = True
l = []
while go:
    user_input = input('Please enter a word' '(press just enter to stop) :')
    if user_input == '':
        go = False
    elif len(user_input) % 2 == 1:
        l.append(user_input)
print(l)
