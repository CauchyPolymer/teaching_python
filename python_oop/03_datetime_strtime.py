#strftime = date, time, datetime을 str로 formatting을 해주는 함수
#strptime = 여기서 p는 parse임. str을 date, time, datetime으로 치환. f랑 p랑 반대되는 개념
import datetime
today = datetime.date.today()

today.stftime('%Y-%B-%d')
today.stftime('%B,%d,%Y')
now = datetime.datetime.now()
now.strftime('Day %d, Hour %H') #여러가지 표현을 할 수 있음.

#strptime 의 예제
s = 'year 2015 mo 05 d 15' #str이기 떄문에 계산 불가
t = 'year 2017 mo 03 d 20'
# s - t 는 말이 안됨 하지만 date로 바꾼 다음에 뺄 수 있음, 그럴때 strptime을 사용.

ds = datetime.datetime.strptime(s,'year %Y mo %m d %d') #첫 args를 내가 바꿔줄 str을 넣는다.
dt = datetime.datetime.strptime(t,'year %Y mo %m d %d')
dt - ds #이것은 가능하다. formatting도 가능.
(ds - dt).days
