def squre(x): #요것도 function object로 할당 된다.
    return x**2

a = squre(2)
print(a)

f = lambda x: x**2#이름이 안붙여져 있어서 직접 이름은 넣어줘야 한다.(anonymous)
#램다는 expression만 들어갈 수 있다.

b=f(2)b
print(b)

###

def expo(e):#함수를 리턴
    def wrapped(x): #x를 넣고 x^e를 리턴
        return x**e #펑션이 데이터 인것처럼 다루는 것을 functional programming.
    return wrapped

f = expo(3) #세제곱을 해주는 평선을 만들어주는 것
g = expo(4) #펑션을 만들어 주는 펑션을 만든다! - closure이라고 한다
print(f(2))
print(g(2))

def expo_v2(e):
    return lambda x: x**e

f2 = expo_v2(3)
g2 = expo_v2(4)
print(f2(2))
print(g2(2))
#객체지향 프로그래밍 직전까지의 코스는 끝
