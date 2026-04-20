# logic: Using Stack data structure and hashmap
# while iterating, current val is opening bracket of any type ->push to stack
# if it's not -> check stack[top] to proceed further
class Solution:
    def isValid(self, s: str) -> bool:
        #edge case
        if not s:
            return True
        s_map = {']':'[',
                 '}':'{',
                 ')':'('}
        stack = []
        for item in s:
            if item not in s_map: 
            # it is opening bracket of any type -> push it to stack
                stack.append(item)
            else: # it is closing bracket of any type
                #check if it is matching with stack[top] -> if yes ->pop stack
                                                        #-> else not valid parantheses
                if stack and stack[-1] == s_map[item]:
                    stack.pop()
                else:
                    return False
        # check if stack is empty -> if yes, some brackets still remaind open -> invalid
        if len(stack) != 0:
            return False
        return True
#time comp: O(n), n is len(s)
#space comp: O(n), in worst case, if input s is consisting all opening brackets -> stack end up growing proportional to s