nums = [-1,2,1,-4]
target = 1
# Output = 2
# Given an array nums and a target target, find three integers in nums such that the sum is closest to target. Return the sum.

nums.sort()
closest_sum = float('inf')

for i in range(len(nums) -2):
    left,right = i+1,len(nums)-1

    while left < right:
        current_sum = nums[i] + nums[left] + nums[right]

        if(abs(target -current_sum)) < abs(target-closest_sum):
            closest_sum = current_sum
        
        if current_sum < target:
            left += 1
        elif current_sum > target:
            right -= 1
        else:
             closest_sum = current_sum
             break
print(closest_sum)