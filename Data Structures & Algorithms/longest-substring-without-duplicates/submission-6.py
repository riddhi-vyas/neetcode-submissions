#Time: O(n), Space: O(min(n, alphabet size)), which is O(n) in the general case.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        s_map = {}
        longest = 0
        start = 0
        for end in range(len(s)):
            if s[end] not in s_map:
                s_map[s[end]] = end
            else:
                start = max(start, s_map[s[end]] + 1) #start = max(start, last_seen+1)
                s_map[s[end]] = end
            longest = max(longest, (end-start+1)) # end-start+1 = length of substring
        return longest