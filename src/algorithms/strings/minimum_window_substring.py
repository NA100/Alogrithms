"""
Problem statement:

Given strings s and t, return the smallest substring of s that contains
all characters of t (including multiplicities). If no such substring exists, return "".
Example: s="ADOBECODEBANC", t="ABC" → "BANC".

Intuition (sliding window + need/have counts)
Count what we need from t.

Expand right over s, decrementing need[ch]. When all required chars are
covered (missing == 0), shrink from the left to get the minimal window,
 updating the best answer.
"""

def min_window(str1, str2):
    if len(str1) > len(str2):
        str1, str2 = str2, str1

    m = {}
    m2 = {}
    for c in str1:
        m[c] = m.get(c, 0) + 1

    i = 0
    j = 0
    min_window = str2
    right_window = True

    while j < len(str2):
        print(f"testing string {str2[i:j+1]}")
        if str2[j] in m and right_window:
            c = str2[j]
            m2[c] = m2.get(c, 0) + 1
        print(m2)

        if m == m2 :
            print('match')
            if len(min_window) > len(str2[i:j+1]):
                min_window = str2[i:j+1]
                print('shrinking from left - each')

            if str2[i] in m and i < j:
                m2[str2[i]] = m2.get(str2[i], 1) - 1
                i += 1
            while str2[i] not in m and i < j:
                i += 1
                right_window = False
        else:
            print('increasing from right - each')
            j += 1
            right_window = True

    return min_window


if __name__ == "__main__":
    str1 = "ADOBECODEBANC"
    str2 = "ABC"
    print(min_window(str1, str2))