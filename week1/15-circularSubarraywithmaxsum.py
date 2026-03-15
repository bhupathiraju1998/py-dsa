nums = [5, -3, 5]
max_ending_here = max_so_far = nums[0]
total_sum = sum(nums)
for i in range(1,len(nums)):
    max_ending_here = max(nums[i],max_ending_here+nums[i])
    max_so_far = max(max_ending_here,max_so_far)
min_ending_here = min_so_far = nums[0]
for i in range(1,len(nums)):
    min_ending_here = min(nums[i],min_ending_here+nums[i])
    min_so_far = min(min_ending_here,min_so_far)
max_circular = total_sum - min_so_far

if max_so_far > 0:
    result = max(max_so_far, max_circular)
else:
    result = max_so_far