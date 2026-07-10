class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # start of a sequence is if num-1 does not exist in the arr
        # put all values in a set for O(1) lookups

        if not nums:
            return 0

        seen = set()

        for num in nums:
            seen.add(num)

        max_seq_len = 1
        for num in nums:
            if num-1 not in seen: # then this num could be a start of the seq
                length = 1
                cur_num = num+1
                while cur_num in seen:
                    length += 1
                    cur_num += 1
                max_seq_len = max(max_seq_len, length)
        
        return max_seq_len
