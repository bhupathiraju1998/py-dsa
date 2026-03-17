arr =  [2,0,2,1,1,0]
# Output : [0,0,1,1,2,2]


counts = [0,0,0]

for each in arr:
    counts[each] += 1

R,W,B = counts
nums = []
nums[:R] = [0] * R
nums[R:R+W] = [1] * W   
nums[R+W:] = [2] * B