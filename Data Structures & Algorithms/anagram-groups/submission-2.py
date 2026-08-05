class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[]]
        str_map = {}
        for word in strs:
            word_sorted = str(sorted(word))
            if word_sorted not in str_map:
                str_map[word_sorted] = []
            str_map[word_sorted].append(word)
        return list(str_map.values())