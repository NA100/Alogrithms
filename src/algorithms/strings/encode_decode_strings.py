"""
Design an algorithm to encode a list of strings to a single string.
The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
"""

def encode(str_l):
    result = ""
    for s in str_l:
        prefix = str(len(s)) + "#" + s
        result += prefix
    return result

def decode(str):
    result = []
    i = 0
    while i < len(str):
        j = i
        while str[j] != '#':
            j += 1
        length = int(str[i:j])
        result.append(str[j+1 : j+1+length])
        i = j + 1 + length
    return result

if __name__ == "__main__":
    str_l = ["we","say",":","yes"]
    value  = encode(str_l)
    print(f"encoded value is {value}")
    print(f"decoded value is {decode(value)}")

