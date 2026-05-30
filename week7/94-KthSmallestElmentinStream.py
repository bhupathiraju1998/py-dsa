import heapq
# In Python, you don’t actually have a built-in max-heap.
class KthSmallest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        # Use negative values to simulate max heap
        self.heap = [-n for n in nums]
        
        heapq.heapify(self.heap)
        
        # Keep only k smallest elements
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # Push negative value
        heapq.heappush(self.heap, -val)
        
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        # Return k-th smallest (convert back to positive)
        return -self.heap[0]


# Example usage
kthSmallest = KthSmallest(3, [4, 5, 8, 2])

print(kthSmallest.add(3))   # 4
print(kthSmallest.add(5))   # 4
print(kthSmallest.add(1))   # 3
print(kthSmallest.add(0))   # 2