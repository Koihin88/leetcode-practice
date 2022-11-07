class Solution:
    def isValid(self, s: str) -> bool:
        right_match = {
                ")": "(",
                "}": "{",
                "]": "["
                }
        stack = []

        for c in s:
            if c in right_match:
                if stack and stack[-1] == right_match[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
