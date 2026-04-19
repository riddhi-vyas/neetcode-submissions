##Encode Logic:
# Initialize a result string and Iterate over strs
# For each item in strs, we'll find length of it (convert into str) & append it to result
# Then append any delimiter you want, I am taking #
# Then append the item string to result
## Decode Logic:
# Initialize a decoded_result list and a pointer i = 0
# While i < len(s): assign i value to second pointer j
# While s[j] character is not "#", increment j by 1
# Now, once it reaches #, it will stop and you'll get length int = int(s[i:j])
# Now, you got the length of word, so simply append s[j+1:j+1+length] to decoded_result
# Note: we have taken j+1 above step because at j, we have #
# Increment i pointer where the first word ends using j+1+length
# Return decoded_result

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