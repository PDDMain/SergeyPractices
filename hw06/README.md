# Homework 6

# Task 1: Maximum Coins Collection by a Robot

## Problem Description
You are given a grid of size `N x M`, where the robot starts at the top-left corner `(0, 0)` and aims to reach the bottom-right corner `(N-1, M-1)`. The robot can only move **right** or **up**.

Each cell `(i, j)` in the grid contains a certain number of coins, `a[i][j]`. The robot collects the coins in the cells it passes through. The goal is to calculate the **maximum number of coins** the robot can collect on its path.

The robot starts at cell `(0, 0)` which has no coins, and the destination cell `(N-1, M-1)` also has no coins. Coins are only present in the cells in between.

---

## Input Format
1. Two integers `N` and `M`, representing the number of rows and columns of the grid.
2. A 2D array `a` of size `N x M`, where:
   - `a[i][j]` is the number of coins in cell `(i, j)`.
   - `a[0][0] = a[N-1][M-1] = 0` (these cells have no coins).

---

## Output Format
An integer representing the maximum number of coins the robot can collect.

---

## Constraints
- `1 <= N, M <= 1000`
- `0 <= a[i][j] <= 1000`

---

## Example

### Input
```
4 4 
0 1 2 3
4 5 6 7 
8 9 10 11 
0 1 2 0
```

### Output
```
42
```

# Task 2: Robot Movement with Coins and Burglars

## Problem Description

You have a grid of size `N x M`. A robot starts at the top-left corner `(0, 0)` with **0 coins** initially. The robot wants to reach the bottom-right corner `(N-1, M-1)`. In each move, the robot can:

1. Move **right**: from `(i, j)` to `(i, j+1)`.
2. Move **up**: from `(i, j)` to `(i+1, j)`.  
3. Move **diagonally**: from `(i, j)` to `(i+1, j+1)`.

> **Note**: The wording "up" here means increasing the row index.  
> You can visualize the grid as follows (rows going down, columns going right):
> - Top-left is `(0,0)`
> - Bottom-right is `(N-1, M-1)`

Each cell `(i, j)` contains an integer `a[i][j]`:
- If `a[i][j] > 0`, that cell has **coins** and the robot **adds** that amount to its total.
- If `a[i][j] < 0`, that cell has **burglars** (e.g. `-k`), and the robot **loses** `k` coins.

The robot’s total coin count must **never become negative** at any point in the journey. If the coin count would drop below 0 by entering a particular cell, that path is considered **invalid**.

The goal is to find the **maximum number of coins** the robot can collect upon reaching `(N-1, M-1)` under these conditions. If there is **no valid path** that keeps the coin count non-negative at all times, print `-1`.

---

## Input Format

1. Two integers, `N` (rows) and `M` (columns) (N, M >= 2).
2. A 2D array `a` of size `N x M`, where each `a[i][j]` can be:
   - Positive (coins),
   - Zero (no effect),
   - Negative (burglars).

---

## Output Format

- A single integer: the **maximum** coins collected at `(N-1, M-1)` if a valid path exists.
- Print `-1` if no valid path exists.

---

## Constraints

- \( 1 \leq N, M \leq 1000 \)
- \(-10^4 \leq a[i][j] \leq 10^4\)

(You may adjust constraints depending on your solution approach.)

---

## Example 1

### Input
```
4 3 
0 2 5 
-1 1 1 
10 -2 2
-10 3 0
```

### Output
```
12
```

## Example 2

### Input
```
2 3
0 -1 1000
-1 -1 0
```

### Output
```
-1
```

## Example 3

### Input
```
3 3
0 -1 10 
-1 0 0 
10 -1 0
```

### Output
```
0
```

# Task 3: Robot Movement with Coins and Burglars - find way
For Task 2, you must find the path that yields the maximum number of coins. If there are multiple such paths, print the shortest one.

## Example 1

### Input
```
4 3 
0 2 5 
-1 1 1 
10 -2 2
-10 3 0
```

### Output
```
RIGHT
RIGHT
DOWN
DOWN
DOWN
```

## Example 2

### Input
```
2 3
0 -1 1000
-1 -1 0
```

### Output
```
-1
```

## Example 3

### Input
```
3 3
0 -1 10 
-1 0 0 
10 -1 0
```

### Output
```
DIAGONAL
DIAGONAL
```


# Task 4: Longest Common Substring

## Problem Description
You are given two lines of text (two strings).  
Your task is to find the **longest common substring** between these two strings and print:
1. The **length** of this longest common substring.
2. The **common substring** itself.

If multiple substrings tie for the maximum length, you may print **any** one of them.

---

## Input Format
1. Two lines of input, each containing a single string.

---

## Output Format
1. On the first line, print the integer length of the **longest common substring**.
2. On the second line, print the **common substring** itself.

---

## Constraints
- The lengths of the strings can range from 1 up to (potentially) 10^4
---

## Example

### Input
```
abcxuz
xyzabc
```

### Output
```
3 
abc
```

# Task 4: Longest Common Substring of 3 strings

## Problem Description
You are given three lines of text (three strings).  
Your task is to find the **longest common substring** between these two strings and print:
1. The **length** of this longest common substring.
2. The **common substring** itself.

If multiple substrings tie for the maximum length, you may print **any** one of them.

---

## Input Format
1. Three lines of input, each containing a single string.

---

## Output Format
1. On the first line, print the integer length of the **longest common substring**.
2. On the second line, print the **common substring** itself.

---

## Constraints
- The lengths of the strings can range from 1 up to 500.

---

## Example

### Input
```
abcxuz
xyabcx
aavfcxy
```

### Output
```
2
xy
```


# Task 5: Gray Codes

# Task 6: [Prime number](https://codeforces.com/group/cNX0FWzXMV/contest/573552/problem/G)