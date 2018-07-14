print('Testing break statement in for loop...')
print()

for x in range(10):
    if x == 5:
        break #아예 끝나버림.
    else:
        print(x)

print()
print('Testing break statement in for loop...')
print()

for y in range(10):
    if y == 5:
        continue #그 회차가 끝남. cont는 별로 쓰지 않음 ㅎ
    #while loop 할때 조심해야 할 점이 있음 continue 쓸때는
    #for은 컬렉션 가지고 반복을 해서 무한루프에 잘 안빠지는데 와일은 그럴 확률이 있음.
    print(y)
    if y == 5:
        print('Exit!')

print()
print('WARNING: Testing continue statment in while loop..')
