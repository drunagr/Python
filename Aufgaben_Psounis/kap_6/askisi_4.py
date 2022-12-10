N = int(input('give a number: '))

if N == 0 or N == 1:
    print('it is not a prime')
else:
    for i in range(2, N):
        if N % i == 0:
            print('it is not a prime')
            break
    else:
        print('it is a prime')
