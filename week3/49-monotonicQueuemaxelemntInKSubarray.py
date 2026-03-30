# Operations in a Queue
# | Operation | Meaning                       |
# | --------- | ----------------------------- |
# | Enqueue   | Add element to **back**       |
# | Dequeue   | Remove element from **front** |
# enqueue
# queue.append(4)     # [1, 2, 3, 4]
# dequeue we donot pop first and pop any other elmetns it will not work like queue 
# queue.pop(0)

# You can add/remove from both ends
# | Operation         | Code               | Where |
# | ----------------- | ------------------ | ----- |
# | Add to right      | `dq.append(x)`     | Back  |
# | Remove from right | `dq.pop()`         | Back  |
# | Add to left       | `dq.appendleft(x)` | Front |
# | Remove from left  | `dq.popleft()`     | Front |
from collections import deque

dq = deque()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
l = r = 0
result = []

while r < len(nums):
     # 1️⃣ Remove smaller elements from back (monotonic property)
    while dq and nums[dq[-1]] < nums[r]:
        dq.pop()
     # 2️⃣ Add current element index to back
    dq.append(r)

    # 3️⃣ Remove elements outside the window from front
    if dq[0] < l:
        dq.popleft()

    #4️⃣ If window size reached k → record maximum
    if r - l + 1 == k:
        result.append(nums[dq[0]]) # front = max
        l += 1 # shrink window from left

    r+=1


print(result)