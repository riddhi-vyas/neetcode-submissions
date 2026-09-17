class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        start = 0
        char_map = {}
        max_len = 0
        for end in range(n):
            if s[end] not in char_map:
                char_map[s[end]] = end
            else:
                start = max(start, char_map[s[end]]+1)
                char_map[s[end]] = end
            max_len = max(max_len, (end-start+1))
        return max_len