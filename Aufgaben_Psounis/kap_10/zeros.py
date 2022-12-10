import time
import timeit

nums = [1,2,6,9,3,7]


def timing_with_time():
    start = time.perf_counter()
    time.sleep(1)
    end = time.perf_counter()
    print(end - start)


# code Bucket solution (https://youtu.be/FD3blpwdRPY)
def zerosmove(nums):
    l=0
    for r in range(len(nums)):
        if nums[r] != 0:
            firstnumber = nums[l]
            secondnumber = nums[r]
            nums[l] = secondnumber
            nums[r] = firstnumber
            l += 1
    # return nums
    print(nums, "Bucket")

# =======================

# my solution
def movezeros(nums):
    l, i, j = len(nums), 0, 0

    while i < l and j < l:
        if nums[i] == 0:
            elem = nums.pop(i)
            nums.append(elem)
            j += 1
        else:
            i += 1
    # return nums
    print(nums, "jim")

# =========================
def main():
    #print("bucket\t\t", timeit.timeit(zerosmove(nums)))
    #print("jim\t\t", timeit.timeit(movezeros(nums)))
    zerosmove(nums)
    timing_with_time()
    movezeros(nums)
    timing_with_time()

if __name__ == '__main__':
    main()

