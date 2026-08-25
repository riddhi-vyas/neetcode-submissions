#Time comp: O(n), Space comp: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        s_map = {
            '}':'{',
            ']':'[',
            ')':'('
        }
        stack = []
        for i in range(len(s)):
            if s[i] not in s_map: # it must be opening bracket
                stack.append(s[i])
            else: # it is closing bracket
                if stack and stack[-1] == s_map[s[i]]:
                    stack.pop()
                else:
                    return False
        if len(stack) != 0:
            return False
        return True