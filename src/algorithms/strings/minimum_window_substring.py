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