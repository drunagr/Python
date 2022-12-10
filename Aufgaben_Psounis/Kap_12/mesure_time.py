import time
from functools import cache

a_list = [1, 2, 4, 6, 8, 16, 45, 48, 50, 51, 52, 54, 57, 58, 60, 62, 64, 65, 68, 69, 70, 73, 75, 76, 78, 79, 80, 82, 84,
          85, 87, 88, 89]
nums = [1, 0, 0, 5, 4, 6, 7, 8, 7, 4, 56, 23, 0, 12, 0, 2, 3, 4, 5, 6, 7, 0, 0, 33]


def measure_time(func):
    def wrapper(*arg):
        t = time.time()
        res = func(*arg)
        print("Function took " + str(time.time() - t) + " seconds to run")

        return res

    return wrapper


@measure_time
def binarysearch(nums, target):
    time.sleep(1)
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
                return print("index is: ", index)
    return -1


@measure_time
def zerosmove(nums):
    time.sleep(1)
    l = 0
    for r in range(len(nums)):
        if nums[r] != 0:
            firstnumber = nums[l]
            secondnumber = nums[r]
            nums[l] = secondnumber
            nums[r] = firstnumber
            l += 1
    # return nums
    print("bucket: ", nums)


@measure_time
def movezeros(nums):
    time.sleep(1)
    l, i, j = len(nums), 0, 0

    while i < l and j < l:
        if nums[i] == 0:
            elem = nums.pop(i)
            nums.append(elem)
            j += 1
        else:
            i += 1
    # return nums
    print("jim:    ", nums)


@measure_time
def myFunction(n):
    time.sleep(n)


if __name__ == "__main__":
    # myFunction(2)
    binarysearch(a_list, 1)
    zerosmove(nums)
    movezeros(nums)
