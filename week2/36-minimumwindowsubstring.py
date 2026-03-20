s="ADOBECODEBANC"
t="ABC"
# o/p="BANC" minimum window in s which will contains all the characters

indices,countT = {},{}

res = [-1 , -1]
minLenWind = float("infinity")
l = 0

for each in t:
    countT[each] = 1 + countT.get(each,0)
haveChar , needChar = 0 , len(countT)

for r in range(len(s)):
    eachChar = s[r]

    indices[eachChar] = indices.get(eachChar,0)+1

    if eachChar in countT and  indices[eachChar] == countT[eachChar]:
        haveChar += 1

    while haveChar == needChar:
        if(r-l+1)< minLenWind:
            res = [l,r]
            minLenWind = (r-l+1)
        
        # 👉 Your current window already contains all required characters
        # 👉 But it might be bigger than necessary
        indices[s[l]] -= 1

        # Case 1: Removing extra character (safe)
        # Case 2: Removing required character (danger)
        if s[l] in countT and indices[s[l]] < countT[s[l]]:
            haveChar -= 1
        l += 1
print(res)


