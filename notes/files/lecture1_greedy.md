# Lecture 1: Greedy Algorithms

## Course: Introduction to Algorithms (CS 4820)
### Topic: Greedy Algorithm Design Paradigm

---

## 1. What Is a Greedy Algorithm?

A greedy algorithm builds a solution piece by piece, always choosing the option that looks best *right now* — the locally optimal choice — in the hope that this leads to a globally optimal solution. It never reconsiders or backtracks on choices it has already made.

The defining characteristic: at each step, commit to the choice that seems best at that moment, without worrying about future consequences.

Greedy is not always correct. For some problems it produces an optimal answer; for others it produces a reasonable but suboptimal one. The hard part is *proving* a greedy approach actually yields the optimum.

---

## 2. When Does Greedy Work? Two Key Properties

A problem is a good candidate for a greedy solution when it has both:

**Greedy Choice Property.** A globally optimal solution can be reached by making a locally optimal (greedy) choice at each step. In other words, the choice that looks best locally is part of *some* optimal solution — you never have to undo it.

**Optimal Substructure.** An optimal solution to the problem contains within it optimal solutions to subproblems. After making the greedy choice, what remains is a smaller instance of the same problem.

If a problem has both properties, greedy will find the optimum. Optimal substructure is also shared with dynamic programming — the difference is that greedy commits to one choice without solving all subproblems first.

---

## 3. Canonical Example: Activity Selection (Interval Scheduling)

**Problem.** You are given n activities, each with a start time s_i and finish time f_i. Only one activity can run at a time. Select the maximum number of mutually compatible (non-overlapping) activities.

**Greedy strategy.** Sort activities by *finish time*, earliest first. Repeatedly pick the next activity whose start time is greater than or equal to the finish time of the last activity selected.

**Why finish time?** Choosing the activity that finishes earliest leaves the maximum amount of remaining time for the other activities — it greedily preserves the most future opportunity.

**Pseudocode.**
```
Sort activities by finish time
selected = [first activity]
last_finish = f_1
for each remaining activity i in order:
    if s_i >= last_finish:
        add activity i to selected
        last_finish = f_i
return selected
```

**Running time.** O(n log n), dominated by the sort. The selection scan itself is O(n).

**Common wrong greedy choices** (these do NOT give optimum): picking the shortest activity first, or picking the activity that starts earliest, or picking the one with fewest conflicts. Only "earliest finish time" is provably optimal here.

---

## 4. Proving Greedy Correctness: The Exchange Argument

The standard technique for proving a greedy algorithm optimal is the **exchange argument** (also called "greedy stays ahead" in one of its forms).

The idea: assume there is an optimal solution that differs from the greedy one. Show that you can swap (exchange) an element of the optimal solution for the greedy choice *without making the solution worse*. Repeating this transforms the optimal solution into the greedy one while preserving optimality — proving the greedy solution is also optimal.

"Greedy stays ahead" variant: prove by induction that after each step, the greedy solution is at least as far along (by some measure) as any other solution.

---

## 5. Huffman Coding

**Problem.** Given a set of characters with frequencies, build a binary prefix code (no codeword is a prefix of another) that minimizes the total encoded length.

**Greedy strategy.** Repeatedly take the two lowest-frequency nodes, merge them into a new node whose frequency is their sum, and reinsert. Continue until one tree remains. Lower-frequency characters end up deeper in the tree (longer codes); higher-frequency characters end up shallower (shorter codes).

**Data structure.** A min-priority queue (binary heap) to repeatedly extract the two minimums.

**Running time.** O(n log n) for n characters, using a binary heap.

Huffman coding is provably optimal among prefix codes — a classic exchange-argument proof.

---

## 6. Other Notable Greedy Algorithms

- **Dijkstra's shortest path** — greedily selects the unvisited vertex with the smallest known distance. Correct for non-negative edge weights only.
- **Kruskal's MST** — greedily adds the cheapest edge that does not form a cycle.
- **Prim's MST** — greedily grows a tree by adding the cheapest edge leaving the current tree.
- **Fractional Knapsack** — greedily take items by highest value-to-weight ratio. Greedy is optimal for the *fractional* version but NOT for 0/1 knapsack (which needs dynamic programming).

---

## 7. Key Warning: Greedy Fails on 0/1 Knapsack

For the 0/1 knapsack problem (each item is taken whole or not at all), the greedy value-to-weight ratio strategy can fail. Example: a high-ratio small item can crowd out a better combination of other items. 0/1 knapsack requires dynamic programming for a guaranteed optimum. This is the canonical "greedy is tempting but wrong" example and a frequent exam question.

---

## 8. Summary

Greedy algorithms are fast and simple, often O(n log n), and elegant when they work. The challenge is never the implementation — it's recognizing whether the greedy choice property and optimal substructure hold, and proving it (usually via an exchange argument). When in doubt, greedy is a hypothesis to be proven, not assumed.

**Exam reminder:** Be ready to (a) state the two properties required for greedy correctness, (b) trace activity selection by finish time, and (c) explain why greedy fails on 0/1 knapsack but works on fractional knapsack.
