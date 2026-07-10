class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two ptr approach
        start = 0
        end = len(numbers)-1

        sum_ = numbers[start] + numbers[end]
        while start <= end:
            if sum_ > target:
                end -= 1
            elif sum_ < target:
                start += 1
            else:
                return [start+1, end+1]
            sum_ = numbers[start] + numbers[end]
        
        return [-1, -1]


