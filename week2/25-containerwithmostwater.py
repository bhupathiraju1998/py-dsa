nums=[1,8,6,2,5,4,8,3,7]
result = 0
# brute force
# for l in range(len(nums)):
#     for r in range(1,len(nums)):
#         area = (r-l)*max(r,l)  #width * height
#         result = max(result,area)

l = 0
r = len(nums)-1

while l < r:
    area = (r-l) * min(nums[r],nums[l])
    result = max(result,area)

    if nums[l] < nums[r]:
        l += 1
    elif nums[l] > nums[r]:
        r -= 1
    else:
        l += 1 #update l or r if both nums[l] and nums[r] are of saem height
print(result)