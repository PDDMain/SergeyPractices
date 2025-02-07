## Task A: Email Decryption

### Statement
Tom sent an email with an encrypted message that contains only the symbols **A**, **B**, and **C**. To decode this text, a special rule is applied: each symbol is cyclically incremented—**A** becomes **B**, **B** becomes **C**, and **C** becomes **A**. Moreover, for the symbol at position `i` (0-indexed), you must increment it `(i % 4)` times.

*For example, the symbol at position 0 is not changed (since 0 mod 4 is 0), while the symbol at position 2 is incremented twice.*

### Input
A single line containing a string composed solely of the characters **A**, **B**, and **C**.

### Output
A single line containing the decoded string.

### Sample Test Case

**Input**
```
ABC
```

**Output**
```
ACB
```


---

## Task B: Robot Figure Recognition

### Statement
A robot starts at the origin point **(0, 0)** and draws a figure by sequentially connecting the following points:

1. From **(0, 0)** to **(X1, Y1)**
2. From **(X1, Y1)** to **(X2, Y2)**
3. From **(X2, Y2)** to **(X3, Y3)**
4. From **(X3, Y3)** back to **(0, 0)**

Given the integer coordinates **X1, Y1, X2, Y2, X3, Y3**, determine whether the resulting figure is a **Square**, a **Rectangle**, or **None** of these.

### Input
A single line containing six space-separated integers:
X1 Y1 X2 Y2 X3 Y3


### Output
Output one of the following (case-sensitive): **Square**, **Rectangle**, or **None**.

### Sample Test Case

**Input**
```
0 1 1 1 1 0
```

**Output**
```
Square
```


---

## Task C: Knight's Shortest Path

### Statement
On an **N×N** chessboard, a hungry chess knight starts at cell **(x1, y1)** and wants to reach cell **(x2, y2)**, where delicious chess grass grows. The knight moves in an "L" shape (two cells in one direction and one cell perpendicular to that direction). Determine the minimum number of moves required for the knight to reach the target cell.

### Input
- The first line contains an integer **N** — the size of the chessboard.
- The second line contains two space-separated integers **x1 y1** — the starting cell coordinates.
- The third line contains two space-separated integers **x2 y2** — the target cell coordinates.

### Output
Output a single integer — the minimum number of moves the knight must make to reach **(x2, y2)**.

### Sample Test Case

**Input**
```
8 0 0 7 7
```

**Output**
```
6
```

---

## Task D: Найти Амира
[Link to codeforces](https://codeforces.com/group/cNX0FWzXMV/contest/581876/problem/D)

---

## Task E: Domino Coloring
[Link to cogniterra](https://cogniterra.org/lesson/50877/step/5?unit=42373)

---

## Task F: Inequality Puzzle
[Link to cogniterra](https://cogniterra.org/lesson/50877/step/6?unit=42373)

---

## Task G: Сортировка пузырком
[Link to codeforces](https://codeforces.com/group/cNX0FWzXMV/contest/581876/problem/G)

---

## Tasks*
Try to solve [tasks from cogniterra](https://cogniterra.org/lesson/41715/step/1?unit=33404) preparation from scratch in 2 hours
