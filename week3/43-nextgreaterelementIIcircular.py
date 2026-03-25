nums = [4,1,2]
n=len(nums)
stack=[]
result=[-1] * n 
for i in range(2*n):
    while stack and nums[i % n] > nums[stack[-1]]:
        result[stack.pop()] = nums[i % n]
    stack.append(i % n)
print(result)