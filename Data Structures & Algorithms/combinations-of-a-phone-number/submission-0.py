class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        soln = []
        current = []

        if not digits:
            return soln

        def backtrack(start):
            if start == len(digits):
                soln.append(''.join(current[:]))
                return
            
            for char in digits_dict[digits[start]]:
                current.append(char)
                backtrack(start+1)
                current.pop()
        
        backtrack(0)
        return soln