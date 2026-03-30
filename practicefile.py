# I will give you a LeetCode problem name. 
# For each problem, respond in this exact format:

# - Problem statement (short, like LeetCode)
# - Example with Input, Output, Explanation
# - Constraints

# Do NOT include solution or approach.
    
# Problem: <problem name>


nums = [-2,1,-3,4,-1,2,1,-5,4]

temp_start = 0
start=end=0
max_sum = curr_sum = nums[0]

for i in range(len(nums)):
    if nums[i] > curr_sum+nums[i]:
        temp_start = i 
        curr_sum = nums[i]
    else:
        curr_sum += nums[i]

    if curr_sum > max_sum:
        start = temp_start
        end = i
        max_sum = curr_sum