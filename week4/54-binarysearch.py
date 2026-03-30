# logbase2n = x , means x times we can divide n with 2 == 2 ** x = n

nums = [1, 3, 5, 7, 9, 11, 13]
target = 7

l = 0
n = len(nums) -1 
r = n 

while  l <= r:
    mid = l + (r-l)//2

    if nums[mid] > target:
        r = mid - 1
    elif nums[mid] < target:
        l = mid + 1
    else:
        print(mid)
        break
