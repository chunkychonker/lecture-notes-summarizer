# Study Sheet: lecture1_greedy

## Key Concepts

- Greedy Algorithm
- Greedy Choice Property
- Optimal Substructure
- Exchange Argument (Greedy Stays Ahead)
- Activity Selection / Interval Scheduling
- Huffman Coding
- Dijkstra's Shortest Path
- Kruskal's MST
- Prim's MST
- Fractional Knapsack
- 0/1 Knapsack

## Definitions

- **Greedy Algorithm**: An algorithm that builds a solution piece by piece, always committing to the locally optimal choice at each step without backtracking or reconsidering previous decisions.
- **Greedy Choice Property**: A globally optimal solution can be reached by making locally optimal (greedy) choices; the greedy choice at each step is guaranteed to belong to some optimal solution and never needs to be undone.
- **Optimal Substructure**: An optimal solution to the problem contains optimal solutions to its subproblems. After making the greedy choice, the remaining problem is a smaller instance of the same problem. Shared with dynamic programming.
- **Exchange Argument**: A proof technique for greedy correctness: assume an optimal solution differs from the greedy solution, then show you can swap (exchange) an element of the optimal solution for the greedy choice without degrading solution quality. Repeating this converts the optimal solution into the greedy solution, proving the greedy solution is also optimal.
- **Greedy Stays Ahead**: A variant of the exchange argument: prove by induction that after each step, the greedy solution is at least as far along (by some measure) as any other solution.
- **Activity Selection Problem**: Given n activities with start times s_i and finish times f_i, select the maximum number of mutually compatible (non-overlapping) activities. Optimal greedy strategy: sort by earliest finish time and greedily pick compatible activities.
- **Huffman Coding**: A greedy algorithm to build an optimal binary prefix code minimizing total encoded length. Repeatedly merges the two lowest-frequency nodes into a new node (sum of frequencies) using a min-priority queue until one tree remains. Provably optimal among prefix codes.
- **Prefix Code**: A binary code where no codeword is a prefix of another, enabling unambiguous decoding.
- **Fractional Knapsack**: Knapsack variant where items can be taken in fractional amounts. Greedy by highest value-to-weight ratio is optimal.
- **0/1 Knapsack**: Knapsack variant where each item is taken whole or not at all. Greedy value-to-weight ratio is NOT optimal; requires dynamic programming.

## Key Facts

- Two required properties for greedy correctness: (1) Greedy Choice Property and (2) Optimal Substructure.
- Activity Selection greedy rule: sort by finish time (earliest first), select activity if s_i >= last_finish. Running time: O(n log n) dominated by sort; selection scan is O(n).
- Incorrect greedy rules for Activity Selection: shortest duration first, earliest start time first, fewest conflicts first — none are provably optimal.
- Huffman Coding uses a min-priority queue (binary heap). Running time: O(n log n) for n characters.
- In Huffman coding, lower-frequency characters get longer codes (deeper in tree); higher-frequency characters get shorter codes (shallower).
- Dijkstra's algorithm is correct only for non-negative edge weights.
- Kruskal's MST: greedily adds cheapest edge that does not form a cycle.
- Prim's MST: greedily grows tree by adding cheapest edge leaving the current tree.
- Greedy fails on 0/1 Knapsack: a high-ratio small item can crowd out a better combination; dynamic programming required.
- Greedy algorithms are typically O(n log n); the challenge is proving correctness, not implementation.

## Likely Exam Material

- State the two properties required for greedy correctness (Greedy Choice Property and Optimal Substructure).
- Trace the Activity Selection algorithm on a given input, sorted by finish time.
- Explain and apply the exchange argument to prove a greedy algorithm optimal.
- Explain why greedy fails on 0/1 Knapsack but succeeds on Fractional Knapsack.
- Describe the Huffman coding greedy strategy and its running time.
- Identify correct vs. incorrect greedy rules for Activity Selection.
- Compare greedy and dynamic programming: both require optimal substructure; greedy commits to one choice without evaluating all subproblems.

## Review Questions

1. What are the two properties a problem must have for a greedy algorithm to yield a globally optimal solution?
2. In Activity Selection, why is 'earliest finish time' the correct greedy rule? Why do 'shortest duration' and 'earliest start time' fail?
3. Describe the exchange argument proof technique. How does it establish greedy optimality?
4. Trace Huffman coding on characters with frequencies: A=5, B=9, C=12, D=13, E=16, F=45. What tree structure results?
5. Why does Dijkstra's algorithm require non-negative edge weights?
6. Contrast Fractional Knapsack and 0/1 Knapsack with respect to greedy correctness. Provide a counterexample showing greedy fails for 0/1 Knapsack.
7. What data structure supports Huffman coding efficiently, and what is the resulting time complexity?
8. How does the 'greedy stays ahead' variant differ from the standard exchange argument?
