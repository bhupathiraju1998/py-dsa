prices= [100, 80, 60, 70, 60, 75, 85]
# Span:   [ 1,   1,  1,  2,  1,  4,  6]
# For each day, count how many consecutive days before it (including today) had price ≤ today’s price
# https://www.youtube.com/watch?v=jgEF8Dod5KE
n = len(prices)
# brute force:
res = [1] * n
for i in range(n-1,-1,-1):
    for j in range(i-1, -1 , -1):
        if prices[i] > prices[j]:
            res[i] += 1
        else:
            continue
print(res)

stack = []  # stores indices
span = [0] * len(prices)

for i in range(len(prices)):
    # remove smaller or equal elements
    while stack and prices[i] >= prices[stack[-1]]:
        stack.pop() #we pop as the we check and pop all smaller value until we find the grter value than i

    if not stack:
        span[i] = i + 1
    else:
        span[i] = i - stack[-1] # we subtract the index to get the no of days

    stack.append(i)

