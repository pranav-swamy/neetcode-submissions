class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        elts = set()
        for num in nums:
            if num in elts:
                return True
            else:
                elts.add(num)
        return False