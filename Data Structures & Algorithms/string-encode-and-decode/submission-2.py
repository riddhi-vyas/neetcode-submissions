#Time: O(N), Space: O(N), where N is the total number of characters in all strings.
class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        encoded_str = ""
        for item in strs:
            item_len = len(item)
            encoded_str += str(item_len) + "#" + item
        return encoded_str

    # two pointers
    def decode(self, s: str) -> List[str]:
        decoded = []
        if not s:
            return []
        start = 0
        while start < len(s):
            end = start
            while s[end] != "#":
                end += 1
            item_len = int(s[start:end])
            decoded.append(s[end+1:end+1+item_len])
            start = end + 1 + item_len
        return decoded