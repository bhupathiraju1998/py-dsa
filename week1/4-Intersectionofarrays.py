nums1=[1,2,2,1,2]
nums2=[2,2,2,2,1,3]

indices={}

for each in nums1:
    indices[each] = indices.get(each,0) + 1

for each in nums2:
    if each in indices and indices[each] > 0  :
        print(each)
        indices[each] -= 1