nums = [10, 20, 30, 40]
k = 50

l = 0
r = len(nums) -1
max_sum = -1

while l < r:
    total = nums[l] + nums[r]

    if total < k:
        max_sum = max(max_sum,total)
        l += 1
    else:
        r -= 1
print(max_sum)