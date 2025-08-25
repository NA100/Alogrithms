# python_basics.py

# ==== 1. Lists ====
# ==== 0. Empty Array Initialization ====

empty_list = []                    # Empty list
empty_2d = [[0] * n for _ in range(m)]  # m x n grid of zeros
zeros = [0] * 5                    # List of 5 zeros
inf_array = [float('inf')] * 10    # 10 elements of infinity

arr = [1, 2, 3]
arr.append(4)
arr.pop()             # Removes last element
arr.insert(1, 99)     # Insert at index 1
arr.remove(2)         # Removes first occurrence of 2
arr.sort()            # In-place sort
print("List:", arr)

# ==== 2. Tuples ====
t = (1, 2)
x, y = t              # Tuple unpacking
print("Tuple:", x, y)

# ==== 3. Sets ====
s = set()
s.add(1)
s.update([2, 3])
s.discard(2)
print("Set:", s, 1 in s)

# ==== 4. Dictionaries ====
d = {'a': 1, 'b': 2}
d['c'] = 3

value = d.get('d', 0)


for key, val in d.items():
    print(f"Dict Key: {key}, Value: {val}")
print("Get with default:", value)

# ==== 5. Loops & Comprehensions ====
for i in range(1, 4):
    print("Range Loop:", i)

squares = [x * x for x in range(5)]
print("Squares:", squares)

# ==== 6. Functions ====
def add(a, b=0):
    return a + b

print("Function add:", add(2, 3))

# ==== 7. Recursion ====
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print("Factorial(5):", factorial(5))

# ==== 8. Strings ====
s = "hello world"
print("First char:", s[0])
print("Reversed:", s[::-1])
print("Split:", s.split())
print("Join:", "-".join(['a', 'b', 'c']))

# ==== 9. Heaps (Min/Max) ====
import heapq

min_heap = []
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 2)
print("Min-heap pop:", heapq.heappop(min_heap))

max_heap = []
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -1)
print("Max-heap pop:", -heapq.heappop(max_heap))

# ==== 10. Deque ====
from collections import deque

dq = deque()
dq.append(1)
dq.appendleft(2)
dq.pop()
dq.popleft()
print("Deque:", dq)

# ==== 11. Counter ====
from collections import Counter

freq = Counter([1, 1, 2, 3, 3, 3])
print("Counter:", freq)

# ==== 12. Grid Traversal ====
m, n = 3, 3
grid = [[0] * n for _ in range(m)]

for i in range(m):
    for j in range(n):
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + dx, j + dy
            if 0 <= ni < m and 0 <= nj < n:
                pass  # safe neighbor access

print("Empty Grid:", grid)

# ==== 13. Lambda & Sorting ====
pairs = [(1, 3), (2, 2), (3, 1)]
pairs.sort(key=lambda x: x[1])
print("Sorted by second item:", pairs)

# ==== 14. Two Pointers ====
arr = [1, 2, 3, 4]
i, j = 0, len(arr) - 1
while i < j:
    print("Two pointers:", arr[i], arr[j])
    i += 1
    j -= 1

# ==== 15. Binary Search ====
def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

print("Binary search:", binary_search([1, 2, 3, 4, 5], 3))

# ==== 16. Fibonacci (DP) ====
n = 7
fib = [0, 1]
for i in range(2, n+1):
    fib.append(fib[i-1] + fib[i-2])
print("Fibonacci up to n:", fib)

# ==== 17. Min Cost Climbing Stairs Example ====
def minCostClimbingStairs(cost):
    a, b = cost[0], cost[1]
    for i in range(2, len(cost)):
        a, b = b, cost[i] + min(a, b)
    return min(a, b)

print("Min Cost Climbing Stairs:", minCostClimbingStairs([10, 15, 20]))


#Mutating outer variables
def counter():
    n = 0
    def inc():
        nonlocal n     # rebind outer n
        n += 1
        return n
    return inc

c = counter()
print(c())  # 1
print(c())  # 2


#wrapper calls
def log_calls(fn):
    def wrapper(*args, **kwargs):
        print(f"→ {fn.__name__}({args}, {kwargs})")
        result = fn(*args, **kwargs)
        print(f"← {result}")
        return result
    return wrapper

@log_calls
def add(a, b): return a + b
add(2, 3)

