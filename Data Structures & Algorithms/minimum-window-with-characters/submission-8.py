from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        t_map = Counter(t)
        s_map = {} # will only store chars present in t_map

        required = len(t_map)
        formed = 0 # Use this instead of helper(containsAll), it will track how many req chars currently have enough freq/copies

        min_len = float('inf')
        best_start = 0 # shortest substring's start pointer (window's start)
        start = 0

        for end in range(len(s)):
            char = s[end]
            #Step1 - Only track chars required by t
            if char in t_map:
                s_map[char] = s_map.get(char, 0) + 1

                #Step2 - Increase formed only when reach required count
                if s_map[char] == t_map[char]:
                    formed += 1
                    
            #Step3 - Check while all required counts are satisfied
            while required == formed:
                window_len = end-start+1
                if window_len < min_len:
                    min_len = window_len
                    best_start = start

                #Shrink window: Remove leftmost char from window
                leftmost = s[start]
                if leftmost in t_map:
                    s_map[leftmost] -= 1
                    #check if this char no longer has enough freq/copies
                    if s_map[leftmost] < t_map[leftmost]:
                        formed -= 1
                #update start at end of each iteration
                start += 1
        if min_len == float('inf'):
            return ""
        return s[best_start:best_start+min_len]