nums=[3,1,2,10,1]
# o/p = [3,4,6,16,17]

current_sum = 0
result = []

for each in nums:
    current_sum += each
    result.append(current_sum)
print(result)