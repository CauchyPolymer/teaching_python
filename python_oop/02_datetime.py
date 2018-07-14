import datetime #날짜와 시간 데이터는 별도로 할당되어 있음. built in은 아님.import써야함.
# import뒤에 파이썬 설치할때 datetime.py라는 파일이 설치 됨. -> module = file 이라고 칭함.
# time, datetime은 naive or aware 둘이 서로 섞으면 안됨!
# naive = 오전 10시 공통된 가정이 있어서 틀릴 수 있음self.
# aware = 한국시간 오전 10시 (시간대 정보를 포함해서 표현)

###### TIMEZONE이란?
#date 와 date는 더할 수가 없고 뺄수는 있다. = time delta 임. 즉 date - td = date!
#예 #d1 = datetime.date(2017,12,21)
#d2 = datetime.date(2017,12,19) + datetime.timedelta(days=2)
#d1 == d2 #True라고 뜸!

# NAIVE 경우
# d1 = datetime.datetime(2017,12,21)
# d2 = datetime.datetime(2017,12,21,9)
# dt2 - dt1
# (dt2 - dt1)/3600 #이와같이 빼려면 naive는 naive끼리 함께 해야함.

# AWARE 경우
# d1 = datetime.datetime(2017,12,21,0,0,tzinfo=datetime.timezone(datetime.timedelta(hours=9))) #시차가 +9시간
# d2 = datetime.datetime(2017,12,21,0,0,tzinfo=datetime.timezone(datetime.timedelta(hours=8)))
# dt2 == dt1 #둘다 0시 0분인데 timezone이 달라서 다르다고 나옴. 한국 어딘가와 중국 어딘가의 차이
# d3 = datetime.datetime(2017,12,22,tzinfo=datetime.timezone(datetime.timedelta(hours=7)))
# dt1 == dt3 #는 시차가 다르기 때문에 9시 7시 시차에도 불구하고 True값임!


print(dir(datetime)) #dir == directory
print('-' * 40) #디렉토리 안에서 무엇을 쓸 수 있는지 보여줌 .이후 쓸 수 있는 것들

my_dir = [s for s in dir(datetime) # __asdad__ 처럼 __앞뒤로 있는건 내부적으로 사용하는 모듈이라 쓸데가 없음
            if not s.startswith('__')] # 그 모듈들을 모두 제거하기.

print('\n'.join(my_dir))
print('-' * 40)

print(datetime.date)
print(datetime.time)
print(datetime.datetime)
print(datetime.timezone) #시차계산
print(datetime.timedelta) #시간과 시간의 차이이
print('-' * 40)
####################
d1 = datetime.date(2017,8,16) #date라고 하는 type
print(d1,type(d1))
d2 = datetime.date(year = 2017, month = 8, day =16) #keyword args
print(d2,d1==d2)

d3 = datetime.date.today() #type 다음에 오는 ()가 있는 것들은 method 라고 함.
print(d3)
print(d3.year)
print(d3.month)
print(d3.day)
print(d3.weekday())
print('-' * 40)
print(d3.strftime('%Y -*- %m -*- %d')) #strftime = string format time : date를 스트링으로 바꿀 때 쓴다.
######################

td = d3 - d2
print(td)
print(type(td)) #date끼리 뺴면 .timedelta라는 다른 type이 나옴

print('-' * 40)
############
t1 = datetime.time(10,20,30) #keyword args 쓰면 마음대로 순서 지정 가능, positional은 시분초 순서.
print(t1)
t2 = datetime.time(hour=10, minute=30, second=20)
print(t2)
t3 = datetime.time(hour=10, minute=30, second=20, microsecond=500)
print(t3)

print(t3>t2)
print('-' * 40)
##############

td = datetime.timedelta(hours=9)
tz = datetime.timezone(td)
t4 = datetime.time()
