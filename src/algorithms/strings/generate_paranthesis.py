"""
Given n pairs of parentheses, write a function to generate all combinations
of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]

"""

def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    stack = []
    res = []

    def generate(open, closed):
        if open == n and closed == n:
            print("adding to res", "".join(stack))
            res.append("".join(stack))

        if open < n:
            print("appending (", open, closed)
            stack.append("(")
            generate(open + 1, closed)
            stack.pop()

        if open > closed:
            print("appending )", open, closed)
            stack.append(")")
            generate(open, closed + 1)
            stack.pop()

    generate(0, 0)
    return res





if __name__ == "__main__":
    print(generateParenthesis(3))