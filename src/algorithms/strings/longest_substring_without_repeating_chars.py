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
Explanation: The answer is "wke". Note that "pwke" is not a substring (it skips characters), so it doesn’t count.
s = "" → 0
Notes
Characters are case-sensitive ('A' ≠ 'a').
All characters in s are considered (letters, digits, symbols, spaces).
We care about contiguous substrings, not subsequences.
"""