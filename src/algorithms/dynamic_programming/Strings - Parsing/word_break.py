"""
Problem
Given:
s: a string
wordDict: list of valid words
Return: True if s can be segmented into one or more words from wordDict.
"""

def word_break(s, wordDict):
    word_set = set(wordDict)  # faster lookup
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True  # base case

    for i in range(1, n + 1):  # end index of substring
        for word in word_set:
            if len(word) <= i and dp[i - len(word)] and s[i - len(word):i] == word:
                dp[i] = True
                break  # no need to check more words once True

    return dp[n]


def main():
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(word_break(s, wordDict))  # Expected: True

    s = "applepenapple"
    wordDict = ["apple", "pen"]
    print(word_break(s, wordDict))  # Expected: True

    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print(word_break(s, wordDict))  # Expected: False


if __name__ == "__main__":
    main()
