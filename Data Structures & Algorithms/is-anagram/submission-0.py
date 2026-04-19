class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #edge cases
        if not s or not t:
            return False
        if not s and not t:
            return True
        #create a hashmap for s to store it's values and counts
        s_map = {}
        for char in s:
            if char not in s_map:
                s_map[char] = 1
            else:
                s_map[char] +=1
        # iterate over t and check if all it's chars in s_map or not
        for char in t:
            if char not in s_map:
                return False # if chars of s_map and t are not matching -> not anagram
            else:
                s_map[char] -= 1
        # check s_map if it's still have any char left after iterating over t
        for count in s_map.values():
            if count != 0:
                return False
        return True