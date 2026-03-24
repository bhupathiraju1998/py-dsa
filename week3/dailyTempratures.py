temperatures = [73,74,75,71,69,72,76,73]
# return [1,1,4,2,1,1,0,0] how many days each temp is a dayily temp



res = [0] * len(temperatures)
stack = []

for i in range(len(temperatures)):
    while stack and temperatures[i] > temperatures[stack[-1]]:
        prev_index = stack.pop()  # Pop ONCE, store it
        res[prev_index] = i - prev_index  # Use stored index
    stack.append(i)   
print(res)