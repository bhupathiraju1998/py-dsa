# increment(3, 10)
# Result:
# Bottom 3 elements → 1, 2, 3
# Add +10 to each
# [11, 12, 13, 4, 5]
class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.inc = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
            self.inc.append(0)

    def pop(self) -> int:
        if not self.stack:
            return -1
        
        i = len(self.stack) - 1
        if i > 0:
            self.inc[i - 1] += self.inc[i]
        
        val = self.stack.pop() + self.inc.pop()
        return val

    def increment(self, k: int, val: int) -> None:
        if self.stack:
            i = min(k, len(self.stack)) - 1
            self.inc[i] += val