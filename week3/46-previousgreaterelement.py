arr = [10, 4, 2, 20, 40, 12, 30]

# o/p = [-1, 10, 4, -1, -1, 40, 40]
n = len(arr)
res = [-1] * n
stack = []

for i in range(n):
    while stack and arr[i] >= stack[-1]:
        stack.pop()
    if stack:
        res[i] = stack[-1]

    stack.append(arr[i])
print(res)