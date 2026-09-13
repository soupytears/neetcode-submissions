class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in '({[':
                stack.append(c)
            # if closing bracket but nothing to match it
            elif not stack:
                return False
            elif (ord(stack[-1]) - ord(c) == -2 or
                    ord(stack[-1]) - ord(c) == -1): 
                stack.pop()
            else:
                return False
        return not stack
