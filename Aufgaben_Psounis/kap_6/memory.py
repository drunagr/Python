import random

# N only Even please (6-18)...
N = 4

hidden1 = []
while len(hidden1) < N//2:
    zahl = random.randrange(0, 9)
    if zahl not in hidden1:
        hidden1.append(zahl)

hidden = 2 * hidden1[:]

# print(hidden)

state = []

for i in range(0,N):
    state.append("closed")

# print(state)

print('======================================')

# other states : open, temp_open

active_game = True
found = 0
score = 0

while active_game:
    score += 1
    # read first position
    first_position = int(input('give first position (0-'+ str(N-1) +') and closed:'))
    while (first_position < 0 or first_position >= N) or state[first_position] == 'open':
        print('error!')
        first_position = int(input('give first position (0-'+ str(N-1) +') and closed:'))


    # read second position
    second_position = int(input('give second position (0-'+ str(N-1) +') and closed:'))
    while (second_position < 0 or second_position >= N) or state[second_position] == 'open' \
                                                     or second_position == first_position:
        print('error!')
        second_position = int(input('give second position (0-'+ str(N-1) +') and closed:'))


    # change state: both temp_open
    state[first_position] = 'temp_open'
    state[second_position] = 'temp_open'

    # print current state
    # print('')
    for position in range(N):
        if state[position] == 'closed':
            print(' _ ', end='')
        elif state[position] == 'open':
            print(' ',hidden[position], end='')
        else:
            #temp_open
            print('',hidden[position], end='')
    print('')

    # check if same then open, else closed
    if hidden[first_position] == hidden[second_position]:
        state[first_position] = 'open'
        state[second_position] = 'open'
        print('Success')
        found += 2
        if found == N:
            print('======================================')
            print('bravo !! Game finished! Score = ', score)
            active_game  = False
    else:
        state[first_position] = 'closed'
        state[second_position] = 'closed'
        print('Failure')

    # print current state
    print('')
    for position in range(N):
        if state[position] == 'closed':
            print(' _ ', end='')
        elif state[position] == 'open':
            print(hidden[position], end='')
        else:
            #temp_open
            print(hidden[position], end='')
    print('')

