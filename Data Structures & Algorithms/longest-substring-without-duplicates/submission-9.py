#Time comp: O(n), n is length of string
#Space comp: O(k), k is number of unique characters in sliding window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        start = 0
        longest = 0
        char_map = {}
        for end in range(n):
            if s[end] not in char_map:
                char_map[s[end]] = end
            else:
                start = max(start, char_map[s[end]]+1)
                char_map[s[end]] = end
            longest = max(longest, end-start+1)
        return longest