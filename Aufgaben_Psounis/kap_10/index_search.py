a_list = [1, 2, 4, 6, 8, 16, 45, 48]

def binarysearch(nums, target):
    a = 0
    b = len(nums)
    if target in nums:
        while a < b:
            index = (a + b) // 2
            if nums[index] < target:
                a = index
            elif nums[index] > target:
                b = index
            else:
                return index
    return -1

# play loop

while True:
    my_number = int(input('\nnumber to search: '))
    result = binarysearch(a_list, my_number)

    if result != -1:
        print(f'index number of ' + str(my_number) + ' is: ' + str(result))
    else:
        print('Sorry there is no such number!')
    print('=======================')
    more = input('press q to finish otherwise press enter: ')
    print('=======================')
    if more == 'q':
        print('Bye Bye')
        break





