from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        t_map = Counter(t)
        s_map = {} # it will store only chars req by t_map
        
        required = len(t_map)
        formed = 0 # instead of helper containsAll(), use this variable to track whether we have all the character copies required by t_map

        start = 0
        best_start = 0
        min_len = float('inf')

        for end in range(len(s)):
            char = s[end]

            #Step 1 - Only track chars present in t_map
            if char in t_map:
                s_map[char] = s_map.get(char, 0) + 1
                #Step2 - Increase formed when reach req count for char
                if s_map[char] == t_map[char]:
                    formed += 1
            
            #Step3 - Check if all req counts are satisfied
            while required == formed:
                window_len = end-start+1
                if window_len < min_len:
                    min_len = window_len
                    best_start = start
                # Shrink the window to get next min window -> remove leftmost or START
                leftmost = s[start]
                if leftmost in t_map:
                    s_map[leftmost] -= 1
                    #if this leftmost no longer has enough copies, decrease formed
                    if s_map[leftmost] < t_map[leftmost]:
                        formed -= 1
                start += 1 # update start after each iteration
        if min_len == float('inf'):
            return ""
        return s[best_start:best_start+min_len]