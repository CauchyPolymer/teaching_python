t = (1,2,3.14) # collection(sequence,mapping)
print(type(t)) # sequence - list,range,tuple // mapping - map
# TUPLE은 ()를 쓰는데, context에 따라 ()를 생락 할 수도 있음. 그리고 immutable
t = t+(4,5)
print(t)

t = 1,2,3.14
print(t)

print('-' * 40)

s = set() #SET은 바뀔 수 있다.
print(type(s))
s={}
print(type(s))

s={'ab','cd','ef'}
print(s)
s = {'ab','cd','ef','ab'}
print(s)

l = ['apple','banana','apple','apple'] #list에서는 각각 다 다른 아이템, 하지만 튜플은 집합적이라 중복이 제거 됨.
s = set(l)
print(s)

s1 = {1,2,3}
s2 = {2,3,4}
print('Union is {}'.format(s1.union(s2))) #합집합 - 새로운 SET을 만듬.
print('intersection is {}'.format(s1.intersection(s2))) #교집합
print('Difference is {}'.format(s1 - s2)) #차집합

s1.add(100) #아이템 추가인데, 순서 없이 추가됨.
print(s1)
s1.remove(3)
print(s1)
s1.clear() #아예 셋을 비울 수 있다.
print(s1)
s1.add(None) # NONE과 TRUE역시 값이기 때문에 SET에 들어갈 수 있다.
s1.add(True)
print(s1)
