arr = [4, 8, 5, 2, 25]

n = len(arr)
stack = []
res = [-1] * n

for i in range(n-1,-1,-1):
    
    while stack and stack[-1] >= arr[i]:
        stack.pop()
    
    if stack:
        res[i] = stack[-1]

    stack.append(arr[i])
print(res)
# Keep removing bigger elements from stack until a smaller one is found
# we pop because we maintin the existing small and the current elemnt i in stack 