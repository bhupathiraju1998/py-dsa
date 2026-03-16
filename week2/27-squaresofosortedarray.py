nums = [-4,-1,0,3,10]
#op = [0,1,9,16,100]

l = 0
r = len(nums) - 1
res = []

while l <= r:
    lSquare = nums[l]**2
    rSquare = nums[r]**2 

    if lSquare > rSquare:
        res.append(lSquare)
        l += 1
    else:
        res.append(rSquare)
        r -= 1

print(res[::-1])
