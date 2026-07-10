class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)

        max_len = 0
        for num in nums:
            if num-1 in numset: # num is the middle of a sequence, so skip
                continue
            else: # num is the start of a sequence, count and keep track of max_len
                current_num = num
                current_len = 1
                while current_num + 1 in numset:
                    current_len += 1
                    current_num += 1
                
                max_len = max(max_len, current_len)
        return max_len


