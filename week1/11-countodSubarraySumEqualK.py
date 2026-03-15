nums = [1,2,3,2]
k = 3
prefix_map = {0: 1}  # 0 sum occurs once (empty prefix)
prefix_sum = 0
count = 0

for num in nums:
    prefix_sum += num
    if prefix_sum - k in prefix_map:
        count += prefix_map[prefix_sum - k]
    prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1

print(count)

# Count subarrays	{0:1}
# prefix_sum → frequency
# {sum:count}

# When COUNTING subarrays

# Example problem:
# Number of subarrays with sum = K

# We initialize:

# prefix_map = {0: 1}
# Why?

# Because sum 0 has occurred once before the array starts.

# Example:

# nums = [3]
# target = 3

# At index 0:

# prefix_sum = 3
# needed = 0

# Map:

# {0:1}

# So we add 1 valid subarray.

# ///////////////
# Sure! Let’s dry run your counting subarrays code step by step in single-line style.

# We have:

# nums = [1,2,3,2]
# k = 3
# prefix_map = {0:1}  # empty prefix sum occurs once
# prefix_sum = 0
# count = 0

# i = 0, num = 1
# prefix_sum = 0 + 1 = 1
# prefix_sum - k = 1 - 3 = -2 → not in map
# count = 0
# update map: prefix_map[1] = 0 + 1 → 1
# prefix_map = {0:1, 1:1}

# i = 1, num = 2
# prefix_sum = 1 + 2 = 3
# prefix_sum - k = 3 - 3 = 0 → 0 in map, freq = 1
# count = 0 + 1 = 1
# update map: prefix_map[3] = 0 + 1 → 1
# prefix_map = {0:1, 1:1, 3:1}

# Subarray contributing to count: [1,2]

# i = 2, num = 3
# prefix_sum = 3 + 3 = 6
# prefix_sum - k = 6 - 3 = 3 → 3 in map, freq = 1
# count = 1 + 1 = 2
# update map: prefix_map[6] = 0 + 1 → 1
# prefix_map = {0:1, 1:1, 3:1, 6:1}

# Subarray contributing to count: [3]

# i = 3, num = 2
# prefix_sum = 6 + 2 = 8
# prefix_sum - k = 8 - 3 = 5 → 5 not in map
# count = 2
# update map: prefix_map[8] = 0 + 1 → 1
# prefix_map = {0:1, 1:1, 3:1, 6:1, 8:1}

# ✅ Final Result
# count
# Subarrays with sum = 3:
# [1,2]
# [3]