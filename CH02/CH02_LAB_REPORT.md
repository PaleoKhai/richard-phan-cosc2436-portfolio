# Lab Report — Chapter 2: Selection Sort

*Complete both sections and commit this file with your code.*

## Test Results

```
3
0
0
[2, 3, 5, 6, 10]
[]
[1, 4, 4]
[9, 1, 5]
['Radiohead', 'Kishore Kumar', 'Wilco', 'Neutral Milk Hotel', 'Beck', 'The Strokes', 'The Black Keys']

```

## Reflection Questions

1. **Explain selection sort to someone who has never programmed.**
   - Imagine you have a messy hand of playing cards and you want to sort them from lowest to highest value. An efficient way to do this is by looking through your entire hand and locating the lowest value card and placing that card into a new pile. You would then repeat this process until all the cards in your hand are sorted. Selection sort is fundamentally the same exact principle. It searches through an unsorted list, finds the smallest valu,e and moves it into its correct position, one element at a time.

2. **Your list gets twice as long. Does selection sort do twice the work, or more?**
   - My find_smallest function loops through the list once O(n) times. Then, my selection_sort function calls find_smallest once per element, which is n times. So the total work is O(n) * O(n), which means O(n^2). This essentially means doubling the list size causes selection sort to do quadruple the work, not just double.

3. **Chapter 2 says arrays are used more often than linked lists in practice. Based on what you built, why would that be?**
   - Based on what I have coded, it is incredibly inefficient to use a linked list over an array. In my code, elements are accessed directly by index. Using an array allows me to access that element in constant time since the element has a predictable memory address. Since linked lists do not support direct indexing, in order to access a specific element, I would have to traverse through the list until I reach my desired element, which makes the linked list much more inefficient than an array in this scenario.
