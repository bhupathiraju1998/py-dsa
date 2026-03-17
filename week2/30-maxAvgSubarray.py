nums = [1,12,-5,-6,50,3]
k = 4


window_sum = sum(nums[:k])
max_sum = window_sum

for i in range(k,len(nums)):
    window_sum += nums[i]
    window_sum -= nums[i-k]
    max_sum = max(max_sum,window_sum)

print(max_sum/k)