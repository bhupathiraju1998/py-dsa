# Longest Substring Without Repeating Characters
s = "abcabcbb"
# Output = 3  ("abc")
char_set = set()
l = 0
max_length = 0
for r in range(len(s)):
    while s[r] in char_set:
        char_set.remove(s[l])
        l += 1
    char_set.add(s[r])
    max_length = max(max_length,r-l+1)

print(max_length)