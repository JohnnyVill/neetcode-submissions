class Solution:
    def isValid(self, s: str) -> bool:
        """
        Approach:
        Create a stack that will keep track of all open parentheses, whenever a closed parenthesis
        shows remove the top item from that and check if it is valid if is not return false. If the loop
        is complete and the stack is empty return true
        """
        stack = []
        matching = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for i in s:
            if i not in matching:
                stack.append(i)
            else:
                if stack and stack[-1] == matching[i]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        return False

        