from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        t_map = Counter(t)
        s_map = {} #it will store only chars req by t

        required = len(t_map)
        formed = 0

        min_len = float('inf')
        best_start = 0
        start = 0

        for end in range(len(s)):
            char = s[end]
            #Step1 - Track only chars present in t
            if char in t_map:
                s_map[char] = s_map.get(char, 0) + 1 #update s_map if char in t
                #Step2 - Increase formed if char freq is same as t_map
                if s_map[char] == t_map[char]:
                    formed += 1
                #Step3 - if all chars in s_map are satisfied -> find min window
                while formed == required:
                    #Step a - get the length of current substring
                    window_len = end - start + 1
                    #Step b - update (min_len, best_start) if window_len is smaller
                    if window_len < min_len:
                        min_len = window_len
                        best_start = start
                        
                    #shrink the window
                    #step c - update start ptr, s_map to check for next substring
                    leftmost = s[start]
                    if leftmost in t_map:
                        s_map[leftmost] -= 1
                        #step d - after updating s_map, check if formed still equals required
                        if s_map[leftmost] < t_map[leftmost]:
                            formed -= 1
                    #update start after each iteration
                    start += 1
        # Handle cases where no valid window exists
        if min_len == float('inf'):
            return ""
        return s[best_start:best_start+min_len]