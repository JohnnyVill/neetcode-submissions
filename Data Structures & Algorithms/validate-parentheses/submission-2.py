class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matchMap = {
            "[":"]",
            "(":")",
            "{":"}"
        }
        for i in s:
            if i in "[({":
                stack.append(i)
            elif i in "]})" and stack:
                check = stack.pop()
                if matchMap[check] != i:
                    return False
            else:
                return False
        return True if not stack else False

