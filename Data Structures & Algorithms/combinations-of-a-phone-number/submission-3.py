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
        cur = []
        if not digits:
            return soln

        def backtrack(digit_index):
            if digit_index == len(digits):
                soln.append(''.join(cur))
                return
            for ch in digits_dict[digits[digit_index]]:
                cur.append(ch)
                backtrack(digit_index+1)
                cur.pop()
        
        backtrack(0)
        return soln
