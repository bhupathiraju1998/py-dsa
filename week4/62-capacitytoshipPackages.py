arr = [3,2,2,4,1,4]
targetDays  = 3

l = max(arr)
r = sum(arr)

while l < r:
    mid= l + ((r-l)//2)

    days = 1
    curr_sum = 0
    for eachWeight in arr:
        if curr_sum + eachWeight > mid:
            days += 1
            curr_sum = 0
        curr_sum += eachWeight

    if days > targetDays:
        l = mid + 1
    else:
        r = mid
print(l)


# For each mid:

# You simulate how many days it would take.

# If it takes too many days (days > targetDays), capacity is too small → move right:

# l = mid + 1

# Otherwise, capacity works → try smaller:

# r = mid
# ⚖️ The invariant

# At every step:

# All values < l are invalid (too small)
# All values ≥ r are valid (work)

# So you are shrinking the search space toward the first valid capacity.

# 🧠 Why l is the answer

# The loop stops when:

# l == r

# At that point:

# l is the smallest value that works
# r is also the same value

# So:

# print(l)

# returns the minimum valid capacity

# 💡 Intuition (very important)

# You are finding:

# “the first capacity where shipping in ≤ targetDays becomes possible”

# This is a lower bound search, and in such patterns:

# l always converges to the answer