import random

def random_numbers():
    r = random.randrange(1,101)
    return r

r = random_numbers()
go = True
while go:
    guessed_number = input('guess the number : ')
    if int(guessed_number) == r:
        print('Congratz!')
        go = False
    elif int(guessed_number) < r:
        print('TOO LOW')
    else :
        print('TOO HIGH')
