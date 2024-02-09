# arrays/ encode decode strings
# The challenge of this problem lies in choosing an appropriate separator character for the encode method, as well as ensuring that the decode method is able to correctly identify and split the original strings. Additionally, the solution should be efficient in terms of time and space complexity.
# Desig a algorith that encodes a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
class Solution:
    def encode(self, text: list[str]) -> str:
        separator = '#'
        encoded_str = separator.join(text)
        return encoded_str
    
    def decode(self, text: str) -> list[str]:
        separator = '#'
        return text.split(separator)

codec = Solution()
strs = ["hello", "world"]
encoded_str = codec.encode(strs)
print(encoded_str) 
decoded_str = codec.decode(encoded_str)
print(decoded_str)
