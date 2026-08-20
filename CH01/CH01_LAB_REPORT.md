# Lab Report — Chapter 1: Binary Search

*Complete both sections and commit this file with your code.*

## Test Results

```
9
10
9
2
128
7
8
256
8
9
1024
10
11
2048
11
12
10
10
3
100
100
6
1000
1000
9
10000
10000
13
100000
100000
16
1000000
1000000
19

As list size increases from 10 to 1,000,000, binary search's step count only grew a minor amount, while linear search's step count grew in direct proportion to the list size. The growth chart shows linear search's line rising steeply, while binary search's line stays relatively flat near the bottom of the chart even as list size increases drastically. The growth chart essentially shows O(n) growth versus O(logn) growth.

```

## Reflection Questions

1. **Explain binary search to someone who has never programmed.**
   - *Imagine you are looking up a name in a phone book. Instead of starting from page one and checking every name, you open to the middle of the phone book and check if your name comes before or after that point. You then repeat this process, discarding the other half every time, until you find your name. This process is must more efficient then searching from the very first page.*

2. **Doubling the list adds only one step to binary search. Why does that happen?**
   - *Fundamentally, binary search essentially cuts the remaining list in half with every guess, therefore, the number of steps needed ultimately depends on how many times you must divide the list size by two before finding your result. Which means doubling the list means halving the list one more time.*

3. **Where does binary search show up in real software?**
   - *Binary search is a very commonly used searching method. It can be used anywhere that has large amounts of sorted data that needs to be searched quickly. For example, searching for a word in a dictionary app or finding a song title in a song index.*
