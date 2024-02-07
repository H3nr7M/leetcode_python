
# The challenge of this problem lies in choosing an appropriate separator character for the encode method, as well as ensuring that the decode method is able to correctly identify and split the original strings. Additionally, the solution should be efficient in terms of time and space complexity.
# Desig a algorith that encodes a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
class Codec:
    def encode(self, strs):
        res = ''
        for s in strs:
            res += '#' + str(len(s)) + s

        return res

    def decode(self, s):
        res = []
        i = 0
        while i < len(s):
            if s[i] == '#':
                x = int(s[i+1])
                res.append(s[i+2:i+x+2])
                i = i+x+2
            else:
                i += 1
        return res

        
        

codec = Codec()
strs = ["hello", "world"]
encoded_str = codec.encode(strs)
print(encoded_str) 
decoded_str = codec.decode(encoded_str)
print(decoded_str) 