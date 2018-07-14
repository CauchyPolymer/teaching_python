a = 'apple'
b = 'banana'
c = '''cran
berry''' #triple-quoted string
d = "donut"
print(a)
print(b)
print(c)
print(d)

e = "I don't "
print(e)

f = 'He said, "Yes" '
print(f)

g = '''He said, "I don't"'''
print(g)

h = 'He said, "I don\'t"' #역슬래시 \ 의 작은 따옴표는 string의 끝이 아니라, 그냥 ' 로써의 역할 표시
print(h)

i = "He said, \"I don't\"" # \ <- Escape Charater, Character Escaping
print(i)

j = 'apple \ndonut'
print(j)

k = 'Backslash \\ is below the delete Key.' #역슬래스 자체를 escape 한다는 것은 \ 자체를 사용하는 경우
print(k)

i = 'He said, "I can\'t come to the soccer game today."'
print(i)

print('apple' + 'mango') #string concatenation
#print('apple' - 'mango') string에서 string을 뺄 수 없어서 에러

print('apple' * 5)

l = len('apple')
print(l)

n = 10
print('My favorite number is' + str(n)) #int를 스트링화 시켜줄 수 있다

n = '20'
m = 2 + int(n)
print(m)
