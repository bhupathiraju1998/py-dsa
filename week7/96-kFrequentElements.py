# “Trending hashtags”
# “Most used keywords today
from collections import Counter
import heapq

def topKFrequent(nums, k):
    freq = Counter(nums)
    # freq = {}
    # for x in nums:
    # freq[x] = freq.get(x, 0) + 1

    heap = []

    for num, count in freq.items():
        heapq.heappush(heap, (count, num))  # min-heap by frequency

        if len(heap) > k:
            heapq.heappop(heap)  # remove smallest frequency

    return [num for count, num in heap]



def topKFrequent(words, k):
    freq = Counter(words)

    heap = []

    for word, count in freq.items():
        # use negative frequency for max-heap behavior
        # word stays positive for lexicographical tie-breaking
        heapq.heappush(heap, (-count, word))

    result = []

    for _ in range(k):
        result.append(heapq.heappop(heap)[1])

    return result
# words = ["i","love","leetcode","i","love","coding"]
# k = 2

# In heap tuples:
# (-count, word)

# Python compares:
# first element → frequency
# if tie → second element → word