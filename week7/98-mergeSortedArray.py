import heapq

def mergeKArrays(arrays):
    heap = []
    result = []

    # Step 1: push first element of each array
    for i in range(len(arrays)):
        if arrays[i]:
            heapq.heappush(heap, (arrays[i][0], i, 0))  
            # (value, array_index, element_index)

    # Step 2: process heap
    while heap:
        val, i, j = heapq.heappop(heap)
        result.append(val)

        # push next element from same array
        if j + 1 < len(arrays[i]):
            heapq.heappush(heap, (arrays[i][j+1], i, j+1))

    return result

arrays = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]

print(mergeKArrays(arrays))



# | Step | Action | Heap              | Popped | Result            | Next Push |
# | ---- | ------ | ----------------- | ------ | ----------------- | --------- |
# | 0    | init   | (1,A),(2,B),(3,C) | -      | []                | -         |
# | 1    | pop    | (2,B),(3,C)       | 1      | [1]               | push 4    |
# | 2    | pop    | (3,C),(4,A)       | 2      | [1,2]             | push 5    |
# | 3    | pop    | (4,A),(5,B)       | 3      | [1,2,3]           | push 6    |
# | 4    | pop    | (5,B),(6,C)       | 4      | [1,2,3,4]         | push 7    |
# | 5    | pop    | (6,C),(7,A)       | 5      | [1,2,3,4,5]       | push 8    |
# | 6    | pop    | (7,A),(8,B)       | 6      | [1,2,3,4,5,6]     | push 9    |
# | 7    | pop    | (8,B),(9,C)       | 7      | [1,2,3,4,5,6,7]   | -         |
# | 8    | pop    | (9,C)             | 8      | [1,2,3,4,5,6,7,8] | -         |
# | 9    | pop    | empty             | 9      | [1..9]            | -         |
