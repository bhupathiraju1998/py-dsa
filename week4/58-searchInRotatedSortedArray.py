nums= [ 4,5,6,7,0,1,2]
target = 0
# op = 4

def binarySearch(nums,target,l,r):
    
    if(l > r):
        return -1
    
    mid = l + ((r-l)//2)
    if nums[mid] == target:
        return mid 
    
    if nums[mid] >= nums[l]:
        if(nums[l] <= target and nums[r] >= target):
            return binarySearch(nums,target,l,mid-1)
        else:
            return binarySearch(nums,target,mid+1,r)
    else:
        if(nums[mid] <= target and target <= nums[r]):
            return binarySearch(nums,target,mid+1,r)
        else:
            return binarySearch(nums,target,l,mid-1)

    

    
l = 0
r = len(nums)-1
print(binarySearch(nums,target,l,r))