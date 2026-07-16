class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # the key idea is
        # for every substring from
        # start+1 to len(s), check if start:end is a palindrome
        # if it is, then add it to path and recurse on end (the next char after the substring)

        soln = []
        path = []

        def is_palindrome(chars):
            return chars == chars[::-1]

        def backtrack(start):
            if start == len(s):
                # found a split of all palindromes
                soln.append(path[:])
                return
            
            for end in range(start+1, len(s)+1):
                if is_palindrome(s[start:end]):
                    path.append(s[start:end])
                    backtrack(end)
                    path.pop()
        
        backtrack(0)
        return soln
