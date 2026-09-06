#Time: O(N), Space: O(N), where N is the total number of characters in all strings.
class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        encoded_string = ""
        for item in strs:
            item_len = len(item)
            encoded_string = encoded_string + str(item_len) + '#' + item
        return encoded_string

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        start = 0
        decoded = []
        while start < len(s):
            end = start
            while s[end] != '#':
                end += 1
            item_len = int(s[start:end])
            decoded.append(s[end+1:end+item_len+1])
            start = end + item_len + 1
        return decoded