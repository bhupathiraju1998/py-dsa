# Given an integer array nums, return an array answer such that
#  answer[i] is the product of all elements of nums except nums[i].
nums=[1,2,3,4]

res = [1] * len(nums)

 
prefix = 1
for i in range(len(nums)):
    res[i] = prefix
    prefix *= nums[i]

suffix = 1
for i in range(len(nums)-1,-1,-1):
    res[i] *= suffix
    suffix *= nums[i]

print(res)