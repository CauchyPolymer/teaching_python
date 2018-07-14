print(True)
print(False) #list나 dict같은 경우 아이템이 하나도 없으면 거짓.
print(type(True))#none type 에서 none 이면 거짓
print(type(False))
print('-' * 40)

print(bool(1))
print(bool(0)) #0이 아닌 모든 것은 참. 0이면 거짓
print(bool(1))
print('-' * 40)

print(bool(3.14))
print(bool(0))
print(bool(-1.4))
print('-' * 40)

print(bool('3.14'))
print(bool('0'))
print(bool('')) #empty string은 거짓
print('-' * 40)

print(bool(['a','b']))
print(bool([1]))
print(bool([]))
print('-' * 40)


print(bool({'name': 'Alex'}))
print(bool({}))
print('-' * 40)

print(bool(None))
print('-' * 40)

print(int(True))
print(int(False))
print('-' * 40)
