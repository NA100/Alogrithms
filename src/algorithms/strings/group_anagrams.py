"""
Problem statement
Given an array of strings strs, group the anagrams together.
Return a list of groups (order of groups and words inside each group does not matter).
Example
Input: ["eat","tea","tan","ate","nat","bat"]
Output: [["eat","tea","ate"],["tan","nat"],["bat"]]

Time complexity = O(n * m)
Space complexity = O(n)
"""

def group_anagrams(list_str):
    result = []
    dict = {}
    for str in list_str:
        key = [0] * 26
        for c in str:
            index = ord(c.lower()) - ord('a')
            print(index)
            key[index] = key[index] + 1
        dict.setdefault(tuple(key), []).append(str)
        #if tuple(key) in dict:
            #dict[tuple(key)].append(str)
        #else:
            #dict[tuple(key)] = [str]
    for v in dict.values():
        result.append(v)
    return result

if __name__ == "__main__":
    list_str = ["Abc", "cba", "ted", "bac"]
    print(group_anagrams(list_str))