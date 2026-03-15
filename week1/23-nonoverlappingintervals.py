intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Greedy Idea (Optimal)
# Sort intervals by end time.
# Always keep the interval that ends earliest.
# If the next interval starts before the previous end, it overlaps → remove it.
# Why this works:
# Choosing the earliest ending interval leaves maximum space for future intervals.
intervals.sort(key=lambda x: x[1])
        
end = intervals[0][1]
remove = 0

for i in range(1, len(intervals)):
    if intervals[i][0] < end:
        remove += 1
    else:
        end = intervals[i][1]
        