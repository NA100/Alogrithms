"""
A Trie (pronounced “try”, also called a prefix tree) is a tree-like data structure
used to efficiently store and search for strings, especially when many strings share
common prefixes.

Think of it like an index in a dictionary:
- Words are stored character by character along a path in the tree.
- Common prefixes are stored only once, saving space and speeding up lookups.
Prefix Tree (Trie)
- Auto-complete
- Spell checker
- Prefix-based queries
- IP routing
- Word games

3 functions:
- insert(string) - O(L)
- search(string) - O(L)
- startsWith(string) - O(P)
- Space O(N * L)
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.endOfWord = True
        return cur

    def search(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return cur.endOfWord

    def startsWith(self, prefix):
        cur = self.root
        for c in prefix:
            if c not in cur.children[c]:
                return False
            cur = cur.children[c]
        return True

