nums = [1,0,0,1,1,1,1,0,1,0]

prefix_sum = 0
max_length = 0
mp={0:-1}
for i in range(len(nums)):
    if nums[i] == 0:
        prefix_sum -= 1
    else:
        prefix_sum += 1

    if prefix_sum in mp:
        length = i - mp[prefix_sum]
        max_length = max(max_length,length)
    else:
        mp[prefix_sum] = i

print(max_length)