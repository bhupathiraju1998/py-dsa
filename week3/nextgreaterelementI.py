nums1 = [4,1,2]
nums2 = [1,3,4,2]
# [-1,3,-1]->o/p


# brute force
nums1Idx = {n:i for i,n in enumerate(nums1)}
res = [-1] * len(nums1)

for i in range(len(nums2)):
    if nums2[i] not in nums1Idx:
        continue
    for j in range(i+1,len(nums2)):
        if nums2[j] > nums2[i]:
            idx = nums1Idx[nums2[i]]
            res[idx] = nums2[j]
            break
print(res)

# o(nusm1.length+nums2.length) usign monotonic stack 
stack = []
res2 = [-1] * len(nums1)
for i in range(len(nums2)):
    cur = nums2[i]
    while stack and cur > stack[-1]:
        val = stack.pop()
        idx = nums1Idx[val]
        res2[idx] = cur 
    if cur in nums1Idx:
        stack.append(cur)
print(res2)

# chatgpt
stack = []
next_greater = {}

for num in nums2:
    while stack and num > stack[-1]:
        next_greater[stack.pop()] = num
    stack.append(num)