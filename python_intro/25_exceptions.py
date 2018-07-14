

a = [1, 2, 3]
#print(a[3]) # IndexError

b = {'k1':1, 'k2':2, 'k3':3}
#print(b['k4']) #Key Error
#print(c)

import random
#random.randrangee(100) #AttributeError randrangee라는 것이 없어서 나는 에러
#attribute란? 어떤 variable./여기에오는것/ 을 attribute
def func (a,b):
    print(a,b)

#func(500) #TypeError
#print(int('apple')) #Value Error
#import randomm #ImportError import잘못 적은것.

#x = flaot(input('Enter numer: ')) #error(exception) handling
#y = float(input('Enter denom: '))

#print(x/y) # potential ZeroDeivisionError 0이 분모일때 나는 에러
#
# if abs(y-0.0) < 0.00001: #if를 써서 에러가 날 확률을 줄여준다. 여기서는 y=0일때 성립하지 않는 식이기 때문에
#     print('cannot divide by zero') # y=0 *** abs(절대값임)
# else:
#     z = x / y
#     print('x/y = {:.2f}'.format(z)
#
# try: #이 부분에서 exception이 발생해도 실행된다.
#     z = x/y #try block
#     #print('x/y = {:.2f}'.format(z))
# except:
#     print('Exceptional event') #이 부분부터 실행된다. #except block
# else:
#     print('x/y = {:.2f}'.format(z))
# finally: #상관없이 무조건 실행되는 경후
#     print('Clean up')
#

# try: #try가 있으려면 except나 fianlly중에 하나는 있어야 함. except는 여라가지가 있을 수 있다. exception에 이름을 적어준다.
#     x = float(input('Enter numer:'))
#     y = float(input('Enter denom:'))
#     a = ['apple']
#     z = x/y
#     print(a[int(z)]) CTRL + C keyboard error으로 터미널이 꺼집니다.

except ZeroDeivisionError:
    print('cannot divide by 0')
except Exception as e:
    print('Ration >= 1')
    print(e)
except ZeroDivisionError:
    print('please try again')
except IndexError as e:
    print('Ration >= 1')
    print(e)

# try:
#     x = float(input('Enter Numer : '))
#     y = float(input('Enter Denom : '))
#
#     a = ['apple']
#     z = x/y
#     print(a(int(z)))
# except:
#     print('please try again : ')
