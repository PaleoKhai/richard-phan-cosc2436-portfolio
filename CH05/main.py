"""
Lab: Rooted & Compressed - Tree Traversal and Huffman Coding
COSC 2436 - Chapter 7

This starter code scaffolds three parts:
  Part 1: BFS vs DFS directory traversal
  Part 2: DFS vs BFS shortest-path counterexample (mango-seller style)
  Part 3: Mini Huffman coding (build tree, encode, decode)

Fill in every function marked with a TODO. Do not change function
signatures - the entry point at the bottom calls them exactly as written.
All input data below is hardcoded (no file I/O, no randomness) so the
lab runs the same way every time.
"""

from collections import deque
import heapq


# ---------------------------------------------------------------------------
# PART 1: File directory traversal (BFS vs DFS)
# ---------------------------------------------------------------------------

class DirNode:
    """A simple directory/file node used to build a tree (no real filesystem
    access is used here - this is a hardcoded tree so the lab is portable)."""

    def __init__(self, name, children=None):
        self.name = name
        # children is a list of DirNode objects (an empty list means a 'file')
        self.children = children if children is not None else []


def build_sample_directory():
    """Builds a small, hardcoded nested directory tree (>= 10 nodes) so
    students can compare BFS vs DFS traversal order without needing real
    files on disk."""
    # Leaf 'files'
    file1 = DirNode("notes.txt")
    file2 = DirNode("todo.txt")
    file3 = DirNode("photo.png")
    file4 = DirNode("song.mp3")
    file5 = DirNode("draft.docx")
    file6 = DirNode("index.html")
    file7 = DirNode("style.css")

    # Sub-folders
    docs = DirNode("docs", [file1, file2, file5])
    media = DirNode("media", [file3, file4])
    web = DirNode("web", [file6, file7])

    # Root (11 nodes total)
    root = DirNode("root", [docs, media, web])
    return root


def print_names_bfs(start_dir):
    """
    Print every node name in the tree using BREADTH-FIRST traversal.
    Use a deque and the book's queue/popleft pattern:
        queue = deque([start_dir])
        while queue:
            current = queue.popleft()
            print(current.name)
            for child in current.children:
                queue.append(child)

    NOTE: No 'searched' set is required here (unlike the Chapter 6
    mango-seller graph).
    """
<<<<<<< HEAD
    queue = deque([start_dir])  # starter queue - build the loop below
    # TODO: while the queue is not empty, popleft the current node, print
    #       its name, then append each of its children to the queue
    # TODO: add a comment here explaining WHY no 'searched' set is needed
    #       for a tree (hint: trees have no cycles, unlike Chapter 6's graph)
    while queue:
        current  = queue.popleft()
        print(current.name)
        for child in current.children:
            queue.append(child)
=======
    # TODO: Store the name as the key and number as the value in contact_book
    # Step 1: Use contact_book[name] = number to add the entry
    contact_book[name] = number
>>>>>>> 0408890cebd9d35c77241e995fa950baec168538
    pass


def print_names_dfs(start_dir):
    """
    Print every node name in the tree using DEPTH-FIRST traversal.
    This should be RECURSIVE and needs no queue.
    """
<<<<<<< HEAD
    # TODO: print start_dir.name, then recursively call print_names_dfs
    #       on each child in start_dir.children
    print(start_dir.name)
    for child in start_dir.children:
        print_names_dfs(child)
    pass
=======
    # TODO: Check if name exists in contact_book
    # Step 1: Use an if/else or .get() to safely look up the key
    # Step 2: Return the number if found, otherwise return "Not found"
    if name in contact_book:
        return contact_book[name]
    else:
        return "Not found"

>>>>>>> 0408890cebd9d35c77241e995fa950baec168538


# ---------------------------------------------------------------------------
# PART 2: DFS fails at shortest path - counterexample
# ---------------------------------------------------------------------------

class TreeNode:
    """A binary tree node used for the mango-seller style counterexample."""

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def build_mango_tree():
    """
    Builds a small, hardcoded binary tree mirroring the book's diagram:
      - 'target' appears 3 levels deep on the LEFT branch
      - 'target' appears 1 level deep on the RIGHT branch
    DFS (which dives left first) will incorrectly return the farther
    target; BFS should correctly return the closer one.
    """
<<<<<<< HEAD
    # Left branch: root -> left -> left -> left = target (depth 3)
    left_leaf = TreeNode("target")
    left_level2 = TreeNode("L2", left=left_leaf)
    left_level1 = TreeNode("L1", left=left_level2)

    # Right branch: root -> right = target (depth 1)
    right_leaf = TreeNode("target")

    root = TreeNode("root", left=left_level1, right=right_leaf)
    return root
=======
    # TODO: Step 1: Check if name is already a key in voted_dict
    # Step 2: If yes, this is a duplicate vote attempt -> return "Already voted!"
    # Step 3: If no, add name to voted_dict (mark as voted) -> return "Allowed to vote"
    if name in voted_dict:
        return "Already voted!"
    else:
        voted_dict[name] = True
        return "Allowed to vote"
    
>>>>>>> 0408890cebd9d35c77241e995fa950baec168538


def dfs_search(root, target):
    """
    Depth-first search: recursively dive down the LEFT branch first,
    then the right, and return the FIRST node whose value == target
    that is found. Return None if not found.
    """
<<<<<<< HEAD
    # TODO: check if root is None -> return None
    # TODO: check if root.value == target -> return root
    # TODO: recursively search root.left, and if a result is found return it
    # TODO: otherwise recursively search root.right and return that result
    if root is None:
=======
    time.sleep(0.01)  # short sleep so the demo runs quickly
    return "Contents of " + url


def get_page(cache, url):
    """
    Return the page contents for 'url', using 'cache' (a dict) to avoid
    repeating expensive simulate_server_call() calls.
    Should print whether this request was a "HIT" or "MISS" before returning.
    """
    # TODO: Step 1: Check if url is already a key in cache
    # Step 2: If it is, print "HIT" and return the cached value
    # Step 3: If not, print "MISS", call simulate_server_call(url),
    #         store the result in cache, then return it
    if url in cache:
        print(f"HIT: {url}")
        return cache[url]
    else:
        print(f"MISS: {url}")
        result = simulate_server_call(url)
        cache[url] = result
        return result


# ============================================================
# PART 2: Build Your Own Mini Hash Table
# ============================================================

def simple_hash(key, num_slots):
    """
    A simple hash function: sum the character codes of key,
    then mod by num_slots to fit it into the array.
    """
    # TODO: Step 1: Loop over each character in key
    # Step 2: Add up ord(char) for every character into a running total
    # Step 3: Return total % num_slots
    total = 0
    for char in key:
        total += ord(char)
    return total % num_slots


class MiniHashTable:
    """
    A simplified hash table built on a plain Python list.
    Collisions are handled via chaining: each slot holds a list of
    (key, value) pairs.
    """

    def __init__(self, num_slots):
        self.num_slots = num_slots
        # Each slot starts as an empty list (chain) for collision resolution
        self.slots = [[] for _ in range(num_slots)]
        self.num_items = 0

    def insert(self, key, value):
        """
        Insert key/value into the table using simple_hash to find the slot.
        If key already exists in that slot's chain, update its value.
        Otherwise, append (key, value) to the chain and increase num_items.
        """
        # TODO: Step 1: Find the slot index using simple_hash(key, self.num_slots)
        # Step 2: Loop through self.slots[index] looking for an existing pair with this key
        # Step 3: If found, update its value; if not found, append (key, value)
        # Step 4: If this was a brand new key, increment self.num_items
        index = simple_hash(key, self.num_slots)
        chain = self.slots[index]

        for i, (existing_key, existing_value) in enumerate(chain):
            if existing_key == key:
                chain[i] = (key, value)
                return
        chain.append((key, value))
        self.num_items += 1
        pass

    def get(self, key):
        """
        Retrieve the value associated with key, or None if not found.
        """
        # TODO: Step 1: Find the slot index using simple_hash(key, self.num_slots)
        # Step 2: Search self.slots[index] for a pair matching key
        # Step 3: Return the value if found, otherwise return None
        index = simple_hash(key, self.num_slots)
        chain = self.slots[index]
        for existing_key, existing_value in chain:
            if existing_key == key:
                return existing_value
>>>>>>> 0408890cebd9d35c77241e995fa950baec168538
        return None
    if root.value == target:
        return root
    left_result = dfs_search(root.left, target)
    if left_result is not None:
        return left_result

<<<<<<< HEAD
    return dfs_search(root.right, target)
=======
    def load_factor(self):
        """
        Return the current load factor: num_items / num_slots.
        """
        # TODO: Step 1: Divide self.num_items by self.num_slots
        # Step 2: Return the result
        return self.num_items / self.num_slots
>>>>>>> 0408890cebd9d35c77241e995fa950baec168538


def bfs_search(root, target):
    """
    Breadth-first search: use a queue (deque) to explore level by level
    and return the FIRST node whose value == target found at the
    shallowest depth. Return None if not found.
    """
    queue = deque([root]) if root is not None else deque()  # starter queue
    # TODO: while the queue is not empty, popleft the current node
    # TODO: if current.value == target, return current
    # TODO: otherwise append current.left and current.right (if they exist) to the queue
    while queue:
        current = queue.popleft()
        if current.value == target:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
    return None


# ---------------------------------------------------------------------------
# PART 3: Mini Huffman coding
# ---------------------------------------------------------------------------

class HuffmanNode:
    """A node in the Huffman tree. Leaf nodes hold a character; internal
    nodes hold only a combined frequency and two children."""

    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

    def __lt__(self, other):
        # Needed so heapq can order HuffmanNode objects by frequency.
        return self.freq < other.freq


def count_frequencies(text):
    """
    Count how many times each character appears in text.
    Return a dict like {'a': 3, 'b': 1, ...}.
    """
<<<<<<< HEAD
    freq_dict = {}
    # TODO: loop over every character in text and update freq_dict counts
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return freq_dict
=======
    # TODO: Step 1: Create a list of num_slots empty lists (the chains)
    # Step 2: Loop through each key in keys
    #   - Compute the slot index using hash_func(key, num_slots)
    #   - If that slot already has 1+ items in it, count that as a collision
    #   - Append the key to that slot's chain
    # Step 3: After the loop, find the longest chain length across all slots
    # Step 4: Return (total_collisions, longest_chain_length)
    chains = [[] for _ in range(num_slots)]
    total_collisions = 0

    for key in keys:
        index = hash_func(key, num_slots)
        if len(chains[index]) >= 1:
            total_collisions += 1
        chains[index].append(key)
    longest_chain_length = 0
    for chain in chains:
        if len(chain) > longest_chain_length:
            longest_chain_length = len(chain)

    return total_collisions, longest_chain_length
>>>>>>> 0408890cebd9d35c77241e995fa950baec168538


def build_huffman_tree(freq_dict):
    """
    Build a Huffman tree from a frequency dictionary using the greedy
    approach with a heapq priority queue:
        1. Push a HuffmanNode(freq, char) for every character.
        2. While more than one node remains in the heap:
             - pop the two lowest-frequency nodes
             - combine them into a new internal node
               (freq = sum of the two, char=None, left=one, right=other)
             - push the new node back onto the heap
        3. Return the single remaining node (the tree root).
    """
    heap = []
    heapq.heapify(heap)  # placeholder - keeps heap a valid heap structure
    # TODO: push a HuffmanNode(freq, char) onto heap for every char in freq_dict
    #       using heapq.heappush(heap, node)
    # TODO: while len(heap) > 1: heapq.heappop the two smallest nodes,
    #       combine them into a new HuffmanNode, and heapq.heappush it back
    # TODO: return the single remaining node (heap[0]), or None if freq_dict is empty
    for char, freq in freq_dict.items():
        heapq.heappush(heap, HuffmanNode(freq, char))

    if len(heap) == 1:
        only = heapq.heappop(heap)
        return HuffmanNode(only.freq, left = only)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(left.freq + right.freq, left = left, right = right)
        heapq.heappush(heap, merged)
    return heap[0]


def generate_codes(root):
    """
    Walk the Huffman tree (left = '0', right = '1') to build a code table.
    Return a dict like {'a': '01', 'b': '1', ...}.
    Hint: a recursive helper that carries the 'path so far' as a string
    works well here.
    """
    codes = {}
    # TODO: write a recursive helper(node, path) that:
    #         - if node.char is not None, records codes[node.char] = path (or '0' if path is empty)
    #         - otherwise recurses into node.left with path + '0' and node.right with path + '1'
    # TODO: call the helper starting at root with an empty path, then return codes
    def helper(node, path):
        if node.char is not None:
            codes[node.char] = path if path else "0"
            return
        helper(node.left, path + "0")
        helper(node.right, path + "1")
    helper(root, "")
    return codes


def huffman_encode(text, codes):
    """
    Encode text into a single bitstring using the code table produced by
    generate_codes.
    """
    encoded = ""
    # TODO: for each character in text, look up its code in codes and append it to encoded
    for char in text:
        encoded += codes[char]
    return encoded


def huffman_decode(encoded, root):
    """
    Decode a bitstring by walking the Huffman tree one bit at a time,
    starting over at the root each time a leaf is reached ('read like a
    tape').
    """
    decoded = ""
    # TODO: walk the tree one bit at a time starting from root:
    #         - bit '0' moves to current.left, bit '1' moves to current.right
    #         - when a leaf (current.char is not None) is reached, append
    #           current.char to decoded and reset current back to root
    current = root
    for bit in encoded:
        if bit == "0":
            current = current.left
        else:
            current = current.right
        if current.char is not None:
            decoded += current.char
            current = root

    return decoded


# ---------------------------------------------------------------------------
# Entry point - deterministic, hardcoded scaffolding (no file I/O, no random)
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # ---- Part 1 ----
    print("Part 1: Directory traversal")
    sample_root = build_sample_directory()

    print("BFS order:")
    print_names_bfs(sample_root)

    print("DFS order:")
    print_names_dfs(sample_root)

    # TODO: add a comment explaining, in your own words, why BFS and DFS
    # visit the same nodes in a different order, and why no 'searched' set
    # was needed here (trees have no cycles, unlike Chapter 6's graph).

    # ---- Part 2 ----
    print("Part 2: DFS vs BFS shortest path counterexample")
    mango_root = build_mango_tree()

    dfs_result = dfs_search(mango_root, "target")
    bfs_result = bfs_search(mango_root, "target")

    print("DFS found target node:")
    print(dfs_result)
    print("BFS found target node:")
    print(bfs_result)

    # ---- Part 3 ----
    print("Part 3: Mini Huffman coding")
    sample_text = "huffman coding builds trees from frequencies"

    freqs = count_frequencies(sample_text)
    print("Character frequencies:")
    print(freqs)

    huffman_root = build_huffman_tree(freqs)
    codes = generate_codes(huffman_root)
    print("Code table:")
    print(codes)

    encoded_text = huffman_encode(sample_text, codes)
    print("Encoded bitstring:")
    print(encoded_text)

    decoded_text = huffman_decode(encoded_text, huffman_root)
    print("Decoded text:")
    print(decoded_text)

    print("Round trip matches original:")
    print(decoded_text == sample_text)

    # Reflection: compare compressed size to fixed-width baseline
    fixed_width_bits = 8 * len(sample_text)
    compressed_bits = len(encoded_text)
    print("Fixed-width bit count (8 times length of string):")
    print(fixed_width_bits)
    print("Compressed bit count:")
    print(compressed_bits)

    # TODO: add a comment explaining why more frequent characters end up
    # with shorter Huffman codes, and what that means for the total bit count.
