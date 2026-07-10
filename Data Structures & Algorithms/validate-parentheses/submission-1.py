class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch in ('(', '{', '['):
                stack.append(ch)
            elif ch == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif ch == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            elif ch == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0