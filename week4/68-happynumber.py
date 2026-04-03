def isHappy(n:int)->int:
    visit = set()

    while n not in visit:
        visit.add(n)
        n = sumOfSquares(n)
        if n == 1:
            return True
    return False 

def sumOfSquares(n:int)->int:
    output = 0
    while n:
        digit = n % 10
        digit = digit ** 2
        output += digit
        n = n // 10 
    return output
print(isHappy(19))