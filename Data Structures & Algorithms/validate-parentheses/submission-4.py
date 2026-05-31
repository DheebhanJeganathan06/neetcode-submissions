class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            elif (not stack):
                return False
            else:
                if (
                    (c == ')' and stack[-1] == '(')
                    or (c == ']' and stack[-1] == '[')
                    or (c == '}' and stack[-1] == '{')
                ):
                    stack.pop()
                else:
                    return False
        return not stack
            
            
        