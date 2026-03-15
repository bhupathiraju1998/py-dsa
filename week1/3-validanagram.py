s='rat'
t='cat'

indiceOne = {}
indiceTwo = {}

for each in s:
    indiceOne[each] = indiceOne.get(each,0) + 1
for each in t:
    indiceTwo[each] = indiceTwo.get(each,0) + 1

print(indiceTwo == indiceOne)