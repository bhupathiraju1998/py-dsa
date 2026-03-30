heights = [2,1,5,6,2,3]


n=len(heights)
max_area = 0

for i in range(n):
    height = heights[i]

    left = i
    while left >= 0 and heights[left] >= heights[i]:
        left -= 1

    right = i
    while right < n  and heights[right] >= height:
        right += 1
    
    width = right -left -1
    area = height * width
    max_area = max(max_area,area)

print(max_area)