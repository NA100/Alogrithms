"""
Alright — Matrix Chain Multiplication (MCM) is a classic interval DP problem.
It’s not about actually multiplying matrices, but about finding the optimal parenthesization to minimize scalar multiplications.
Problem
You’re given a sequence of matrices:
Matrix A₁ has dimensions p₀ × p₁
Matrix A₂ has dimensions p₁ × p₂
...
Matrix Aₙ has dimensions pₙ₋₁ × pₙ
You must find the minimum number of scalar multiplications needed to multiply them all.
Example
Dimensions: [10, 30, 5, 60]
That means:
A1: 10 × 30
A2: 30 × 5
A3: 5 × 60
Possible ways:
(A1 A2) A3: cost = (10×30×5) + (10×5×60) = 1500 + 3000 = 4500
A1 (A2 A3): cost = (30×5×60) + (10×30×60) = 9000 + 18000 = 27000
Minimum cost = 4500
"""