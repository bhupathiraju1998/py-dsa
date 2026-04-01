def minDays(bloomDay, m, k):
    if m * k > len(bloomDay):
        return -1

    def canMake(day):
        bouquets = 0
        flowers = 0

        for bloom in bloomDay:
            if bloom <= day:
                flowers += 1
                if flowers == k:
                    bouquets += 1
                    flowers = 0
            else:
                flowers = 0

        return bouquets >= m

    low, high = min(bloomDay), max(bloomDay)

    while low < high:
        mid = (low + high) // 2
        if canMake(mid):
            high = mid
        else:
            low = mid + 1

    return low

bloomDay = [1,10,3,10,2]
m = 3
k = 1
print(minDays(bloomDay,m,k))