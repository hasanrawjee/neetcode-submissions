class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {')': '(', ']': '[', '}': '{'}
        stack = []

        for c in s:
            if c in bracketMap:
                if stack and stack[-1] == bracketMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
