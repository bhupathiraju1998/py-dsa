import heapq
# “Top 10 trending posts”,crypto terending by percentage etc
class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = nums
        
        # Convert list into a heap
        heapq.heapify(self.heap) #only root is samllest
        
        # Keep only k largest elements
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # If heap has less than k elements, just push
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            # If new value is bigger than smallest (heap[0])
            if val > self.heap[0]:
                heapq.heapreplace(self.heap, val)
        
        # Top of heap is kth largest
        return self.heap[0]


# Example usage (same as LeetCode test)
kthLargest = KthLargest(3, [4, 5, 8, 2])
print(kthLargest.add(3))   # 4
print(kthLargest.add(5))   # 5
print(kthLargest.add(10))  # 5
print(kthLargest.add(9))   # 8
print(kthLargest.add(4))   # 8