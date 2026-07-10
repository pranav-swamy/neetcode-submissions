class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)

        for i in range(len(temperatures)):
            while stack and stack[-1][1] < temperatures[i]:
                prevIdx, prevTemp = stack.pop()
                result[prevIdx] = i - prevIdx
            stack.append((i, temperatures[i]))
        
        return result