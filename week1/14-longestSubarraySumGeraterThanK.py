arr = [1, -2, 3, 4, -1, 2, 1]
k = 5
n = len(arr)
max_len = 0
for i in range(n):
    curr_sum = 0
    for j in range(i,n):
        curr_sum += arr[j]
        if curr_sum > k:
            max_len = max(max_len, j-i+1)
print(max_len) #TC-O(n2)


# this below works for positive array only sliding window
arr2 = [1, 2, 3, 4, 1, 2, 1]
left = curr_sum = max_l = 0
for right in range(len(arr2)):
    curr_sum += arr2[right]

    while curr_sum > k:
        max_l = max(max_l,right-left+1)
        curr_sum -= arr2[left]
        left+=1
print(max_l)
