import random
hidden = random.randrange(1, 100)
print(hidden)
count = 0
max_guesses  = 5

print('you have ' + str(max_guesses) + ' tries...')
print('to guess the hidden number (1-100): ')

guess = int(input('give a number: '))

while True:
    count += 1
    if count == max_guesses:
        print('you lose!')
        break

    if guess > hidden:
        print('it is smaller!')
    elif guess < hidden:
        print('it is bigger!')
    else:
        print('you found it!')
        break
    guess = int(input('give a number: '))



