numbers = []

print('give a number (3-20): ')
n = int(input())

while n < 3 or n > 20:
    print('the number must be (3-20): ')
    n = int(input())
print('---you must give ' + str(n) + ' numbers---')

for i in range(1, n+1):
    print('give ' + str(i) + 'st number: ')
    zahl = int(input())
    numbers.append(zahl)

numbers.sort()

print('here is your list: ')
print(numbers)