# Lab Report — Chapter 9: Dijkstra's Algorithm

*Complete both sections and commit this file with your code.*

## Test Results

```
=== Part 1: Book's warm-up graph ===
Costs: {'start': inf, 'a': 5, 'b': 2, 'finish': 6}
Parents: {'start': None, 'a': 'b', 'b': 'start', 'finish': 'a'}
Path: start -> b -> a -> finish

=== Part 2: Twin Peaks -> Golden Gate Bridge ===
BFS fewest-hops path: twin_peaks -> a -> b -> golden_gate
BFS hop count: 3
Dijkstra lowest-cost path: twin_peaks -> c -> d -> e -> golden_gate
Dijkstra total cost: 12

=== Part 3: Breaking Dijkstra with negative weights ===
Costs: {'start': inf, 'a': 2, 'b': -8, 'finish': 6}
Parents: {'start': None, 'a': 'start', 'b': 'a', 'finish': 'b'}
Path: start -> a -> b -> finish
Reported cost to finish: 6
True cheapest cost (by hand): 2 + (-10) + 5 = -3

```

## Reflection Questions

1. **Explain Dijkstra's algorithm to someone who has never programmed.**
   - Imagine you are planning on driving across town with traffic in mind. Instead of committing to one route and hoping for the best, you keep track of the fastest known time to reach every intersection you have come across. You also check the neighboring intersections to see if that time is faster. After completing this process, you are left with the fastest known time to reach your destination. Dijkstra's algorithm is essentially the same exact process, where you find the shortest path between nodes in a weighted graph.

2. **Why does the algorithm always pick the cheapest unprocessed node next, instead of going in order?**
  - Because going in order does not guarantee that a node is the current best route to reach the destination. Picking the cheapest unprocessed node each time guarantees that the unprocessed node's cost can only get more expensive by routing through something that's already more expensive than it.
3. **Where does the "cost" on an edge come from in real routing software, and how does changing what you measure change the answer without changing the algorithm?**
  - The edge cost is just a number you decide to sum along the path. It could be anything from distance, time, length, etc. Dijkstra's algorithm does not care what the numbers represent, it only cares about finding the path that minimizes the total.
