class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # the key idea is
        # for every substring from
        # start+1 to len(s), check if start:end is a palindrome
        # if it is, then add it to path and recurse on end (the next char after the substring)

        soln = []
        cur = []
        def is_palindrome(word):
            return word == word[::-1]

        def backtrack(start):
            if start == len(s):
                soln.append(cur[:])
                return
            
            for end in range(start+1, len(s)+1):
                if is_palindrome(s[start:end]):
                    cur.append(s[start:end])
                    backtrack(end)
                    cur.pop()
        
        backtrack(0)
        return soln

       
