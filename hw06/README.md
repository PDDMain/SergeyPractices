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

------------------

# Additional tasks

------------------------------------

# Task 7: Symmetric Points with Respect to a Horizontal Line

## Problem Description
You are given a set of points \((x, y)\) in a 2D plane. Determine if there exists a horizontal line (i.e., \(y = c\)) such that the set of points is symmetric with respect to that line.  
Formally, for every point \((x_i, y_i)\) above the line, there must be a corresponding point \((x_i, 2c - y_i)\) below the line.

**Goal**  
- Print "YES" if such a horizontal line exists.
- Print "NO" otherwise.

---

## Input Format
1. An integer \(N\) representing the number of points.
2. \(N\) lines follow, each with two integers \(x_i\) and \(y_i\).

---

## Output Format
- "YES" if the points can be symmetrically divided by some horizontal line.
- "NO" otherwise.

---

## Constraints
- \(1 <= N <= 10^5\)
- \(-10^9 <= x_i, y_i <+ 10^9\)

*(You may adjust constraints depending on your solution approach.)*

---

## Example

### Input
```
6
0 1
2 3
2 -1
-3 -3
2 1
-3 5
```

### Output
```
YES
```

# Task 8: Lego Towers - Make Them Beautiful

## Problem Description
Peter has a row of \(N\) towers, each with a certain height. A row of towers is called **"beautiful"** if for any two neighboring towers, their heights differ by at most 1. Peter has \(K\) extra blocks that he can use to **add** to the towers (but he cannot remove blocks). Determine if Peter can make the row beautiful by distributing these \(K\) blocks among the towers in some way.

**Goal**  
- Print "YES" if it’s possible to achieve the condition (neighboring towers differ in height by \(\leq 1\)).
- Print "NO" otherwise.

---

## Input Format
1. An integer \(N\) representing the number of towers.
2. An integer \(K\) representing how many extra blocks are available.
3. A list (or array) of \(N\) integers representing the heights of the towers.

---

## Output Format
- "YES" if there is a way to make the row beautiful.
- "NO" otherwise.

---

## Constraints
- \(1 <= N <= 10^6\)
- \(0 <= K <= 10^9\)
- Tower heights are non-negative and can be up to 10^9.

---

## Example

### Input
```
5 3 
2 2 3 5 6
```

### Output
```
YES
```

# Task 9: Magic House Teleports

## Problem Description
You have a "magic house" with \(N\) rooms in a row, labeled from 1 to \(N\). Each room \(i\) has a teleport distance \(k_i\) associated with it. If you are in room \(i\), you can teleport to room \(i + k_i\). You start in room 1 and want to know if it is possible to reach room \(N\).

**Goal**  
- Print "YES" if you can reach room \(N\).
- Print "NO" otherwise.

---

## Input Format
1. An integer \(N\), the number of rooms.
2. A list of \(N\) integers \(k_1, k_2, ..., k_N\)

---

## Output Format
- "YES" if room \(N\) is reachable from room 1.
- "NO" otherwise.

---

## Constraints
- \(1 <= N <= 10^6\)
- \(-10^9 <= k_i <= 10^9\)

*(You may adjust constraints depending on your solution approach.)*

---

## Examples

### Input
```
5 
1 1 1 2 2
```

### Output
```
NO
```

### Input
```
5 
3 3 0 -2 2
```

### Output
```
YES
```

# Task 10: Fibbi's Program Reconstruction

## Problem Description
Fibbi had a program in a simple language that produces a sequence of outputs. The language has:
- One variable (`V`).
- Two commands:
  1. `PRINT` — prints the current value of `V`.
  2. `FIBB` — updates `V` to be `V + prevV` (where `prevV` is the value of `V` from before the update).

Initially:
- `V = 1`
- `prevV = 0` (the value of `V` before it ever got changed)

You are given the **output** of this program (the sequence of integers printed). You must reconstruct **any valid sequence of commands** that could produce this output.

**Goal**  
Given the sequence of printed values, output a valid series of `PRINT` and `FIBB` commands that results in exactly that sequence of printed values.

---

## Input Format
1. An integer \(L\), the length of the output sequence.
2. \(L\) integers representing the printed values.

---

## Output Format
- A sequence of commands (`PRINT` or `FIBB`) that produces the given printed values when run on the initial conditions.

*(There may be multiple correct answers. Any valid solution is acceptable.)*

---

## Constraints
- \(1 <= L <= 10^5\)
- Printed values can be up to \(10^{18}\) (Fib-like growth can be large).

---

## Example

### Input
```
3
1 1 2 2 3
```

### Output
```
PRINT
FIBB
PRINT
FIBB
PRINT
PRINT
FIBB
PRINT
```

# Task 11: Daria the Hacker and Oliver's Mysterious Phone Number

## Problem Description
Daria is a clever hacker on a quest to uncover her friend Oliver’s secret phone number. Oliver, who likes to tinker with web designs, built a quirky website that **initially** showed his real phone number. The website then lets anyone press one of two buttons:

1. **+10** – This button adds 10 to the current number on the screen.
2. **×3** – This button multiplies the current number on the screen by 3.

Over time, people (and Oliver himself) pressed these buttons in some sequence, transforming the phone number into the current (rather large or otherwise changed) number on the page.

Daria has managed to **hack** into the website's logs, discovering the entire history of button presses **in the exact order** they occurred, as well as the **final** number currently displayed. But she needs to **work backwards** to figure out what the **original** phone number was.

Her mission: **reconstruct Oliver’s hidden phone number**.

---

## Input Format
1. An integer `F`, representing the **final** number displayed on the webpage.
2. An integer `K`, the number of operations that were performed on the page.
3. A list of `K` operations in the order they were applied (each operation is either `+10` or `×3`).

---

## Output Format
Print a single integer: the **original** phone number (before any operations were applied).

---

## Constraints
- \(1 <= K <= 10^5\)
- The final number `F` can be very large (potentially up to \(10^{18}\) or beyond).
- Each reverse step must result in an integer when reversing the “×3” operation, otherwise the data might be invalid (or someone input the wrong button presses into the database).

---

## Example

### Input
```
151 3
+10 ×3 +10
```

### Output
```
37
```
