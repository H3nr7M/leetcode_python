'''
Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.
'''
def run_length_encode(s):
    """Encodes a string using run-length encoding"""
    if not s: #if string is empty,
        return ""
    result = []
    count = 1
    for i in range(1, len(s)): 
        if s[i] == s[i-1]:
            count += 1
        else:
            result.append(str(count) + s[i-1])
            count = 1
    result.append(str(count) + s[-1]) #append the last character
    return "".join(result) #join the list of strings into a single string

def run_length_decode(s):
    """Decodes a string that was encoded using run-length encoding"""
    if not s:
        return ""
    result = []
    i = 0
    while i < len(s):
        count = int(s[i])
        result.append(s[i+1] * count)
        i += 2 #increment by 2 because the format is "count + character"
    return "".join(result)

if __name__ == "__main__":
    s = "DAAABBCT"
    encoded = run_length_encode(s)
    print(encoded)
    decoded = run_length_decode(encoded)
    print(decoded)
