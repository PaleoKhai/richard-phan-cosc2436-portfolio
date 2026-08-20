# Lab Report — Chapter 10: Greedy Algorithms

*Complete both sections and commit this file with your code.*

## Test Results

```
Part 1: Scheduled classes
[('Art', 9.0, 10.0), ('Math', 10.0, 11.0), ('Music', 11.0, 12.0)]
Part 2: Greedy knapsack choice
[('stereo', 3000, 4)]
Part 2: Greedy knapsack value
3000
Part 2: Brute-force knapsack choice
[('laptop', 2000, 3), ('guitar', 1500, 1)]
Part 2: Brute-force knapsack value
3500
Part 2: Gap between brute force and greedy
500
Part 3: Stations chosen, in order
['kone', 'ktwo', 'kthree', 'kfive']
Part 3: Exact solver combinations to check for 5 stations
32
Part 3: Exact solver combinations to check for 20 stations
1048576
Part 3: Exact solver combinations to check for 100 stations
1267650600228229401496703205376
Reflection
TODO: write your reflection answer here

```

## Reflection Questions

1. **Explain the greedy strategy to someone who has never programmed.**
   - Imagine you are packing for a trip across the country, instead of planning ahead and preparing clothes or whatever other items you may need for the specific location, you decide to just grab whatever seems best like the best choice at the time. This is the greedy strategy, where at every step you just take whatever looks like the best local choice, and commit to it, and move onto the next step. It is fast and simple, but you risk not grabbing the best overall outcome.

2. **Greedy was perfect for scheduling and wrong for the knapsack. What changed about the problem?**
  - In scheduling, you greedily pick the event that finishes the earliest, and it can never come back to hurt you in the future. This essentially cuts off any future options. On the other hand, the knapsack problem breaks that safety net, taking the most valuable item right now can eat up the capacity you may need in the future. Greedy in knapsack has to weigh an item's value against how much room it will cost you.
3. **You already wrote a greedy algorithm in an earlier lab — building the Huffman tree in Chapter 7 repeatedly merges the two lowest-frequency nodes. Is that one exactly optimal, or an approximation?**
  - I believe Huffman coding is optimal. Huffman coding is essentially a rare case where using the greedy strategy produces the best possible answer. Huffman is safe because of approvable structural property of optimal codes themselves. Thus, it is optimal, and not just an approximation.
