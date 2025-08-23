"""
Longest Substring Without Repeating Characters — Problem Statement

Given a string s, return the length of the longest substring (a contiguous block of characters)
 that contains no repeating characters.
Examples
s = "abcabcbb" → 3
Explanation: The answer is "abc", length 3.
s = "bbbbb" → 1
Explanation: The answer is "b".
s = "pwwkew" → 3
Explanation: The answer is "wke".
Note that "pwke" is not a substring (it skips characters), so it doesn’t count.
s = "" → 0
Notes
Characters are case-sensitive ('A' ≠ 'a').
All characters in s are considered (letters, digits, symbols, spaces).
We care about contiguous substrings, not subsequences.
"""

def find_longest_substring(str):
    i, j = 0, 1
    final_max = 0
    l = len(str)
    charset = set(str[i])
    while j < l:
        print(f"{i}, {j}")
        if str[j] not in charset:
            charset.add(str[j])
            print(f"adding {str[j]} to {charset} ")
        else:
            while str[i] != str[j]:
                print(f"removing all chars before dup {str[j]}")
                print(f"removing CHAR {str[i]}")
                charset.remove(str[i])
                i = i + 1
            i = i + 1
            print(f"removing matching char {str[i]}")
        current_max = j - i + 1
        print(f"current_max: {current_max}")
        print(f"{i}, {j}")
        print(f"ending -------\n")
        final_max = max(current_max, final_max)
        j = j + 1
    return final_max

if __name__ == "__main__":
    print("abc {}", find_longest_substring("abcabcbb"))

