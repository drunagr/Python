import random
hidden_number = random.randrange(10, 1000)

tries = 5

print('you have ' + str(tries) + ' tries...')
guess = int(input('to guess the hidden number (10-1000): '))


while guess <10 or guess > 1000:
    print('the number must be between 10 and 1000')
    guess = int(input('try again (10-1000): '))

for i in range(0,tries-1):
    if hidden_number == guess:
        print('bravo, you found it!')
        break
    elif guess < hidden_number:
        print('the hidden number is bigger!')
    else:
        print('the hidden number is smaller!')
    guess = int(input('try again: '))
else:
    print('==============')
    print('Sorry you lost...\n' + 'the hidden number was: ' + str(hidden_number))