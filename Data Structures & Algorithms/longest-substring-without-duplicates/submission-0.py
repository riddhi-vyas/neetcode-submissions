# Logic - sliding window approach
# Initialize-> start = 0, max_len = 0, char_map = {}, n = len(s)
# Iterate over s using pointer "end" and check if char is already in char_map?
# If char is in dict AND char_map[s[end]] >= start, then update start to char_map[char] + 1
# Else add char to char_map with value = current index(end)
# & update max_len with max(end-start+1, max_len)
# return max_len
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        start = 0
        max_len = 0
        char_map = {}
        n = len(s)
        for end in range(n):
            if s[end] in char_map and char_map[s[end]] >= start:
            # means char is being repeated in given subsrtring -> Update start
                start = char_map[s[end]] + 1
            char_map[s[end]] = end #update map[s[end]] with current val(end)
            max_len = max(end-start+1, max_len)
        return max_len
