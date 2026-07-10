class MinStack:

    # keep track of min so far

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        minvalue = val
        if self.stack:
            minvalue = min(val, self.stack[-1][1])
        self.stack.append((val, minvalue))
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        else:
            return -1
        

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        else:
            return -1
        
