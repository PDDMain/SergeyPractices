### Task 1: Magic Numbers
A "magic number" is a number that satisfies the following conditions:

It is a three-digit number.
The sum of its digits is divisible by 5.
The product of its digits is an odd number.
Problem:
How many magic numbers exist?

#### Input:
None (the task is independent of input).

#### Output:
Output the total number of magic numbers.

#### Example:
For a three-digit number:

The number 135 is magic because:
Sum of digits = 1 + 3 + 5 = 9 (not divisible by 5, so not magic).
Product = 1 × 3 × 5 = 15 (odd, satisfies condition 3).

### Task 2: Divisible Coins
You are given n coins, where each coin has a value of 1, 2, or 3. Your goal is to determine if it's possible to divide the coins into two groups such that the sum of values in both groups is equal.

#### Input:
A single integer n (1 ≤ n ≤ 100) representing the number of coins.
The second line contains n integers (1, 2, or 3) representing the value of each coin. 
#### Output:
Print YES if it's possible to divide the coins into two groups with equal sums, otherwise print NO.

#### Example:
Input:
```
4
1 2 3 2
```
Output:
```
YES
```

### Task 3: Chocolate Bars
You have a chocolate bar consisting of n × m squares. You can break the chocolate into smaller pieces along the lines between the squares. Each break splits one piece into two smaller pieces, and it costs 1 unit of energy.

#### Problem:
Determine the minimum energy required to break the entire chocolate into 1 × 1 squares.

#### Input:
Two integers n and m (1 ≤ n, m ≤ 100), representing the dimensions of the chocolate bar.
#### Output:
Output a single integer, the minimum energy required to break the chocolate.

#### Example:
Input:
```
2 3
```
Output:
```
5
```

### Task 4: Arranging Books
There are n books, and each book has a unique number from 1 to n written on its spine. The books are arranged on a shelf in some random order. Your goal is to sort the books so that their numbers are in ascending order (1, 2, ..., n), but you can only swap two adjacent books in one move.

#### Problem:
Determine the minimum number of swaps needed to sort the books.

#### Input:
The first line contains an integer n (1 ≤ n ≤ 100), the number of books.
The second line contains n integers, representing the current arrangement of the books.
#### Output:
Output a single integer, the minimum number of adjacent swaps required.

#### Example:
Input:
```
5
4 3 2 5 1
```
Output:
```
8
```

### Task 5: Flower Picking with a Basket
You have a garden with n flowers in a straight line, each with a beauty value bᵢ (positive or negative). You also have a basket that can hold at most m flowers. You want to pick a continuous segment of flowers such that the sum of their beauty values is maximized, while ensuring that the segment contains no more than m flowers.

#### Problem:
Find the maximum sum of beauty values that can be obtained from any continuous segment of at most m flowers.

#### Input:
The first line contains two integers n and m (1 ≤ m ≤ n ≤ 10000), where n is the number of flowers and m is the basket capacity (maximum number of flowers you can pick).
The second line contains n integers bᵢ (-100000 ≤ bᵢ ≤ 100000), the beauty values of the flowers.
#### Output:
Output a single integer, the maximum sum of beauty values.

#### Example:
Input:
```
6 3
-2 4 -1 3 5 -6 1
```
Output:
```
12
```

### Task 6: Shuffling a Deck
You are given a deck of n cards, each with a unique number from 1 to n, shuffled in a random order. Your goal is to return the deck to its sorted order (1, 2, ..., n) using a special shuffle operation.

#### Special Shuffle Operation:
In one operation, you can split the deck into two contiguous segments and reverse the order of one of these segments.
#### Problem:
You are allowed to perform at most n operations to sort the deck. After each operation, output the current state of the deck.
Any correct way to sort the list is acceptable, as long as the number of iterations does not exceed n.

#### Goal:
Return a list of lists, where each list represents the state of the deck after an operation.
The final list must represent the sorted deck.
#### Input:
The first line contains an integer n (2 ≤ n ≤ 100), the number of cards.
The second line contains n integers, representing the current shuffled order of the deck.
#### Output:
Output a list of lists, where each list represents the deck state after one operation. If the deck is sorted before using n or less operations, stop the process.

#### Example:
Input:
```
5
3 2 5 4 1
```
Output:
```
3 2 5 4 1
2 3 5 4 1
2 3 5 1 4
1 2 3 4 5
```

#### Explanation:
Start with the shuffled deck [3, 2, 5, 4, 1].
Split into [3, 2] and [5, 4, 1], reverse [3, 2] → [2, 3], resulting in [2, 3, 5, 4, 1].
Split into [2, 3, 5] and [4, 1], reverse [4, 1] → [1, 4], resulting in [2, 3, 5, 1, 4].
Split into [2, 3] and [5, 1, 4], reverse [5, 1, 4] → [4, 1, 5], resulting in [1, 2, 3, 4, 5].
The process stops since the deck is now sorted.

### Task 7: Permutations with Missing Digits
You are given a sequence of n integers, which is supposed to represent a permutation of numbers from 1 to n. However, some numbers are missing from the sequence and replaced with a question mark (?). Your task is to fill in the missing numbers to form a valid permutation.

#### Input:
The first line contains a single integer n (2 ≤ n ≤ 12), the size of the permutation.
The second line contains n integers, where some of the numbers are ?, representing the missing values.
#### Output:
Output a single line containing the valid permutation. If there are multiple valid solutions, output any one of them. If it's not possible to construct a valid permutation, output NO.

#### Example 1:
Input:
```
5
3 ? 1 ? 5
```
Output:
```
3 4 1 2 5
```
#### Example 2:
Input:
```
4
? 3 ? 3
```
Output:
```
NO
```

### Task 8: Balanced Subarray
You are given an array of n integers, which contains only 1s and -1s. Your task is to find the longest subarray in which the sum of elements is exactly 0.

#### Input:
The first line contains an integer n (2 ≤ n ≤ 100), the size of the array.
The second line contains n integers, each either 1 or -1, representing the array.
#### Output:
Output a single integer: the length of the longest subarray with a sum of 0. If no such subarray exists, output 0.

#### Example 1:
Input:
```
8
1 -1 1 -1 -1 1 1 -1
```

Output:
```
8
```
#### Example 2:
Input:

```
6
1 1 -1 -1 1 -1
```

Output:
```
4
```