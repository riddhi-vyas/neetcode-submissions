class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #edge case
        if not s or not t:
            return False
        if not s and not t:
            return True
        s_map = {}
        for char in s:
            if char not in s_map:
                s_map[char] = 1
            else:
                s_map[char] += 1
        for char in t:
            if char not in s_map:
                return False
            elif char in s_map:
                s_map[char] -= 1
        for count in s_map.values():
            if count != 0:
                return False
        return True