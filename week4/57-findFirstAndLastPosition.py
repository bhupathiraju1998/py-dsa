nums = [5,7,7,8,8,10]
target = 6

# op is [3,4]


def binarySearch(leftbias:bool)->int:
    l = 0
    r = len(nums) -1
    i = -1
    while l <= r :
        mid = l + ((r-l)//2)

        if target > nums[mid]:
            l = mid +1
        elif target < nums[mid]:
            r = mid - 1
        else:
            i = mid
            if leftbias:
                r = mid -1
            else:
                l = mid +1

    return i
print('leftIndex',binarySearch(True))
print('rightIndex',binarySearch(False))