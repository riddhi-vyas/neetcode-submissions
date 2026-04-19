class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #edge case
        if not strs:
            return [[]]
        str_map = {} #dict to store string_sorted as key, anagram list as values
        for word in strs:
            word_sorted = str(sorted(word))
            if word_sorted not in str_map:
                str_map[word_sorted] = []
            str_map[word_sorted].append(word)
        return list(str_map.values())

# time comp: O(m*nlogn)
# space comp: O(m*n)