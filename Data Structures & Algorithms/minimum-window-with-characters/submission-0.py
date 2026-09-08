#Time comp: O(len(s) + len(t))
#Space comp: O(k) where k is the number of unique characters in t
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        t_map = Counter(t) #Required char frequencies
        s_map = {} #frequencies of required chars in current window
        required = len(t_map) #no. of required unique chars
        formed_count = 0 # no. of unique char requirements currently satisfied

        left = 0
        min_start = 0
        min_len = float('inf')

        for right in range(len(s)):
            right_char = s[right]

            #only track chars required by t
            if right_char in t_map:
                s_map[right_char] = s_map.get(right_char, 0) + 1

                #increase only when exact required freq is reached
                if s_map[right_char] == t_map[right_char]:
                    formed_count += 1
            
            #shrink window while it contains everything required to get min_window
            while formed_count == required:
                current_len = right - left + 1

                if current_len < min_len:
                    min_len = current_len
                    min_start = left
                
                left_char = s[left]

                if left_char in t_map:
                    s_map[left_char] -= 1

                    #this char requirement is no longer satisfied
                    if s_map[left_char] < t_map[left_char]:
                        formed_count -= 1
                left += 1
        if min_len == float('inf'):
            return ""
        return s[min_start: (min_start+min_len)]