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
{3, 4}
{-34, 1, 2, 5, 6, 36}
{1, 2, 36}
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
