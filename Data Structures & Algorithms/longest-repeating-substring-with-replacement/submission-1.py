#Time comp: O(n), Space comp: O(m), where m is count of distinct chars in map
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
            max_freq = max(max_freq, freq_map[s[end]])
            # chars_need_to_change = window_size - max_freq
            if (end - start + 1) - max_freq > k:
                #shrink window: 1) decrease freq of start, 2) update start by 1
                freq_map[s[start]] -= 1
                start += 1
            #always update longest_len at the end
            longest = max(longest, end-start+1)
        return longest