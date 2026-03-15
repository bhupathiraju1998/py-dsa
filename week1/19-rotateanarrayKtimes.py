arr = [1,2,3,4,5]
k = 2

k = k % len(arr)


# reverse full array
l,r =0,len(arr)-1
while l < r:
    arr[l],arr[r] = arr[r],arr[l]
    l,r = l+1,r-1

# reverse first portion
l,r =0,k-1
while l < r:
    arr[l],arr[r] = arr[r],arr[l]
    l,r = l+1,r-1

    
# reverse second portion
l,r =k,len(arr)-1
while l < r:
    arr[l],arr[r] = arr[r],arr[l]
    l,r = l+1,r-1
print(arr)