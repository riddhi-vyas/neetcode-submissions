#Time comp: O(n), n is length of string
#Space comp: O(k), k is number of unique chars in alphabet (O(26) or O(1))
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        start = 0
        longest = 0
        max_freq = 0
        freq_map = {}
        n = len(s)
        for end in range(n):
            if s[end] not in freq_map:
                freq_map[s[end]] = 1
            else:
                freq_map[s[end]] += 1
            max_freq = max(max_freq, freq_map[s[end]]) #always update max_freq
            # window size = (end-start+1)
            # chars_need_to_change = window_size - max_freq
            if (end-start+1) - max_freq > k:
                #shrink window: 1) decrease freq of start in map 2) increment start by 1
                freq_map[s[start]] -= 1
                start += 1
            longest = max(longest, (end-start+1)) #always update longest at end of each iter
        return longest