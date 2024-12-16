# Dynamic Programming Tasks

## Task 1: Fibonacci Sequence

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

## Task 2: Climbing Stairs

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


## Task 3: Climbing Stairs with Dangerous Rocks

**Description:**

You are climbing a staircase with **n** steps, but some steps are dangerous, and you cannot step on them. The status of each step is given in a list where:

- `D` indicates the step is safe.
- `|` indicates the step is dangerous and cannot be stepped on.

You can climb either 1 step or 2 steps at a time. Determine the number of distinct ways you can safely reach the top of the staircase.

**Input Format:**

1. An integer \( n \), representing the number of steps in the staircase.
2. A list of \( n \) characters where:
   - `D` represents a safe step.
   - `|` represents a dangerous step.

**Constraints:**

- \( 1 \leq n \leq 100 \)
- The input will always ensure that:
  - The first step is `D` (safe).
  - The last step is `D` (safe).
  - Neighbour rocks cannot be both unsafe

**Output:**

An integer representing the number of distinct ways to reach the top of the staircase while avoiding dangerous steps.

**Example:**

- **Input:**
```
6
DD|DDD
```

- **Output:**
```
2
```

## Task 4: Climbing Stairs with Dangerous Rocks and Maximum Coins

**Description:**

You are climbing a staircase with **n** steps. Each step is either dangerous or safe, and every step has a certain number of coins. Your goal is to collect the maximum number of coins while safely reaching the top of the staircase.

- `D c`: A safe step with **c** coins.
- `|`: A dangerous step that cannot be stepped on.

You can climb either 1 step or 2 steps at a time. Determine the **maximum number of coins** you can collect while safely reaching the top of the staircase.

**Input Format:**

1. An integer \( n \), representing the number of steps in the staircase.
2. A list of \( n \) strings where:
   - Each string is either `D c` (safe step with \( c \) coins) or `|` (dangerous step).

**Constraints:**

- \( 1 \leq n \leq 100 \)
- The input will always ensure that:
  - The first step is safe (`D c`).
  - The last step is safe (`D c`).
- \( 0 \leq c \leq 100 \) (coins on a step).

**Output:**

An integer representing the **maximum number of coins** that can be collected while safely reaching the top of the staircase.

**Example:**

- **Input:**
```
6 
D 1
D 2 
|
D 4
D 6
D 3
```

- **Output:** 
```
12
```

## Task 5: Jumping Stairs with Dangerous Rocks and Maximum Coins
The same as **task 4**, but You can climb either 2 step or 3 steps at a time

- **Input:**
```
9
D 2
D 1
D 2 
D 3
|
D 10
D 6
D 1
D 10
```

- **Output:** 
```
24
```

## Task 6: Jumping Stairs with Dangerous Rocks and Maximum Coins
The same as **task 5**, but instead of printing maximum amount of coins - print sequence of indexes of visited rocks

- **Input:**
```
9
D 2
D 1
D 2 
D 3
|
D 10
D 6
D 1
D 10
```

- **Output:** 
```
1 3 6 9
```