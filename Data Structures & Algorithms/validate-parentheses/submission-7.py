#Time comp: O(n), Space comp: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        char_map = {
            ']': '[',
            ')': '(',
            '}': '{'
        }
        my_stack = []
        for i in range(len(s)):
            if s[i] not in char_map: # if yes -> char is any type of opening bracket -> push
                my_stack.append(s[i])
            else:
                if len(my_stack) != 0 and my_stack[-1] == char_map[s[i]]:
                    my_stack.pop()
                else:
                    return False
        #check if my_stack empty: if yes -> valid string, otherwise not valid
        if len(my_stack) != 0:
            return False
        return True