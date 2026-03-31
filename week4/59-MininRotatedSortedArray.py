nums = [5,7,8,12,15,20,-7,-4,0,2]


l = 0
r = len(nums) - 1

while(l < r):
    mid = l + ((r-l)//2)

    if(nums[mid] > nums[r]):
        l = mid + 1
    else:
        r = mid 

print(l)