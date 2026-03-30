
# [12, -1, -7] → first negative = -1
# [-1, -7, 8] → first negative = -1
# [-7, 8, -15] → first negative = -7
# [8, -15, 30] → first negative = -15
# Output: [-1, -1, -7, -15]
# 2️⃣ What we need to check for each step

# Imagine sliding the window one by one:

# Add any new negative numbers in the current window to a list (deque).
# We need to know which numbers are negative and their positions.
# Remove numbers that are no longer in the window.
# If a negative number’s index is out of the current window, it cannot be the first negative anymore.
# Report the first negative number in the current window.
# If there’s no negative number in the window, report 0.
# 3️⃣ Why use a deque
# Deque will store indices of negative numbers in order of their appearance.
# Front of deque (dq[0]) → always the first negative in the current window.
# When the window moves, we remove indices that leave the window from the front.
from collections import deque
arr = [12, -1, -7, 8, -15, 30]
k = 3
dq = deque()      # stores indices of negative numbers
result = []       # stores first negative of each window

for i in range(len(arr)):

    # 1️⃣ Add new negative numbers
    if arr[i] < 0:
        dq.append(i)
    
    # 2️⃣ Remove numbers out of the current window
    if dq and dq[0] <= i - k:
        dq.popleft()
    
    # 3️⃣ Record result for current window (once we have first full window)
    if i >= k - 1:
        result.append(arr[dq[0]] if dq else 0)

print(result)

# | i | arr[i] | Window indices | dq (indices of negatives)    | First negative |
# | - | ------ | -------------- | ---------------------------- | -------------- |
# | 0 | 12     | [0]            | []                           | -              |
# | 1 | -1     | [0,1]          | [1]                          | -              |
# | 2 | -7     | [0,1,2]        | [1,2]                        | -1             |
# | 3 | 8      | [1,2,3]        | [1,2]                        | -1             |
# | 4 | -15    | [2,3,4]        | [1,2,4] → remove 1 ✅ → [2,4] | -7             |
# | 5 | 30     | [3,4,5]        | [2,4] → remove 2 ✅ → [4]     | -15            |
