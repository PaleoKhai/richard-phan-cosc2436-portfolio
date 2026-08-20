# Lab Report — Chapter 8: Balanced Trees

*Complete both sections and commit this file with your code.*

## Test Results

```
=== PART 1: Basic BST operations ===
[20, 30, 40, 50, 70]
3
True
3
=== PART 2: Same values, different insertion order ===
Tree A height: 0
Tree B height: 0
Tree A in-order: []
Tree B in-order: []
Tree A search comparisons for largest value: 0
Tree B search comparisons for largest value: 0
=== PART 3: AVL rotations fix the shape ===
AVL tree height after sorted insertion: 4
=== REFLECTION ===
See comments above for the reflection table.

```

## Reflection Questions

1. **Explain a binary search tree to someone who has never programmed.**
   - Imagine you are playing the "guess my number" game with your friend. You are told that they are thinking of a number between 1 and 100. You decide to split that in half by guessing 50. After which you are told higher/lower, you then split that half into half again. A binary search tree is essentially the same concept but you turn that "guess" into a node, or a stored value, so you can use it later on for comparison purposes.

2. **A tree built from sorted input performs no better than a plain list. Explain why, using your own two trees.**
  - If I insert two trees with one having the input, [1,2,3,4,5,6,7], and the other having the input, [4,2,6,1,3,5,7], the tree with the sorted input would continue to branch right because the next node is always a larger value than the old node. The other tree with the unsorted input would branch both left and right. A balanced tree is only fast when the insertions are evenly split left and right.
3. **Chapter 8 says balanced trees are used for database indexes. Based on what you built, why is a tree a good fit for that job?**
  - Balanced trees give roughly logarithmic search. So even when used for large database indexes, the lookup process is still relatively quick and easy. Furthermore, balanced trees allow for easy insertion and deletion without the need to re-sort everything.
