# Hashmap: k:v -> sorted_string_chars: original_string
#Time comp: O(N*MlogM), N it strs size and M is item size for max item in strs, Space comp: O(N*M)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        strs_map = {}
        for item in strs:
            item_sorted = str(sorted(item))
            if item_sorted not in strs_map:
                strs_map[item_sorted] = []
            strs_map[item_sorted].append(item)
        return list(strs_map.values())