class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s)-1

        while start < end:
            # move start and end to relevant positions
            while start < len(s) and not s[start].isalnum():
                start += 1
            while end >= 0 and not s[end].isalnum():
                end -= 1

            # if all chars are invalid -> start >= len(s) or end < 0, exit
            if start == len(s) or end == -1:
                return True


            # compare
            if s[start].lower() != s[end].lower():
                return False
        
            # move pointers
            start += 1
            end -= 1

        return True
