# arr =[ 1,2,1,1,1]
k=5
# longest subarray sum equalsk non negative we use 2 pointer or sliding window
nums=[1,2,1,1,1]
max_length = 0
l = 0
current_sum = 0
for r in range(len(nums)):

    current_sum += nums[r]

    while current_sum > k and  l <= r:
        current_sum -= nums[l]
        l += 1 

    if(current_sum == k):
        max_length = max(max_length,r - l + 1)

print(max_length)


# ii) if negative number we use prefix sum with hash map
nums2=[3, 1, -1, 2, 5, -2, 3]
target = 5

max_ans= 0
prefix_map={}
prefix_sum = 0

for i in range(len(nums2)):
    prefix_sum += nums2[i]
    needed = prefix_sum - target
    if needed in prefix_map:
        max_ans = max(i-prefix_map[needed],max_ans)

    if prefix_sum == target:
        max_ans = max(max_ans,i+1)

    if prefix_sum not in prefix_map:
        prefix_map[prefix_sum] = i

print(prefix_map)


# chatgpt ans
nums = [3,1,-1,2,5,-2,3]
k = 5
prefix_map = {0: -1}  # 0 at index -1 helps handle subarrays starting at index 0
prefix_sum = 0
max_len = 0

for i in range(len(nums)):
    prefix_sum += nums[i]
    if prefix_sum - k in prefix_map:
        max_len = max(max_len, i - prefix_map[prefix_sum - k])
    if prefix_sum not in prefix_map:
        # we wrote this if bcoz if we have multiple sum whose value is alredy present it will reqetie the index but since we want longest we ave the first index
        prefix_map[prefix_sum] = i

print(max_len)

# Problem	Initialization
# Longest subarray	{0:-1}
# prefix_sum → first index
# {sum:index}

# When finding LONGEST subarray length

# Example problem:
# Longest subarray with sum = K

# We initialize:

# prefix_map = {0: -1}
# Why?

# If the subarray starts from index 0, we want:

# length = i - (-1)

# which gives:

# i + 1

# So this automatically handles the case where prefix_sum == target.

# Example:

# nums = [2,3]
# target = 5

# At i = 1
# prefix_sum = 5
# needed = 5 - 5 = 0

# Map:
# {0:-1}
# Length:
# 1 - (-1) = 2
# Correct.



# ////////////////////
# Sure! Let’s dry run your code in single-line steps for

# nums = [3,1,-1,2,5,-2,3], k = 5
# Initial state
# prefix_sum = 0, max_len = 0, prefix_map = {0: -1}
# i = 0, nums[0] = 3
# prefix_sum = 0 + 3 = 3
# prefix_sum - k = 3 - 5 = -2 → not in map
# map: 3 not in map → add 3:0
# prefix_map = {0:-1, 3:0}
# max_len = 0

# i = 1, nums[1] = 1
# prefix_sum = 3 + 1 = 4
# prefix_sum - k = 4 - 5 = -1 → not in map
# map: 4 not in map → add 4:1
# prefix_map = {0:-1, 3:0, 4:1}
# max_len = 0

# i = 2, nums[2] = -1
# prefix_sum = 4 + (-1) = 3
# prefix_sum - k = 3 - 5 = -2 → not in map
# map: 3 already in map → skip
# prefix_map = {0:-1, 3:0, 4:1}
# max_len = 0

# i = 3, nums[3] = 2
# prefix_sum = 3 + 2 = 5
# prefix_sum - k = 5 - 5 = 0 → 0 in map at index -1
# length = 3 - (-1) = 4 → max_len = 4
# map: 5 not in map → add 5:3
# prefix_map = {0:-1, 3:0, 4:1, 5:3}

# i = 4, nums[4] = 5
# prefix_sum = 5 + 5 = 10
# prefix_sum - k = 10 - 5 = 5 → 5 in map at index 3
# length = 4 - 3 = 1 → max_len = max(4,1) = 4
# map: 10 not in map → add 10:4
# prefix_map = {0:-1, 3:0, 4:1, 5:3, 10:4}

# i = 5, nums[5] = -2
# prefix_sum = 10 + (-2) = 8
# prefix_sum - k = 8 - 5 = 3 → 3 in map at index 0
# length = 5 - 0 = 5 → max_len = 5
# map: 8 not in map → add 8:5
# prefix_map = {0:-1, 3:0, 4:1, 5:3, 10:4, 8:5}

# i = 6, nums[6] = 3
# prefix_sum = 8 + 3 = 11
# prefix_sum - k = 11 - 5 = 6 → not in map
# map: 11 not in map → add 11:6
# prefix_map = {0:-1, 3:0, 4:1, 5:3, 10:4, 8:5, 11:6}
# max_len = 5
# ✅ Final Result
# max_len = 5
# Longest subarray = [1, -1, 2, 5, -2]