## Set
### Task 1: Unique Elements in Two Lists
#### Problem:
You are given two lists of integers, A and B. Your task is to find:

The set of elements that are present in both lists (intersection).
The set of elements that are present in either list but not both (symmetric difference).
The set of elements that are unique to A (elements in A but not in B).
Write a program that computes and outputs these three sets.

#### Input:
The first line contains the integers in list A (space-separated).
The second line contains the integers in list B (space-separated).

#### Output:
Three lines:
The intersection of A and B.
The symmetric difference of A and B.
The elements unique to A.

#### Example Input:

```
1 2 3 4 36
3 4 5 6 -34
```
#### Example Output:

```
3 4
-34 1 2 5 6 36
1 2 36
```

### Task 2: Count Unique Words
#### Problem:
You are given a paragraph of text containing multiple sentences. Your task is to count the number of unique words in the text, ignoring case and punctuation.

#### Input:

A single string containing the paragraph.
#### Output:

An integer representing the count of unique words.
#### Example Input:

```
The quick brown fox jumps over the lazy dog. The fox was very quick!
```

#### Example Output:
```
7
```
**Explanation**: After removing punctuation and ignoring case, the unique words are: {'brown', 'jumps', 'over', 'lazy', 'dog', 'was', 'very'}.

## Dict
### Task 3: Inventory Management
#### Story:
A small store keeps track of its inventory using a dictionary. The owner wants to perform the following operations:

Add new items to the inventory.
Update the quantity of existing items.
Find the total quantity of concrete type of items in stock.

#### Task:
Write a program to help the store owner manage their inventory.

#### Input:

The first line contains an integer n (1 ≤ n ≤ 100), the number of operations.
Each of the next n lines describes an operation:
"ADD <item> <quantity>" to add a new item or increase the quantity of an existing item.
"REMOVE <item> <quantity>" to decrease the quantity of an item (but not below zero).
"TOTAL <item>" to calculate the total quantity of items.
Quantity of items in the store isn't negative

#### Output:
For each "TOTAL <item>" operation, output the total quantity of items in stock.

#### Example Input:
```
6
ADD apples 10
ADD bananas 5
REMOVE apples 3
ADD oranges 7
TOTAL apples
ADD bananas 2
REMOVE bananas 2
TOTAL bananas
```

Example Output:
```
7
5
```

### Task 4: Word Frequency Counter
#### Story:
A librarian wants to analyze the text of a book to determine the most frequently used words. The librarian ignores case and punctuation, and considers only words with at least three characters.

#### Task:
Write a program that counts the frequency of each word in a paragraph and identifies the top k most frequent words.

#### Input:

A single string containing the paragraph.
An integer k (1 ≤ k ≤ 10), the number of top words to display.
#### Output:

A list of the k most frequent words and frequency in text, sorted by frequency in descending order (if frequencies are equal, sort alphabetically). 
#### Example Input:
```
The quick brown fox jumps over the lazy dog. The fox was very quick.
3
```

#### Example Output:

```
the 3
fox 2
quick 2
```

## Additional Part
### Task 5: Array Rotation
#### Story:
You are given an array `a` representing the levels of your favorite video game. In each level, you can rotate the array **left** or **right** by one position to unlock new challenges. To pass the game, the levels must be in **non-decreasing order**.
Before the game starts, you are allowed to rotate the array at most k times (either left or right). You need to determine if it is possible to make the array sorted by performing these rotations. If possible, return the **minimum number of rotations** needed and the direction (L for left or R for right). If it is not possible to sort the array within k rotations, return -1.
#### Input:
- An integer `n` representing the length of the array. (1 <= n <= 1000)
- An integer `k` representing the maximum number of rotations allowed.
- An array `a` of length `n` containing integers.

#### Output:
- If it is possible to sort the array within k rotations, return the minimum number of rotations and the direction (L or R).
- Otherwise, return -1.
#### Constraints:
- `1 ≤ n ≤ 1000`
- `0 ≤ k ≤ n`

#### Example 1:
Input:
```
7
7
4 2 3 4 5 1 2
```
Output:
```
-1
```

#### Example 2:
Input:
```
7
4
2 3 4 5 1 2
```
Output:
```
2 R
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
3 2 1 4 5
1 2 3 4 5
```

#### Explanation:
Start with the shuffled deck [3, 2, 5, 4, 1].
Split into [3, 2] and [5, 4, 1], reverse [5, 4, 1] → [1, 4, 5], resulting in [3, 2, 1, 4, 5].
Split into [3, 2, 1] and [4, 5], reverse [3, 2, 1] → [1, 2, 3], resulting in [1, 2, 3, 4, 5].
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
You are given an array of n integers, which contains only 1s and -1s. Your task is to find the subarray in which the sum of elements is exactly 0 and length more than 2.

#### Input:
The first line contains an integer n (2 ≤ n ≤ 1000), the size of the array.
The second line contains n integers, each either 1 or -1, representing the array.
#### Output:
Output a two integers: the begin and end indexes of the subarray with a sum of 0. If no such subarray exists, output 0 and length more than 2.
Numeration starts from 0

#### Example 1:
Input:
```
8
-1 1 1 -1 1 -1 -1 1 -1
```

Output:
```
2 7
```
#### Example 2:
Input:

```
6
1 1 -1 -1 1 -1
```

Output:
```
1 4
```