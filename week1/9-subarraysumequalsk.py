# Given an integer array nums and an integer k, return the total
#  number of continuous subarrays whose sum equals k.
# A subarray must be contiguous.
# Input: nums = [1,1,1], k = 2
# Output: 2
nums=[1,1,1]
k = 2

current_sum = 0
count = 0
dict = {0:1}
for each in nums:
    current_sum += each
    diff = current_sum - k
    count += dict.get(diff,0)
    dict[current_sum] = dict.get(current_sum,0) + 1



