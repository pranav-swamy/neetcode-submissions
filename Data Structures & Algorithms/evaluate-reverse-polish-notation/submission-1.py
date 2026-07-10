class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for ch in tokens:
            if ch == '+':
                stack.append(stack.pop() + stack.pop())
            elif ch == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif ch == '*':
                stack.append(stack.pop() * stack.pop())
            elif ch == '/':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b))
            else:
                stack.append(int(ch))
                print(stack)
        
        #print((6 / -132))
        return stack[-1]

        
                
