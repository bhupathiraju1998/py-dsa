s = "cbaebabacd"
p = "abc"

indicesP = {}
indicesS={}

for i in range(len(p)):
    indicesP[p[i]] = indicesP.get(p[i],0) + 1
    indicesS[s[i]] = indicesS.get(s[i],0) + 1
    

res = [0] if indicesP == indicesS else []
l = 0
for r in range(len(p),len(s)):
    indicesS[s[r]] = indicesS.get(s[r],0) + 1
    indicesS[s[l]] -= 1
    
    if indicesS[s[l]] == 0:
        indicesS.pop(s[l])

    l += 1
    if indicesP == indicesS:
        res.append(l)

print(res)

