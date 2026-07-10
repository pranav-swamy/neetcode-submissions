class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # one pass solution
        idx = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in idx: # seeing a val of a different idx for the first time since it is only one loop
                return [idx[diff], i]
            idx[nums[i]] = i # add the idx to the map
        return []