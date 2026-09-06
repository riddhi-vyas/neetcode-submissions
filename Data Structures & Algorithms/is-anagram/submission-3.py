#Hashmap storing k:v -> char: freq
#Invariant: two strings should have same chars + with same freq each
#Time comp: O(n+m), where n = size of s, m = size of t, Space comp: O(k), here s_map will only store distinct letters from alphabate (26)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s or not t:
            return False
        if not s and not t:
            return True
        s_map = {}
        for ch in s:
            if ch not in s_map:
                s_map[ch] = 1
            else:
                s_map[ch] += 1
        for ch in t:
            if ch not in s_map:
                return False
            else:
                s_map[ch] -= 1
        for count in s_map.values():
            if count != 0:
                return False
        return True