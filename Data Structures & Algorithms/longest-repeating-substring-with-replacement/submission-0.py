# Logic: Sliding window
# Initialize: n=len(s), start=0, max_freq=0, max_len=0, char_map={}
# Iterate over s using end as index
# If s[index] not in char_map, add to char_map with val=1, else value+1
# Update max_freq by comparing it to current element's freq from char_map
# Now, keep in mind that window_size would be end-start+1 currently
# Also, keep in mind that chars_need_to_change = window_size - max_freq
# Check if chars_need_to_change > k
# If yes, reduce window_size: 1)reduce freq of char at start in char_map by 1
#                             2)update start -> start+1
# Update max_len by comparing it to window_size (because we need to find max_window)
# Return max_len
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        n = len(s)
        start = 0
        max_freq = 0
        max_len = 0
        char_map = {}
        for end in range(n):
            if s[end] not in char_map:
                char_map[s[end]] = 1
            else:
                char_map[s[end]] += 1
            max_freq = max(char_map[s[end]], max_freq) #update max_freq
            # window_size = end-start+1
            # chars_need_to_change = window_size - max_freq
            if (end-start+1) - max_freq > k:
            # reduce window -> decreas s[start] by 1 in char_map & update start by 1
                char_map[s[start]] -= 1
                start += 1
            #update max_len at the end
            max_len = max(end-start+1, max_len)
        return max_len
#time comp: O(n), n is len(s)
#space comp: O(m), m is unique chars in s