# Programming Competition Tasks

## Task 1: Array Rotation
### Story:
You are given an array `a` representing the levels of your favorite video game. In each level, you need to rotate the array left by one position to unlock new challenges. However, the levels are numbered in such a way that they must be in non-decreasing order to pass the game. You can rotate the array at most `k` times, and you need to figure out if it is possible to make the array sorted by doing the rotations. If it is possible, return the minimum number of rotations needed, otherwise, return -1.

### Input:
- An integer `n` representing the length of the array.
- An integer `k` representing the maximum number of rotations allowed.
- An array `a` of length `n` containing integers.

### Output:
- Return the minimum number of rotations needed to sort the array, or `-1` if it is not possible.

### Constraints:
- `1 ≤ n ≤ 1000`
- `0 ≤ k ≤ n`

### Example:
#### Input:
```
7
4 2 3 4 5 1 2
```
#### Output:


---

## Task 2: Minimum Swaps to Sort
### Story:
In a small village, there is a group of children who are playing a game with numbered cards. The children need to line up in ascending order by card number, but some children are not standing in the right order. The teacher allows them to swap cards with one another to get into the correct order. Your task is to find the minimum number of swaps the children need to make to line up in ascending order.

### Input:
- An integer `n` representing the number of children (maximum `1000`).
- An array `a` of length `n` containing the card numbers.

### Output:
- Return the minimum number of swaps needed to sort the array in ascending order.

### Constraints:
- `1 ≤ n ≤ 1000`

### Example:
#### Input:
```
6
5 5 4 3 2 1
```
#### Output:

---

## Task 3: String Compression
### Story:
Peter is trying to save space on his device by compressing a long string of text. He comes up with a simple compression method: for each sequence of identical characters, he replaces them with the character followed by the number of times it appears consecutively. For example, `"aaabbbcc"` would be compressed to `"a3b3c2"`. Can you help Peter compress his string efficiently?

### Input:
- A string `s` of length `n` containing lowercase English letters.

### Output:
- Return the compressed string.

### Constraints:
- `1 ≤ n ≤ 1000`

### Example:
#### Input:

#### Output:

---

## Task 3: String Compression
### Story:
Peter is trying to save space on his device by compressing a long string of text. He comes up with a simple compression method: for each sequence of identical characters, he replaces them with the character followed by the number of times it appears consecutively. For example, `"aaabbbcc"` would be compressed to `"a3b3c2"`. Can you help Peter compress his string efficiently?

### Input:
- A string `s` of length `n` containing lowercase English letters.

### Output:
- Return the compressed string.

### Constraints:
- `1 ≤ n ≤ 1000`

### Example:
#### Input:

#### Output:

---

## Task 4: Prawn Path
### Story:
You are given a 2xN desk, and a prawn starts at the bottom-left corner (position `(1, 0)`). The prawn can move either vertically or diagonally. It can "eat" the opposite prawn by moving diagonally to a cell where a prawn is located (denoted by 'X'). Additionally, the prawn can move vertically to a cell with 'X', in which case it will simply move to the 'X' without "eating" it. The prawn cannot move through cells with '.'.

Your goal is to calculate how many different ways the prawn can travel from the bottom-left corner to the top-right corner of the grid, while avoiding paths that lead to blocked or inaccessible cells.

### Movement rules for the prawn:
- **Vertical move**: The prawn can move up or down from its current position to an adjacent cell, whether the cell contains '.' or 'X'.
- **Diagonal move**: The prawn can move diagonally to a cell containing 'X' (where it "eats" the prawn). The prawn cannot move diagonally to a cell with '.'.

### Input:
- An integer `n` (1 ≤ n ≤ 50), representing the width of the desk (2xN grid).
- The next `n` lines describe the 2xN grid. Each line will contain exactly two characters: either '.' (empty space where the prawn can move) or 'X' (occupied space where the prawn cannot move).
  - The prawn starts at the bottom-left corner `(1, 0)`.
  - The goal is to reach the top-right corner `(0, n-1)`.

### Output:
- Output a single integer: the number of different ways the prawn can travel from the bottom-left corner to the top-right corner.

### Constraints:
- The grid has dimensions 2xN, where 1 ≤ N ≤ 50.
- The input grid will be valid with only '.' and 'X' characters.

### Example:
#### Input:

#### Output:

---

### Notes:
- For each task, ensure to test with edge cases like small grid sizes, sorted input, or strings with repeating characters.
- These tasks can be implemented using different algorithmic approaches including dynamic programming, greedy methods, and graph traversal techniques.
