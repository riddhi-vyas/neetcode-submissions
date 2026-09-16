class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #edge case
        if not strs:
            return []
        anagram = {}
        for item in strs:
            sorted_item = str(sorted(item))
            if sorted_item not in anagram:
                anagram[sorted_item] = []
            anagram[sorted_item].append(item)
        return list(anagram.values())