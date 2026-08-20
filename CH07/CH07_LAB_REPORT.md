# Lab Report — Chapter 7: Trees and Huffman Coding

*Complete both sections and commit this file with your code.*

## Test Results

```
Part 1: Directory traversal
BFS order:
root
docs
media
web
notes.txt
todo.txt
draft.docx
photo.png
song.mp3
index.html
style.css
DFS order:
root
docs
notes.txt
todo.txt
draft.docx
media
photo.png
song.mp3
web
index.html
style.css
Part 2: DFS vs BFS shortest path counterexample
DFS found target node:
target
BFS found target node:
target
Part 3: Mini Huffman coding
Character frequencies:
{'h': 1, 'u': 3, 'f': 4, 'm': 2, 'a': 1, 'n': 3, ' ': 5, 'c': 2, 'o': 2, 'd': 2, 'i': 3, 'g': 1, 'b': 1, 'l': 1, 's': 3, 't': 1, 'r': 3, 'e': 5, 'q': 1}
Code table:
{'f': '000', 'c': '0010', 'l': '00110', 'b': '00111', ' ': '010', 'e': '011', 'u': '1000', 'r': '1001', 'n': '1010', 'i': '1011', 's': '1100', 'q': '11010', 'o': '11011', 'm': '11100', 'd': '11101', 'h': '111100', 'g': '111101', 'a': '111110', 't': '111111'}
Encoded bitstring:
11110010000000001110011111010100100010110111110110111010111101010001111000101100110111011100010111111100101101111000100001001110111110001000010010111101010000111010001010110111100
Decoded text:
huffman coding builds trees from frequencies
Round trip matches original:
True
Fixed-width bit count (8 times length of string):
352
Compressed bit count:
179

```

## Reflection Questions

1. **Explain the difference between BFS and DFS to someone who has never programmed.**
   - Imagine you're searching a building for a specific person, and you don't know which floor or what room they are in. BFS is when you check each and every room on floor 1 before moving onto checking every room on floor 2, and so forth. You will never advance floors before checking every room on the floor you are currently on. On the other hand, DFS is when you walk down one hallway, and check every room in that hallway, and then advance to the next floor, and commit to another hallway and check all the rooms in that hallway before moving onto the next floor.

2. **Why do frequent letters get shorter codes? Use your own code table.**
  - The Huffman's algorithm always merges the two lowest-frequency nodes first. The more frequent characters are more likely to get assigned to its own high-priority node and gets folded into the tree much l later. This allows for shorter codes and faster access time. You essentially optimize the common case at the expense of the more rare case.
3. **Your decoder reads a stream of bits with no separators and still gets it right. Why is there never any ambiguity?**
  - There is never any ambiguity because Huffman codes have a property called prefix-free. In short, this causes a character's code to never have a prefix of another character's code.
