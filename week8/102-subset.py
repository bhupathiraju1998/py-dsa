# If a problem says:

# “Find all possible…”
# “Try every combination…”
# “Check all arrangements…”

# 👉 That’s a strong hint you should think of backtracking.
def subsets(nums):
    res = []
    
    def backtrack(start, path):
        res.append(path[:])
        
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    
    backtrack(0, [])
    return res