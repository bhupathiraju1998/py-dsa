#Two sum arr=[5,2,11,7,15] tar=9

# brute force TC-O(n2) SC-O(1)
nums=[5,2,11,7,15] 
target =9

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if(nums[i]+nums[j] == target):
            print(nums[i],nums[j])

# hashmap2pass - optimal tc-O(n) sc-O(n)
indices={}
for i,n in enumerate(nums):
    indices[n] = i
for i,n in enumerate(nums):
    diff = target - n
    if diff in indices and indices[n] != i:
        print(indices[diff],i)

# hashmap3pass - optimal tc-O(n) sc-O(n)
indices={}
for i,n in enumerate(nums):
    diff = target - n
    if diff in indices:
        print(diff,n)
    indices[n]=i