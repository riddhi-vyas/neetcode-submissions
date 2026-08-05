class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            w_len = str(len(word))
            result = result + w_len + "#" + word
        return result

    def decode(self, s: str) -> List[str]:
        res_list = []
        start = 0
        while start < len(s):
            end = start
            while s[end] != "#":
                end += 1
            word_len = int(s[start:end])
            res_list.append(s[end+1:end+1+word_len])
            start = end + 1 + word_len
        return res_list
