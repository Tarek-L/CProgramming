class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {'{':'}','[':']','(':')'}
        for c in s:
            if c == '{' or c == '[' or c == '(':
                stack.append(c)
            else:
                if not stack:
                    return False
                elif c != m[stack.pop()]:
                    return False
        if not stack:
            return True
        else: return False

        
