def merge_intervals(intervals):
    if not intervals:
        return []

    # Step 1: Sort intervals based on the start time
    intervals.sort(key=lambda x: x[0])

    # Step 2: Initialize merged list with the first interval
    merged = [intervals[0]]

    # Step 3: Iterate through intervals and merge if necessary
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:  # Overlapping intervals
            last[1] = max(last[1], current[1])  # Merge
        else:
            merged.append(current)

    return merged


# Example usage:
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals))