f = open('record.txt',
        encoding='UTF-8',
        mode='wt')

f.write('name, gender, age\n')

name = 'Alice'
gender = 'F'
age = 15
f.write('{},{},{}\n'.format(name, gender, age))

name = 'Bob'
gender = 'M'
age = 14
f.write('{},{},{}\n'.format(name,gender,age))

f.close() #파일은 다 쓰고나면 close 해야함!

#######

import random

try:
    f = open('read_write.txt',
    encoding='UTF-8',
    mode='r')
except FileNotFoundError:
    old_content = '(empty)'
else:
    old_content = f.read()
    f.close()

print('Old content is {}'.format(old_content))

f = open('read_write.txt',
encoding='UTF-8',
mode = 'w') #w를 하면 전에 있던 값을 덮어 씌워버림. 뒤에 붙이려면 append mode가 있음!

new_content = str(random.random())
f.write(new_content)
f.close

print('New content is {}'.format(new_content))
