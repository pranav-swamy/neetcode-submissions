class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i_map = {}

         # dupes work because they get rewritten

        for i in range(len(nums)):
            i_map[nums[i]] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in i_map:
                if i_map[diff] != i: # works because the val is getting replaced on a dupe number
                    return [i, i_map[diff]]
        return [-1, -1]
