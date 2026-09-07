#Time comp: O(n), n is length of string
#Space comp: O(k), where k = 26 (total alphabet chars)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        n = len(s)
        start = 0
        max_freq = 0
        longest = 0
        freq_map = {}
        for end in range(n):
            if s[end] not in freq_map:
                freq_map[s[end]] = 1
            else:
                freq_map[s[end]] += 1
            max_freq = max(max_freq, freq_map[s[end]]) # always update after map changes
            # window_size = end - start + 1
            # chars_need_to_change = window_size - max_freq
            if (end-start+1) - max_freq > k:
                # we need to shrink the window: 1) decrease map[start] 2) update start ptr
                freq_map[s[start]] -= 1
                start += 1
            longest = max(longest, (end-start+1)) # always update longest at end of each iter
        return longest