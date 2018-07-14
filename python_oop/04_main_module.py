#파이선은 두개 이상의 모듈로 이루어 질 수 있다.
# #파일 == 모듈
# import random #이런 경우 역시 random이라는 미리 만들어진 모듈을 찾아서 가지고 오는 경우임
# print(random) #파이썬이 처음 설치가 될때 같이 된 것임~!
# print(type(random))
# print(random.random())
# print('-' * 40)

import lib_module
print('-' * 40)
#import lib_module #import 를 두번한다고 두번실행되지 않는다

#import를 할때 어떤일이 벌어지는가?
#lib_module이라는 이름을 가진 파일을 찾는다.
# 1. 같은 디렉토리에서 찾는다. module search! (없다면, 시스템 디렉토리에서 찾는다.하나만 찾으면 끝남.)
# 2. 실행
# 3. 연결 - 파일 이름을 정할때 시스템 모듈과 겹치는 이름은 쓰면 안좋음.

print(lib_module.a) #1 2 3번의 과정이 실행되는 것을 볼 수 있음.
print(lib_module.b) # 모듈 명 뒤에 . 을 찍으면 모듈 안에 있는 global 변수들을 사용 할 수 있다.
print(lib_module.pi())
print(lib_module.my_list[0])
print(lib_module.d)
#print(lib_module.c) #local scope라 실행 안됨 ㅋ 이것이 파이선에서 다른 모듈을 import한다의 뜻.
print('-' * 40)

#print(lib_module.__dict__) #저 특별변수를 쓰게 되면 global에 해당하는 명령어와 변수가 모두 나온다. 근데 드럽게 나오니까 for loop을 써보자
for attr in lib_module.__dict__:
    print(attr)
print('-' * 40)
################################ from import statement!
from lib_module import a,b # 그 모듈에서 import할 variable을 따로 적어줌.
print(a)
#print(lib_module.b) #이 상황에서는 불가능함. lib_module은 그냥 중간단계 였기 때문.
print(b)
#from random import randrange #random.randrange 같은거임.
#print(randrange(10))

from random import randrange as rr #as는 이름을 바꿀 수 있음. 이름이 겹치는걸 방지하기 위함.
print(rr(10))
print('-' * 40)
import lib_module

print(lib_module) #lib_module은 그냥 이름이라 모든 오브젝트를 연결시켜 주는 것임.
# lib_module = 'abc' #lib_module이 모듈 오브젝트에 연결 되어있는데, abc로 바꾼다는 것은, 모듈 오브젝트 자체가 abc로 바뀐다는 것.
# print(lib_module)
print('-' * 40)

print(lib_module.a)
lib_module.a = 200 #여긴 lib_module을 찍고 들어가서 안에있는 모듈 오브젝트를 바꾼 것
print(lib_module.a)
lib_module.aaa = 1000 #aaa라고 아예 없던게 생김
print(lib_module.aaa) #모듈 밖에서도 수정이 가능하게 자유도가 높음. 하지만 이게 가능하다고 해서 권장되지는 않는다. 빜

print(dir(lib_module)) #dict에서 key값들을 뺀거랑 비슷한 것.
# dict 는 오브젝트에 붙은 애들만 정리하고, dir은 상속처럼 연결 되어 있는 것 까지 정리해줌.

import random
#print(dir(random)) #obj안에 붙어있는 속성들을 attribute라고 한다.
print('-' * 40)

import builtins #builtin scope에 있는 애들을 보여준다.
print(dir(builtins))
