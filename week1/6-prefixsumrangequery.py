nums=[3,1,2,10,1]
# range=
l=1 
r=3
current_sum = 0
arr = []
for each in nums:
    current_sum += each
    arr.append(current_sum)
if l == 0:
    print(arr[r])
else:
    print(arr[r]-arr[l-1])
