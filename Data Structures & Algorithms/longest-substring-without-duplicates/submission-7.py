#Time: O(n), Space: O(min(n, alphabet size)), which is O(n) in the general case.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        start = 0
        longest = 0
        char_map = {}
        for end in range(len(s)):
            if s[end] not in char_map:
                char_map[s[end]] = end
            else:
                start = max(start, char_map[s[end]]+1) #start = max(start, last_seen+1)
                char_map[s[end]] = end
            #update longest always
            longest = max(longest, (end-start+1))  #end-start+1 = length of substring
        return longest