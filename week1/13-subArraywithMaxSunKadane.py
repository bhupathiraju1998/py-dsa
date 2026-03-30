nums = [-2,1,-3,4,-1,2,1,-5,4]
max_sum = curr_sum = nums[0]


for i in range(1,len(nums)):
    curr_sum = max(nums[i],curr_sum+nums[i]) #key step to kadane
    max_sum = max(curr_sum,max_sum)
print(max_sum)

# ifi we want index also we need write in new way

max_s = curr_s = nums[0]
start = end = 0
temp_start = 0
for i in range(1,len(nums)):
    if nums[i] > curr_s+nums[i]:
        temp_start = i
        curr_s = nums[i]
    else:
        curr_s += nums[i]

    if curr_s > max_s:
        max_s = curr_s
        start = temp_start
        end = i
print("Maximum sum:", max_s)
print("Subarray:", nums[start:end+1])
print("Indices:", start, "to", end)



# Maximum subarray sum ≤ k
# Maximum product subarray
# Maximum sum circular subarray (with tweaks)