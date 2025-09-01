"""
return True if both words are anagrams
"""

def solution2(word1, word2):
    return Counter(word1) == Counter(word2)

def is_valid_anagram(word1, word2):
    if len(word1) != len(word2):
        return False

    cArr = [0] * 26

    for c in range(len(s)):
        val1 = ord(word1[c]) - ord('a')
        val2 = ord(word2[c]) - ord('a')
        cArr[val1] += 1
        cArr[val2] -= 1

    for val in cArr:
        if val != 0:
            return False

    return True

if __name__ == "__main__":
    s = "cara"
    t = "arac"
    print(is_valid_anagram(s, t))