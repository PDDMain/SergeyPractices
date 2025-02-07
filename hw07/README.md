# Set of tasks on graphs

## Problem A: Convert Adjacency Matrix to Adjacency List

**Input:**
- The first line contains a single integer `n` — the number of vertices in the graph.
- The next `n` lines contain `n` integers each, forming the adjacency matrix. Each element is either `0` (no edge) or `1` (edge).

**Output:**
- Print the adjacency list of the graph. For each vertex `i` (from `1` to `n`), output its neighbors in ascending order, space-separated.

**Example:**
Input: 
```
4
0 1 1 0
1 0 0 1
1 0 0 1
0 1 1 0 
```
Output: 
```
2 3
1 4
1 4
2 3
```

---

## **Problem B: Convert Adjacency List to List of Edges**

**Input:**
- The first line contains an integer `n` — the number of vertices in the graph.
- Each of the next `n` lines contains the adjacency list for a vertex `i`. Each line starts with the number of neighbors followed by the neighbors themselves.

**Output:**
- Print all edges as a list of pairs `(u, v)` in ascending order of `u`, then by `v`. Each pair is represented as two space-separated integers.

**Example:**
Input:
```
3
2 2 3
1 1
1 1
```
Output:
```
1 2
1 3
```

---

## **Problem C: Convert List of Edges to Adjacency Matrix**

**Input:**
- The first line contains two integers `n` and `m` — the number of vertices and edges.
- The next `m` lines each contain two integers `u` and `v`, indicating an edge between vertices `u` and `v`.

**Output:**
- Print the adjacency matrix of the graph as `n` lines of `n` integers.

**Example:**
Input: 
```
4 4
1 2 1 3
2 4 3 4
```

Output: 
```
0 1 1 0
1 0 0 1
1 0 0 1
0 1 1 0
```

---

## **Problem D: Check if Graph is Connected**

**Input:**
- The first line contains two integers `n` and `m` — the number of vertices and edges.
- The next `m` lines each contain two integers `u` and `v`, indicating an edge between vertices `u` and `v`.

**Output:**
- Print `YES` if the graph is connected, otherwise `NO`.

**Example 1:**
Input: 
```
4 3
1 2 2
3 3 4
```

Output: 
```
YES
```

**Example 2:**
Input: 
```
4 2
1 2
3 4
```
Output: 
```
NO
```

---

## **Problem E: Check if Graph is a Tree**

**Input:**
- The first line contains two integers `n` and `m` — the number of vertices and edges.
- The next `m` lines each contain two integers `u` and `v`, indicating an edge between vertices `u` and `v`.

**Output:**
- Print `YES` if the graph is a tree, otherwise `NO`.

**Example 1:**
Input: 
```
4 3
1 2
2 3
3 4
```

Output: 
```
YES
```

**Example 2:**
Input: 
```
4 4
1 2
2 3
3 4
4 1
```
Output: 
```
NO
```

---

## **Problem F: Depth First Search**

**Input:**
- The first line contains two integers `n` and `m` — the number of vertices and edges.
- The next `m` lines each contain two integers `u` and `v`, indicating an edge between vertices `u` and `v`.
- The last line contains a single integer `s` — the starting vertex.

**Output:**
- Print the vertices visited by DFS in the order they are visited, space-separated.

**Constraints:**
- If there are multiple vertices that can be visited from the current vertex, the algorithm must visit the vertex with the smaller number first.

**Example:**
Input: 
```
5 4
1 2
1 3
2 4
2 5
1 
```
Output: 
```
1 2 4 5 3
```

---

## **Problem G: Breadth First Search**

**Input:**
- The first line contains two integers `n` and `m` — the number of vertices and edges.
- The next `m` lines each contain two integers `u` and `v`, indicating an edge between vertices `u` and `v`.
- The last line contains a single integer `s` — the starting vertex.

**Output:**
- Print the vertices visited by BFS in the order they are visited, space-separated.

**Constraints:**
- If there are multiple vertices that can be visited from the current vertex, the algorithm must visit the vertex with the smaller number first.

**Example:**
Input: 
```
5 4
1 2
1 3
2 4
2 5
1
```
Output: 
```
1 2 3 4 5
```

---

This contest covers parsing between different graph representations, connectivity, tree checks, and traversal techniques while following the additional condition for **DFS** and **BFS**.


# Set of general tasks

## Task 1: Robot Painter

### Problem Description:
A robot is painting a one-dimensional wall consisting of N segments, numbered from 1 to N. The robot has a list of K painting instructions, where each instruction tells it to paint a specific segment a certain color. If a segment is painted multiple times, the last instruction takes precedence.

Determine the final color of each segment after all instructions are executed.

### Input Format:

1. Two integers N (number of segments) and K (number of instructions).
2. K lines follow, each containing two integers and a string:
   * i: The segment to paint (1-indexed).
   * c: The color to paint the segment.
   
### Output Format:

Print N space-separated strings representing the color of each segment after all instructions. If a segment is never painted, output "NONE" for that segment.

### Constraints:

* 1≤N≤10^5 
* 1≤K≤10^5
 
Colors are strings of length between 1 and 10, consisting of lowercase English letters.

### Example Input:
```
5 3  
1 red  
2 blue  
1 green  
```

### Example Output:

```
green blue NONE NONE NONE
```


## Task 2: 11 Cows and Equal Groups

### Problem Description:
You are given 11 cows, each with a specific weight. Your task is to determine if it is possible to pick any 10 cows and divide them into two groups of equal total weight.

### Input Format:

11 integers representing the weights of the cows.

### Output Format:
* Print "YES" if it is possible to divide any 10 cows into two groups of equal weight. 
* Print "NO" otherwise.

### Constraints:

Each weight is a positive integer between 1 and 10^6.

### Example Input:

```
10 20 30 40 50 60 70 80 90 100 110  
```

Example Output:
```
NO
```

## Task 3: Flights with Limited Connections

### Problem Description:
You are planning a trip and want to determine the shortest possible travel time between two cities. 

However, your trip is subject to the following constraints:
1. You can have at most 4 flights in total.
2. Each connecting flight adds 2 hours to your total travel time. 

Determine the minimum travel time from city A to city B under these conditions.

### Input Format:

1. Two integers N (number of cities) and M (number of direct flights). 
2. M lines follow, each containing three integers:
   * u,v,t: A direct flight from city u to city v that takes t hours.
3. Two integers A and B, the starting and destination cities.

### Output Format:
Print the minimum travel time from A to B, or "IMPOSSIBLE" if it’s not possible to reach B from A within the constraints.

### Constraints:

* 1≤N≤500 
* 1≤M≤10^4
* 1≤t≤100
* Cities are numbered from 1 to N.

### Example Input:

```
5 6  
1 2 3  
2 3 4  
3 4 5  
1 5 10  
1 3 8  
3 5 2  
1 5  
```

### Example Output:

```
9
```

## Task 4: Treasure Hunt with Costly Keys

### Problem Description:
You are on a treasure hunt! There are N locked doors, numbered from 1 to N, and each door requires a unique key to open it. Some keys can be purchased outright, while others can only be found after opening certain doors. Your goal is to determine the minimum cost required to open all the doors.

### Input Format:

1. An integer N, the number of doors.
2. A line with N integers, where the i-th integer represents the cost of buying the key for door i.
3. A line with N integers, where the i-th integer represents the position of the key for door i:
   * If the value is “-1,” the key can only be bought. 
   * Otherwise, it represents the door behind which the key is found.

### Output Format:

Print the minimum cost to open all doors.

### Constraints:

* 1≤N≤10^5
* 1 ≤ Cost of each key ≤10^9  

### Example Input:

```
5  
4 7 3 2 8  
-1 1 -1 2 3  
```

### Example Output:

```
9
```

## Task 5: Circular Tracks and Meeting Points

### Problem Description:
You are given a circular track of length L. There are N runners starting at different positions on the track, each with a constant speed. Runners can meet only if they are at the exact same position on the track at the same time.

Determine the earliest time T (if any) at which at least two runners meet after they start.

### Input Format:

1. An integer L, the length of the circular track.
2. An integer N, the number of runners.
3. N lines follow, each containing two integers:
   * x_i: The starting position of the i-th runner.
   * v_i: The speed of the i-th runner.

### Output Format:
Print the earliest time T when at least two runners meet. If no two runners meet, print “NO.”

### Constraints:
* 2 ≤ N ≤ 10^5 
* 1 ≤ L ≤ 10^9 
* 0 ≤ x_i < L 
* 1 ≤ v_i ≤ 10^9
 
### Example Input:
```
12  
3  
0 2  
4 1  
8 2  
```

### Example Output:

```
4
```

## [Task 6 (Contest 11, Task F)](https://codeforces.com/group/cNX0FWzXMV/contest/580045/problem/F)

## [Task 7 (Contest 11, Task G)](https://codeforces.com/group/cNX0FWzXMV/contest/580045/problem/G)

## [Task 8 (Contest 11, Task H)](https://codeforces.com/group/cNX0FWzXMV/contest/580045/problem/H)

