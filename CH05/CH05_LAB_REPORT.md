# Lab Report — Chapter 5: Hash Tables

*Complete both sections and commit this file with your code.*

## Test Results

```
Part 0: Contact book / voter check
555-1234
Not found
Allowed to vote
Already voted!

Part 1: Page cache
MISS: example.com/a
MISS: example.com/b
HIT: example.com/a
MISS: example.com/c
HIT: example.com/b

Part 2: Mini hash table
get('name'): Grace
get('missing'): None
load factor: 0.25

Part 3: Collision comparison
simple_hash:      collisions=2, longest_chain=2
first_char_hash:  collisions=2, longest_chain=2

```

## Reflection Questions

1. **Explain a hash table to someone who has never programmed.**
   - Imagine you are at a theater and need to drop off your coat at the coat check. The employee then asks for your ticket and they look at the first or last two digits of your ticket and put your coat on that rack. A hash table is essentially the same principle. It takes whatever it is you want to store, and converts it into a number. You can then find that item at that number whenever you need access to it.

2. **Chapter 5 says lookups are fast "on average." When is that not true, and what makes it go wrong?**

  - The average-case of a hash table is O(1) when the hash table has a good function and also has enough space to store all the items. It is not true when the function is poor and multiple items get stored at the same position. Lookups can also not work or be very slow when the number of items that need to be stored exceed the size of the hash table. In that situation, the hash table would need to be resized.

3. **Your page cache avoided repeating expensive work. Where have you seen caching in software you use?**
  - I have seen caching be used in web browsers, like Google Chrome, to store images or scripts for a page that I might visit frequently. I have also seen caching on social media software like TikTok, where it caches search results to memory.
