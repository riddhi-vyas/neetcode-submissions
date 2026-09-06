class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        str_map = {}
        for item in strs:
            sorted_item = str(sorted(item))
            if sorted_item not in str_map:
                str_map[sorted_item] = []
            str_map[sorted_item].append(item)
        return list(str_map.values())