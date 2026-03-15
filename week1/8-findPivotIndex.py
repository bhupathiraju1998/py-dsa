# find index of elemnt hwose left sum is equal to right sum
arr=[1,7,3,6,5,6]
# o/p = 3

total = sum(arr)
left_sum = 0
for i in range(len(arr)):
    right_sum = total - arr[i] - left_sum
    if left_sum == right_sum:
        print(i) 
    left_sum += arr[i]
    
