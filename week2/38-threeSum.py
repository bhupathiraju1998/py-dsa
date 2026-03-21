nums = [-1,0,1,2,-1,-4]
# Output = [[-1,-1,2], [-1,0,1]]
# no duplicates
# hint:- sort o(nlogn) the existing array and fins three numbers that sum to zero  and in teh sorted array if the iterating elemnt is positive the next elemtns  will not make sum to zero
# hint2:- a,b,c a is fixed for l ,a nd remingi b,c we use 2sum with 2 pointer but r is moved as we need sum to zero


res = []
nums.sort()

for i , a in enumerate(nums):
    if i > 0 and a == nums[i-1]:
        continue #this is written for cases [-x, -x, x,x] whhy to check same number

    l,r = i+1,len(nums)-1
    while l < r:
        three_sum = a + nums[l] + nums[r]
        if three_sum > 0:
            r -= 1
        elif three_sum < 0:
            l += 1
        else:
            res.append([a,nums[l],nums[r]])
            #below code is for conditions liek [-2,-2,0,2,2]
            # if sum becomes zero we need to push the l 
            l += 1
            while nums[l] == nums[l-1] and l < r:
                l += 1
print(res)
