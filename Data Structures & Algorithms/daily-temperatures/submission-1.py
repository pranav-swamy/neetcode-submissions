class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # store (elt, index) in a stack
        # start processing element
        # if it is > top of stack, pop the stack and record the value for that idx as the difference in positions
        # keep popping from stack until a higer value is found

        stack = []
        res = [0]*len(temperatures)

        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                # found the next higher temp
                pos = stack[-1][1]
                numDays = i - pos
                res[pos] = numDays
                stack.pop()
            
            stack.append((temperatures[i], i))
        
        return res
