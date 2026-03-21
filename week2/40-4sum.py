nums = [1, 0, -1, 0, -2, 2]
target = 0
# Sort the array
# Fix two numbers using two loops (i, j)
# Use two pointers (left, right) to find remaining two numbers
# Skip duplicates to ensure uniqueness
nums.sort()


res = []

n = len(nums)
for i in range(n):
    if i > 0 and nums[i] == nums[i-1]:
        continue
    for j in range(i+1,n):
        if j > i+1 and nums[j] == nums[j-1]:
            continue
        left = j + 1
        right = n -1
        while left < right:
            total = nums[i] + nums[j] + nums[left] + nums[right]

            if total == target:
                res.append([nums[i], nums[j], nums[left], nums[right]])

                left += 1
                right -= 1

                while left < right and nums[left] == nums[left-1]:
                    left += 1

            elif total < target:
                left += 1
            else:
                right -= 1
