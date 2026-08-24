#Hashmap storing k:v -> char: freq
#Invariant: two strings should have same chars + with same freq each
# Time comp: O(n+m), where n = size of s, m = size of t, Space comp: O(k), here s_map will only store distinct letters from alphabate (26)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s and not t:
            return True
        if not s or not t:
            return False
        s_map = {} # k:v -> char:freq
        for char in s:
            if char not in s_map:
                s_map[char] = 1
            else:
                s_map[char] += 1
        for char in t:
            if char not in s_map:
                return False
            else:
                s_map[char] -= 1
        for count in s_map.values():
            if count != 0:
                return False
        return True