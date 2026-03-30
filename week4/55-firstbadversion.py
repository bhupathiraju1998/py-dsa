versions = [False, False, False, True, True, True, True]


def returnVersion(n:int)->bool:
    return versions[n]

def firstBadVersion()->int:
    l =0
    r = len(versions) - 1

    while l < r :
        mid = l+((r-l)//2)

        if returnVersion(mid) == False:
            l = mid + 1
        else:
            r = mid 

    return l
print(firstBadVersion())
