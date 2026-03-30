nums = [1,3,5,6]
target = 5
# op = 1 for 2 and if target is  5 op is 2

l = 0
r = len(nums) -1

while l < r:
    mid = l + ((r-l)//2)

    if nums[mid] == target:
        print(mid)
        break
    elif nums[mid] < target:
        l = mid + 1
    else:
        r = mid
else:
    print(l)

# [0,1] if we donot do l = mid +1 our l point would be only at 0 bcoz of //2 gives the previous index 2.5 is 2,  so l = mid +1
# r = mid -1 and r= mid diff is if we do r = mid -1 and the questions needs to find  out poition and donot want to the before poition 