# Lab Report — Chapter 4: Quicksort

*Complete both sections and commit this file with your code.*

## Test Results

```
Part 1: Divide & Conquer warm-ups
recursive_sum: 52
recursive_count: 12
recursive_max: 10
binary_search_recursive (target=8): 9
binary_search_recursive (target=99): -1

Part 2: Quicksort
first pivot: [-3, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random pivot: [-3, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
middle pivot: [-3, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Part 3: Benchmark
shape             strategy    result            
------------------------------------------------
unsorted          first       0.000830 s        
unsorted          random      0.001219 s        
sorted            first       RecursionError    
sorted            random      0.001222 s        
reverse sorted    first       RecursionError    
reverse sorted    random      0.000975 s        

```

## Reflection Questions

1. **Explain quicksort to someone who has never programmed.**
   - Imagine you have a large stack of papers with names on them that you need to sort alphabetically by last name. Instead of sorting through the entire stack at once, you instead pick one paper at random to be your "pivot point." You then split the rest of the stack into smaller piles. One with all the names that come before the pivot's last name, and one with all the names that come after it. You then repeat this process on each of those two smaller piles until every pile is small enough that it's already sorted. Once every pile is in order, you stack them back together and end up with everything fully sorted.

2. **A random pivot usually avoids the worst case. Why does randomness help here?**

  - Quicksort's worst case happens when the pivot chosen is consistently the smallest or largest value. This causes one side of the split to have zero elements while the other side has almost everything. This worst case reliably happens when a fixed strategy for picking the pivot point is utilized. Therefore, picking the pivot at random allows for the algorithm to be much more consistent.

3. **Where does sorting show up in software you actually use?**
  - The process of sorting is used everywhere in countless software. It can be used to sort an email inbox by date, or used to sort search results by price, etc. It can also be used internally by other algorithms.
