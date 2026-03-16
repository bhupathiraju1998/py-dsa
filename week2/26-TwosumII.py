nums=[1,3,5,4,7,10,11]
target = 9
#find 2 sumber taht target to specific number in an sorted 1 based index array using two pointers

l = 0
r = len(nums) - 1
while l < r :
    currSum = nums[r] + nums[l]
    if  currSum > target:
        r -= 1
    elif currSum < target:
        l += 1
    else:
        print(l+1,r+1)
        break
