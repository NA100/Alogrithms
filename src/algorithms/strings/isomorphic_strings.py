"""
Given two strings s and t, return true if and only if the characters in s can be replaced to get t
with a one-to-one mapping (bijection) between characters of s and t.
 No two different characters in s may map to the same character in t, and each character must map consistently.
Examples
s="egg", t="add" → true
s="foo", t="bar" → false
s="paper", t="title" → true
Notes
Lengths must be equal to be isomorphic.
Mapping is character-to-character; order must be preserved.
"""

def is_isomorphic(str1, str2):
    h1 = {}
    h2 = {}
    if len(str1) != len(str2):
        return false

    for i in range(0, len(str1)):
        h1.put(str[i], str[j])
        h2.put(str[j], str[i])







if __name__ == "__main__":
    result = is_isomorphic("egg", "add")
    print(result)