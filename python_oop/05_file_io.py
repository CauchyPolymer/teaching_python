f = open('some_text.txt', #open이라는 빌트인 펑션을 통해서 파일을 읽고 쓰는게 가능하다.
encoding='UTF-8', mode='rt') #OS가 메모리를 잘 관리 해줌. 같은 dir에 있으니까 파일명만 써주면 되는데 다른 디렉에 있으면 지정해줘야함.
#mode는 두글자가 들어가는데 첫 글자는 r(read) or w(write)임
#file은 binary file 과 text file로 나누어 진다. 구분이 그렇게 베타적인건 아님. 모든 파일은 일단 바이너리 파일임. 모든 파일은 기본적으로 기계어로 저장되기 때문.
#하지만 거기에다가 글자라는 매개를 부여한 것이 text파일. 그 과정이 encoding이다. 반대 과정은 decoding
#기계어로 하는게 힘드니까 128개의 ASCII CODE를 40년대에 개발함. 이것을 표현하기 위해서는 text하나 하나가 1byte=8bit임(컴의 가장 기본적 단위)
#하지만 ASCII는 영어만 표현 가능했음! 그래서 나온게 Latin - 1 이다. 하지만 그리스 문자나 러시아어 동양어가 표현 불가했음
#즉 글자를 1byte 가지고 표현하는게 무리라는 것 왜냐면 256개 이상의 문자가 있기 때문. 그래서 2byte(16bit)나왔는데 그게 UTF-16이다.
#utf 16의 65000개도 적었다 == 이유는 이모티콘부터 고대문자까지 variation이 더 많았던 것. fixed width 보다는 variable-width가변 길이의 인코딩이 중요.
#UTF-8 (1-4byte)의 아이템이 나옴. 1바이트에는 자주쓰는거 4바이트에는 잘 안쓰는 언어를 할당. 그리하여 대세가 됨.


# s = f.read() #read는 전체를 한번에 다 읽는거고
# print(s)

for l in f: #f를 for안에 넣으면 한 줄씩 읽는다.
   print(l,end='') #end를 없애면 줄바꿈이 들어감. 줄바꿈을 두번하기 떄문에

f.close() #file object
print('-' * 40)
###########

import datetime
f = open('profile.txt')
line_no = 1
for line in f:
    if line_no == 1:
        spl = line.split(' ')
        print('First Name : {}'.format(spl[0]))
        print('Last Name : {}'.format(spl[1]))
    elif line_no == 2:
        print('Gender : {}'.format(line),end='')
    elif line_no == 3:
        if line[-1] == '\n':
            line = line[:-1]
        dt = datetime.datetime.strptime(line, '%Y-%m-%d')
        fmt = dt.strftime('%B-%d-%Y')
        print('Birthday : {}'.format(fmt),end='')
    line_no += 1
print()
f.close()
