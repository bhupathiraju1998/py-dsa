arr=[0,0,1,1,1,1,2,2,2,3,4,4,5]
# op = [0,1,2,3,4,5,_,_,_,_,_,_,_.......] 

l = 0
for r in range(1,len(arr)):
    if arr[r-1] != arr[r]:
        arr[l]=arr[r]
        l += 1
print(arr)