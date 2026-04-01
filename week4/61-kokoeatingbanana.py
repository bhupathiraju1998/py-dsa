
import math


piles = [3,6,7,11]
l,r = 0 , max(piles)
res = r
h = 8
while l <= r:
    mid = l + ((r-l)//2)

    hours = 0 
    for p in piles:
        hours += math.ceil(p/mid)

        if hours <= h:
            res = min(res,mid)
            r = mid-1
        else:
            l = mid+1
