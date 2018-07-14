my_list = ['apple', 'banana', 'cherry', 'durian'] #str 4개짜리 리스트를
print(my_list) #그냥 프린트하면 그대로 프린트가
print(' '.join(my_list))#''.join(리스트나 컬렉션) list안에 있는 아이템을 str로 만들어서 붙여주고 ''안에 있는 글자를 끝에 넣어줌
print('\n'.join(my_list))# 구분을 ''안으로 해준다는 것.
print(' -*- '.join(my_list))

print('-' * 40)

print('apple banana blue cherry durian'.split())
#split은 그 과정이 반대임. ''.split()
#''안의 스트링을 쪼개서 리스트로 만드는 과정.
print('apple, banana, blue cherry, durian'.split(sep=',')) #separator
#여기서는 ',' 기준으로 자르는 것
print('-' * 40)

print('abc'.strip()) #양 끝에 빈칸을 다 없애줌.
