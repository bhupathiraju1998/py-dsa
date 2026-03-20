nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
# Output = 6

max_count = 0
l = 0
zero_count = 0
for r in range(len(nums)):

    if nums[r] == 0:
        zero_count+=1

    if zero_count > k:
        if nums[l] == 0:
            zero_count -= 1
        l+=1

    max_count = max(max_count,r-l+1)

print(max_count)