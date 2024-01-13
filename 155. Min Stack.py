class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minVal = float('inf')
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minVal = min(self.minVal, val)

    def pop(self) -> None:
        self.stack.pop()
        self.minVal = min(self.stack) if self.stack else float('inf')
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minVal
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()