l = ['apple', 'banana', 'cherry'] #콜렉션을 만드는 두가지 방법중(list, dict) 하나. DICTIONARY(=Hash map, Hash table)
#list에는 index(무조건 숫자int)가 있고, dict에는 key(대부분 스트링str!)가 있다. 가끔 key를 index라고 부르는경우 있는데 그럼 안됨.
#dict만들떄는 {}를 쓴다. 이걸 쓰는 이유는 key값을 가지고 관리하자 해서 순서가 아님.
d = {} #empty_dictionary
print(type(d))

d = {'name' : 'JongHyun', 'age': 25, 'weight': 85} #item 3개짜리의 딕셔너리
#순서 가지고 하는게 아니기 때문에, key와 value를 구분해준다. age에 해당하는 값 25.
#dict 안에 dict 들어가는게 가능하지만 굉장히 비효율적이라 다르게 만드는게 나음 ㅋ
print(d)
#나오는 순서가 다 다를 수 있지만, 한 번 나오면 계속 그렇게 나옴

print('the name is {}'.format(d['name']))

d['name'] = 'Lim'

print('the name is {}'.format(d['name']))

#l[10] = 'durian'

d['gender'] = 'male' #
d['age'] = 25
d['gender'] = 'NTS'
d['last_name'] = 'Lim'
del d['name']

#print(d['address']) 없는걸 만들 수 는 있지만 읽는 건 안됨됨 

print(len(d))

d['address'] = ['Seoul', 'South Korea']
print(d)
