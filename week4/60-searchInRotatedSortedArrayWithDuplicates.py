# op = true/false 

nums = [2,5,6,0,0,1,2]
target = 0
# print(search(nums, target))  # True

def search(nums,target):
    l = 0
    r =  len(nums) -1 

    while l <= r :
        mid = l + ((r -l)//2)

        if nums[mid] == target:
            return True
        
        if nums[l] == nums[mid] == nums[r]:
            l += 1
            r -= 1

        elif nums[l] <= nums[mid]:
            if nums[l] <= target < nums[mid]:
                r = mid -1 
            else:
                l = mid + 1
        else:
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid -1

    return False 
print(search(nums,target))