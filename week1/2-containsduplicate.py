nums=[1,2,3,3]

#bruteforce tc - O(N2) spc-O(n)
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if(nums[i] == nums[j]):
            print(True)

# optimal solution TC-O(N) SC-O(N)
s=set()
for num in nums:
    if num in s:
        print('contains duplicate')
    else:
        s.add(num)
