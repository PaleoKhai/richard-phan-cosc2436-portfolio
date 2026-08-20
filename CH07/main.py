"""
Lab: Rooted & Compressed - Tree Traversal and Huffman Coding
COSC 2436 - Chapter 7

This starter code scaffolds three parts:
  Part 1: BFS vs DFS directory traversal
  Part 2: DFS vs BFS shortest-path counterexample (mango-seller style)
  Part 3: Mini Huffman coding (build tree, encode, decode)
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
    file1 = DirNode("notes.txt")
    file2 = DirNode("todo.txt")
    file3 = DirNode("photo.png")
    file4 = DirNode("song.mp3")
    file5 = DirNode("draft.docx")
    file6 = DirNode("index.html")
    file7 = DirNode("style.css")

    docs = DirNode("docs", [file1, file2, file5])
    media = DirNode("media", [file3, file4])
    web = DirNode("web", [file6, file7])

    root = DirNode("root", [docs, media, web])
    return root


def print_names_bfs(start_dir):
    """
    Print every node name in the tree using BREADTH-FIRST traversal.
    """
    queue = deque([start_dir])

    # A tree has no cycles: every node (other than the root) has exactly one
    # parent, so we can never re-encounter the same node while walking down
    # from the root. That's why no 'searched' set is needed here, unlike
    # Chapter 6's graph, where revisiting a node was possible.
    while queue:
        current = queue.popleft()
        print(current.name)
        for child in current.children:
            queue.append(child)


def print_names_dfs(start_dir):
    """
    Print every node name in the tree using DEPTH-FIRST traversal.
    This is RECURSIVE and needs no queue.
    """
    print(start_dir.name)
    for child in start_dir.children:
        print_names_dfs(child)


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
    Builds a small, hardcoded binary tree:
      - 'target' appears 3 levels deep on the LEFT branch
      - 'target' appears 1 level deep on the RIGHT branch
    DFS (which dives left first) will incorrectly return the farther
    target; BFS should correctly return the closer one.
    """
    left_leaf = TreeNode("target")
    left_level2 = TreeNode("L2", left=left_leaf)
    left_level1 = TreeNode("L1", left=left_level2)

    right_leaf = TreeNode("target")

    root = TreeNode("root", left=left_level1, right=right_leaf)
    return root


def dfs_search(root, target):
    """
    Depth-first search: recursively dive down the LEFT branch first,
    then the right, and return the FIRST node whose value == target
    that is found. Return None if not found.
    """
    if root is None:
        return None
    if root.value == target:
        return root

    left_result = dfs_search(root.left, target)
    if left_result is not None:
        return left_result

    return dfs_search(root.right, target)


def bfs_search(root, target):
    """
    Breadth-first search: use a queue (deque) to explore level by level
    and return the FIRST node whose value == target found at the
    shallowest depth. Return None if not found.
    """
    queue = deque([root]) if root is not None else deque()

    while queue:
        current = queue.popleft()
        if current.value == target:
            return current
        if current.left is not None:
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
    freq_dict = {}
    for char in text:
        freq_dict[char] = freq_dict.get(char, 0) + 1
    return freq_dict


def build_huffman_tree(freq_dict):
    """
    Build a Huffman tree from a frequency dictionary using the greedy
    approach with a heapq priority queue.
    """
    heap = []
    for char, freq in freq_dict.items():
        heapq.heappush(heap, HuffmanNode(freq, char))

    if len(heap) == 1:
        only = heapq.heappop(heap)
        return HuffmanNode(only.freq, left=only)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, merged)

    return heap[0] if heap else None


def generate_codes(root):
    """
    Walk the Huffman tree (left = '0', right = '1') to build a code table.
    Return a dict like {'a': '01', 'b': '1', ...}.
    """
    codes = {}

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
    for char in text:
        encoded += codes[char]
    return encoded


def huffman_decode(encoded, root):
    """
    Decode a bitstring by walking the Huffman tree one bit at a time,
    starting over at the root each time a leaf is reached.
    """
    decoded = ""
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
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # ---- Part 1 ----
    print("Part 1: Directory traversal")
    sample_root = build_sample_directory()

    print("BFS order:")
    print_names_bfs(sample_root)

    print("DFS order:")
    print_names_dfs(sample_root)

    # BFS and DFS visit the same nodes but in a different order because BFS
    # uses a FIFO queue (finishing one whole level before moving deeper),
    # while DFS uses recursion to plunge all the way down one branch before
    # backtracking. No 'searched' set is needed for either because a tree
    # has no cycles - every node is reachable by exactly one path from the
    # root, so we can never revisit a node the way we could in Chapter 6's
    # graph.

    # ---- Part 2 ----
    print("Part 2: DFS vs BFS shortest path counterexample")
    mango_root = build_mango_tree()

    dfs_result = dfs_search(mango_root, "target")
    bfs_result = bfs_search(mango_root, "target")

    print("DFS found target node:")
    print(dfs_result.value if dfs_result else None)
    print("BFS found target node:")
    print(bfs_result.value if bfs_result else None)

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

    # More frequent characters end up with shorter Huffman codes because the
    # greedy build always merges the two LOWEST-frequency nodes first, which
    # pushes rare characters deep into the tree early and leaves common
    # characters to be merged in later, closer to the root. Since code
    # length equals depth in the tree, common characters get short codes and
    # rare characters get long codes - so the total bit count for the whole
    # message ends up lower than a fixed-width encoding, where every
    # character costs the same 8 bits regardless of how often it appears.
