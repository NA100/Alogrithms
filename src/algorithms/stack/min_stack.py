"""
Design a stack class that supports the push, pop, top, and getMin operations.

MinStack() initializes the stack object.
- void push(int val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.
Each function should run in O(1) time.

Example 1:

Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]

Output: [null,null,null,null,0,null,2,1]

Explanation:
MinStack minStack = new MinStack();
minStack.push(1);
minStack.push(2);
minStack.push(0);
minStack.getMin(); // return 0
minStack.pop();
minStack.top();    // return 2
minStack.getMin(); // return 1
Constraints:

-2^31 <= val <= 2^31 - 1.
pop, top and getMin will always be called on non-empty stacks.

"""

class stack:
    def __init__(self):
        self.list = []
        self.min_list = []

    def push(self, s):
        self.list.append(s)
        if len(self.min_list) == 0:
            self.min_list.append(s)
        elif self.min_list[-1] > s:
            self.min_list.pop()
            self.min_list.append(s)
        else:
            self.min_list.append(self.min_list[-1])

    def pop(self):
        if len(self.list) == 0:
            return None
        self.min_list.pop()
        return self.list.pop()

    def top(self):
        l = len(self.list)
        if l == 0:
            return None
        return self.list[l-1]

    def get_min(self):
        return self.min_list[-1]

if __name__ == "__main__":
    s = stack()
    s.push(1)
    s.push(4)
    s.push(2)
    s.push(3)
    s.push(-1)
    print(s.get_min())
    s.pop()
    print(s.get_min())


