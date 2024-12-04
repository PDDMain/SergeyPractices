# HW Tasks

## Task 1: Merge Two Sorted Lists

**Problem:**  
You are given two sorted lists of integers, A and B. Your task is to merge them into a single sorted list without duplicates.

**Input:**  
The first line contains the integers in list A (space-separated).  
The second line contains the integers in list B (space-separated).

**Output:**  
A single line containing the merged sorted list without duplicates, space-separated.

**Example Input:**  
```
1 3 5 7  
2 3 5 8  
```

**Example Output:**  
```
1 2 3 5 7 8  
```

---

## Task 2: Frequency of Elements

**Problem:**  
Given a list of integers, determine the frequency of each unique element and display them in ascending order of the elements.

**Input:**  
A single line containing the integers in the list (space-separated).

**Output:**  
Each line should contain an element and its frequency, separated by a space, sorted by the elements in ascending order.

**Example Input:**  
```
4 5 6 5 4 3 2 4 5
```

**Example Output:**  
```
2 1  
3 1  
4 3  
5 3  
6 1  
```

---

## Task 3: Anagram Groups

**Problem:**  
You are given a list of words. Group the words that are anagrams of each other.

**Input:**  
The first line contains an integer n, the number of words.  
The next n lines each contain a single word.

**Output:**  
Each group of anagrams should be printed on a separate line, with words separated by spaces. The groups should be ordered by the first occurrence of any word in the group.

**Example Input:**  
```
6  
listen  
silent  
enlist  
google  
gooegl  
abc  
```

**Example Output:**  
```
listen silent enlist  
google gooegl  
abc  
```

---

## Task 4: Longest Substring with At Most K Distinct Characters

**Problem:**  
Given a string and an integer K, find the length of the longest substring that contains at most K distinct characters.

**Input:**  
A single line containing the string S.  
A single integer K.

**Output:**  
A single integer representing the length of the longest substring with at most K distinct characters.

**Example Input:**  
```
eceba  
2  
```

**Example Output:**  
```
3  
```

**Explanation:** The substring "ece" has length 3 with 2 distinct characters.

---

# Easy Dynamic Programming Tasks

## Task 5: Fibonacci Sequence

**Problem:**  
Write a program to compute the nth Fibonacci number using dynamic programming. The Fibonacci sequence is defined as:

```
Fib(0) = 0  
Fib(1) = 1  
Fib(n) = Fib(n-1) + Fib(n-2) for n > 1  
```

**Input:**  
A single integer n (0 ≤ n ≤ 30).

**Output:**  
A single integer representing the nth Fibonacci number.

**Example Input:**  
```
7  
```

**Example Output:**  
```
13  
```

---

## Task 6: Climbing Stairs

**Problem:**  
You are climbing a staircase that has n steps. You can either climb 1 or 2 steps at a time. Write a program to determine how many distinct ways you can climb to the top.

**Input:**  
A single integer n (1 ≤ n ≤ 30).

**Output:**  
A single integer representing the number of distinct ways to climb to the top.

**Example Input:**  
```
4  
```

**Example Output:**  
```
5  
```

**Explanation:** The five ways to climb to the top are:
- 1 step + 1 step + 1 step + 1 step  
- 1 step + 1 step + 2 steps  
- 1 step + 2 steps + 1 step  
- 2 steps + 1 step + 1 step  
- 2 steps + 2 steps  

## [Task 7](https://codeforces.com/group/cNX0FWzXMV/contest/570318/problem/G)

