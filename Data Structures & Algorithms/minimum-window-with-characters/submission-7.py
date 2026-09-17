#Time comp: O(n + m) where n = len(s) and m = len(t)
#Space comp: O(k) where k is the number of distinct characters in t
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        t_map = Counter(t)
        s_map = {} # Only characters required by t are stored in s_map

        required = len(t_map)
        formed = 0 # (instead of containsAll helper, use this to track how many distinct required characters currently have enough copies

        min_len = float('inf')
        best_start = 0
        start = 0
        
        for end in range(len(s)):
            char = s[end]

            # Track only characters required by t
            if char in t_map:
                s_map[char] = s_map.get(char, 0) + 1 #update s_map[char]

                # Increase formed only when we JUST reach the required count
                if s_map[char] == t_map[char]:
                    formed += 1
                
            # All required character counts are satisfied
            while required == formed:
                window_len = end-start+1

                if window_len < min_len:
                    min_len = window_len
                    best_start = start

                # Remove the leftmost character
                leftmost = s[start]
                if leftmost in t_map:
                    s_map[leftmost] -= 1
                    # This character no longer has enough copies
                    if s_map[leftmost] < t_map[leftmost]:
                        formed -= 1
                start += 1
        if min_len == float('inf'):
            return ""
        return s[best_start:best_start+min_len]