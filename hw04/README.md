# Pointer Tasks

## Task 1: Check if Array is Palindrome
### Problem:
Determine whether a given array of integers is a palindrome. An array is considered a palindrome if it reads the same backward as forward.

### Input:
The first line contains an integer n, the number of elements in the array.
The second line contains n space-separated integers representing the array.
### Output:
Output YES if the array is a palindrome.
Otherwise, output NO.

### Example Input 1:
```
5
1 2 3 2 1
```
### Example Output 1:

```
YES
```

### Task 2: Find Intersection of Two Sorted Arrays

#### Problem:
Given two sorted arrays, find their intersection. The intersection should include each element as many times as it appears in both arrays.

**Note:** You are **not allowed** to use the `set` data structure to solve this problem.

#### Input:
- The first line contains two integers `n` and `m`, the sizes of the first and second arrays, respectively.
- The second line contains `n` space-separated integers representing the first sorted array.
- The third line contains `m` space-separated integers representing the second sorted array.

#### Output:
- Output the intersection elements as a single line of space-separated integers. If there is no intersection, output `-1`.

#### Example Input 1:
```
5
5 
1 2 2 3 4 
2 2 3 5 6
```

#### Example Output 1:
```
2 2 3
```

## Task 3: Find Pair with Given Sum in Sorted Array

### Problem:
Given a sorted array of integers and a target sum, determine if there exists a pair of numbers in the array that adds up to the target sum. If such a pair exists, return the pair. If multiple pairs exist, return the first pair found. If no such pair exists, return `-1`.

#### Input:
- The first line contains two integers `n` and `target`, where `n` is the number of elements in the array.
- The second line contains `n` space-separated integers representing the sorted array.

#### Output:
- If a pair is found, output the two numbers separated by a space.
- If no pair is found, output `-1`.

#### Example Input 1:
```
5 
9 
1 2 4 5 6
```
#### Example Output 1:
```
4 5
```
#### Example Input 2:
```
4 
10 
1 3 5 7
```
#### Example Output 2:
```
-1
```

## Task 4
* Fix HW 3 task 4

## [Task 5](https://codeforces.com/group/cNX0FWzXMV/contest/570318/problem/G)
* Fix

## Task 6: Longest Increasing Subsequence (Length Only)

**Problem:**  
Given a list of integers, find the length of the longest strictly increasing subsequence.

**Input:**  
A single line containing the integers in the list (space-separated).

**Output:**  
A single integer representing the length of the longest increasing subsequence.

**Example Input:**  
```
10 9 2 3 7 101 18
```

**Example Output:**  
```
4
```

**Explanation:**  
One longest increasing subsequence is [2, 3, 7, 101], which has length 4.

---

## Task 7: All Substrings With Exactly K Distinct Characters

**Problem:**  
Given a string S and an integer K, find all unique substrings of S that contain exactly K distinct characters. Print these substrings in lexicographical (alphabetical) order, one per line.

**Input:**  
A single line containing the string S.  
A single integer K.

**Output:**  
Print each qualifying substring on its own line, sorted lexicographically. If no such substrings exist, print nothing.

**Example Input:**  
```
abacab
3
```

**Example Output:**  
```
abc
bac
cab
```

---

## Task 8: Minimize Absolute Difference Between Two Sorted Arrays

**Problem:**  
You are given two sorted arrays A and B. The goal is to find two elements, one from each array, such that their absolute difference is minimized. More formally, find a[i] in A and b[j] B that minimize |a[i] - b[j]|.

**Input:**  
Two lines:  
- The first line contains the integers of the sorted array A (space-separated).  
- The second line contains the integers of the sorted array B (space-separated).

**Output:**  
Two integers, one from each array, that minimize the absolute difference. If there are multiple pairs, return any one of them.

**Example Input:**  
```
1 3 15 11 2
23 127 235 19 8
```

**Example Output:**  
```
11 8
```

**Explanation:**  
The pair (11, 8) minimizes the absolute difference with a value of 3.

---

## Task 9: Board Game Player Movement

**Problem:**  
In this board game, there is an infinite line of cells. Two players start at cell 1. Each player rolls a die (with numbers 1 to 6) to move forward. If a player’s move would place them on the same cell as the other player, they stay in their current position instead. Given the dice rolls for each player, determine the final positions of both players.

**Input:**  
Two lines:  
- The first line contains the dice rolls for Player 1 (space-separated integers between 1 and 6).  
- The second line contains the dice rolls for Player 2 (space-separated integers between 1 and 6).

**Output:**  
Two integers representing the final positions of Player 1 and Player 2.

**Example Input 1:**  
```
1 2 3
2 3 4
```

**Example Output 1:**  
```
6 5
```

**Explanation:**  
- Player 1 moves: 1 (to 2), 2 (to 4), 3 (to 6).  
- Player 2 moves: 2 (to 3), 3 (to 5). On their third roll, they would land on cell 6, but Player 1 is already there, so they stay at 5.

**Example Input 2:**  
```
1 1 2 6 4
2 1 5 1 2
```

**Example Output 2:**  
```
6 5
```

- Player 1 moves: 1 (to 2), 1 (stays 2, here is player 2), 2 (stays 2, here is player 2), 6 (to 8), 4 (to 12)
- Player 2 moves: 2 (to 3), 1 (to 4), 5 (to 9), 1 (to 10), 2 (stays 10, here is player 1)
---