class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}

        for i, num in enumerate(nums):
            idx[num] = i
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in idx and idx[diff] != i: # found the idx with hte correct pair
                return [i, idx[diff]]
        return []