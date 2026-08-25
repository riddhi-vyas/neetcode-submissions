#Time comp: O(n), Space comp: O(1)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        s_map = {}
        longest = 0
        length = 0
        start = 0
        for end in range(len(s)):
            if s[end] not in s_map:
                s_map[s[end]] = end
                length = (end - start + 1)
            else:
                start = max(start, s_map[s[end]] + 1)
                length = end - start + 1
                s_map[s[end]] = end
            longest = max(longest, (end-start+1))
        return longest