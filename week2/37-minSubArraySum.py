target = 7
nums = [2,3,1,2,4,3]
# Output = 2  → [4,3]

l = 0
minResLen = float("infinity")
curr_sum = 0

for r in range(len(nums)):
    curr_sum += nums[r]

    while curr_sum >= target:
        minResLen = min(minResLen, r-l+1)
        curr_sum -= nums[l]
        l += 1

print(minResLen)