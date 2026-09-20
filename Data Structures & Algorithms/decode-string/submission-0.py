# 1. Use a stack to handle nesting. Track a current string and repeat count. When you see [, save both(curr_str, repeat_count) on the stack, then reset them to start decoding the inside.
# 2. When you see ], the inside is complete. Pop the saved string and count, then combine: saved string + current string repeated saved count times. Letters build the current string; digits build the repeat count.
#Time comp: O(n), where n is the length of the input string. Each character is processed a constant number of times (digits build the repeat count, brackets push/pop from the stack, and letters are appended).
#Space comp: O(m), where m is the maximum depth of nested brackets. 
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_str = ""
        repeat_count = 0
        for ch in s:
            if ch.isdigit():
                # Build multi-digit counts: "12" becomes 12
                repeat_count = repeat_count * 10 + int(ch)
            elif ch == '[':
                # Save the string before this bracket and its repeat count
                stack.append((current_str, repeat_count))
                # Start decoding inside the brackets -> Reset string, repeat_count
                current_str = ""
                repeat_count = 0
            elif ch == ']':
                previous_str, count = stack.pop()
                # Combine the earlier string with the decoded repetition
                current_str = previous_str + current_str * count
            else:
                current_str += ch
        return current_str