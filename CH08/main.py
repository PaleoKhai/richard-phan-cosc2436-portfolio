"""
Lab: "Out of Balance" -- Binary Search Trees and Why Shape Matters

Part 1: Build a working BST (insert, search, height, in_order)
Part 2: Watch a BST degenerate into a linked list on sorted input
Part 3: Rotate to fix it (single rotations you implement, double
        rotations provided pre-written, then avl_insert)

Determinism note: every value in this file is hardcoded. No randomness,
no file I/O -- so results (heights, comparison counts) are always the
same every time you run this file.
"""


class BSTNode:
    """A single node in a binary search tree."""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# ---------------------------------------------------------------------------
# PART 1: Build a working BST
# ---------------------------------------------------------------------------

def insert(root, value):
    """
    Recursively insert `value` into the BST rooted at `root`.
    Returns the (possibly new) root of this subtree.

    Reminder: this is the SAME recursion shape as the Chapter 3 recursion
    lab -- base case is an empty spot (None), recursive case is
    "go left or go right" depending on the comparison.
    """
    # TODO: Base case - if root is None, create and return BSTNode(value)
    # TODO: Recursive case:
    #       if value < root.value -> root.left = insert(root.left, value)
    #       else                  -> root.right = insert(root.right, value)
    # TODO: return root
    if root is None:
        return BSTNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root  # placeholder so the file runs before this is implemented


def search(root, value):
    """
    Search for `value` starting at `root`.
    Returns a tuple: (found, comparisons)

    NOTE: fill in a short comment below explaining, in your own words,
    how this is the same idea as Chapter 1's binary search -- except we
    are walking left/right CHILD POINTERS instead of jumping to array
    indices with math.
    # TODO: write your one or two sentence connection here
    """
    comparisons = 0
    # TODO: walk down the tree starting at `root`
    #   - every time you look at a node, add 1 to `comparisons`
    #   - if the current node is None, the value is not in the tree ->
    #     return (False, comparisons)
    #   - if node.value == value, return (True, comparisons)
    #   - if value < node.value, move to node.left, else move to node.right
    node = root
    while node is not None:
        comparisons += 1
        if node.value == value:
            return (True, comparisons)
        elif value < node.value:
            node = node.left
        else:
            node = node.right
    return (False, comparisons)  # placeholder


def height(root):
    """
    Return the height of the tree rooted at `root`.
    An empty tree (None) has height 0. A single node has height 1.
    """
    # TODO: base case - if root is None, return 0
    # TODO: recursive case - return 1 + max(height(root.left), height(root.right))
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))  # placeholder


def in_order(root, result=None):
    """
    In-order traversal (left, node, right). Returns a list of values in
    sorted order. This reuses the DFS pattern from the Chapter 7 lab.
    """
    if result is None:
        result = []
    # TODO: if root is None, just return result unchanged (base case)
    # TODO: otherwise recurse left, append root.value, then recurse right
    if root is None:
        return result
    in_order(root.left, result)
    result.append(root.value)
    in_order(root.right, result)
    return result  # placeholder


# ---------------------------------------------------------------------------
# PART 2: Watch it degenerate (constructed counterexample)
# ---------------------------------------------------------------------------

def compare_bst_shapes():
    """
    Build TWO trees from the SAME twelve values:
      - Tree A: values inserted in the mixed order given below
      - Tree B: the SAME values, inserted in already-sorted order

    Print for both trees:
      - height
      - in-order traversal (these should come out IDENTICAL -- that's the point)
      - comparisons needed to search for the LARGEST value

    Tree B should end up looking like a linked list wearing a tree costume.
    """
    mixed_order = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 65]
    sorted_order = sorted(mixed_order)
    largest_value = max(mixed_order)

    tree_a = None
    tree_b = None
    # TODO: build tree_a by inserting every value in mixed_order (in that order)
    # TODO: build tree_b by inserting every value in sorted_order (in that order)

    # TODO: compute height(tree_a) and height(tree_b) and print them
    # TODO: compute in_order(tree_a) and in_order(tree_b) and print them
    #       (they should be identical sorted lists)
    # TODO: search for `largest_value` in tree_a and in tree_b, and print
    #       the comparisons count for each search
    for value in mixed_order:
        tree_a = insert(tree_a, value)

    for value in sorted_order:
        tree_b = insert(tree_b, value)

    height_a = height(tree_a)
    height_b = height(tree_b)
    in_order_a = in_order(tree_a)
    in_order_b = in_order(tree_b)
    found_a, comparisons_a = search(tree_a, largest_value)
    found_b, comparisons_b = search(tree_b, largest_value)

    print("Tree A height:", 0)
    print("Tree B height:", 0)
    print("Tree A in-order:", [])
    print("Tree B in-order:", [])
    print("Tree A search comparisons for largest value:", 0)
    print("Tree B search comparisons for largest value:", 0)

    return tree_a, tree_b

    # TODO (in your own words, as a comment): explain why sorted input is
    # the worst possible input for a plain BST, and name the structure
    # Tree B has effectively turned into. (Hint: connects back to the
    # array-vs-linked-list table from Chapter 2.)


# ---------------------------------------------------------------------------
# PART 3: Rotate to fix it
# ---------------------------------------------------------------------------

def balance_factor(node):
    """
    Return height(left subtree) - height(right subtree) for `node`.
    A balanced AVL node has a balance factor of -1, 0, or 1.
    """
    # TODO: handle node is None -> return 0
    # TODO: return height(node.left) - height(node.right)
    if node is None:
        return 0
    return height(node.left) - height(node.right)  # placeholder


def rotate_right(node):
    """
    Single RIGHT rotation (fixes the LL case).

    TODO: draw your own before/after diagram here as a comment, e.g.:
        Before:                After:
              node                pivot
             /                   /    \
          pivot                 A     node
         /    \                        /
        A      B                      B
    """
    # TODO: let pivot = node.left
    # TODO: node.left = pivot.right
    # TODO: pivot.right = node
    # TODO: return pivot (the new subtree root)
    pivot = node.left
    node.left = pivot.right
    pivot.right = node
    return pivot  # placeholder


def rotate_left(node):
    """
    Single LEFT rotation (fixes the RR case).

    TODO: draw your own before/after diagram here as a comment, e.g.:
        Before:            After:
          node                pivot
             \               /    \
             pivot          node   B
             /   \             \
            A     B              A
    """
    # TODO: let pivot = node.right
    # TODO: node.right = pivot.left
    # TODO: pivot.left = node
    # TODO: return pivot (the new subtree root)
    pivot = node.right
    node.right = pivot.left
    pivot.left = node
    return pivot  # placeholder


def rotate_left_right(node):
    """
    Double rotation for the LR case (pre-written for you):
    rotate node.left LEFT first, then rotate node RIGHT.
    """
    node.left = rotate_left(node.left)
    return rotate_right(node)


def rotate_right_left(node):
    """
    Double rotation for the RL case (pre-written for you):
    rotate node.right RIGHT first, then rotate node LEFT.
    """
    node.right = rotate_right(node.right)
    return rotate_left(node)


def avl_insert(root, value):
    """
    Insert `value` like a normal BST insert, then rebalance on the way
    back up using rotations so the tree's height stays close to log2(n).

    Scope for this lab: implement the LL and RR (single rotation) cases
    yourself; the LR and RL (double rotation) cases are already wired up
    above using rotate_left_right / rotate_right_left.
    """
    # TODO: base case - if root is None, return BSTNode(value)
    # TODO: recurse - if value < root.value: root.left = avl_insert(root.left, value)
    #                 else: root.right = avl_insert(root.right, value)
    # TODO: balance = balance_factor(root)
    # TODO: LL case: balance > 1 and value < root.left.value -> return rotate_right(root)
    # TODO: RR case: balance < -1 and value > root.right.value -> return rotate_left(root)
    # TODO: LR case: balance > 1 and value > root.left.value -> return rotate_left_right(root)
    # TODO: RL case: balance < -1 and value < root.right.value -> return rotate_right_left(root)
    # TODO: otherwise return root unchanged (already balanced at this node)
    if root is None:
        return BSTNode(value)

    if value < root.value:
        root.left = avl_insert(root.left, value)
    else:
        root.right = avl_insert(root.right, value)

    balance = balance_factor(root)

    if balance > 1 and value < root.left.value:
        return rotate_right(root)
    if balance < -1 and value >= root.right.value:
        return rotate_left(root)
    if balance > 1 and value >= root.left.value:
        return rotate_left_right(root)
    if balance < -1 and value < root.right.value:
        return rotate_right_left(root)
    return root  # placeholder


def avl_demo():
    """
    Re-insert the SAME sorted values from Part 2 (the worst case for a
    plain BST) but this time using avl_insert instead of insert.
    Print the resulting height and compare it to Part 2's Tree B height.
    """
    sorted_order = sorted([50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 65])
    avl_root = None
    for value in sorted_order:
        avl_root = avl_insert(avl_root, value)
    print("AVL tree height after sorted insertion:", height(avl_root))


# ---------------------------------------------------------------------------
# REFLECTION
# ---------------------------------------------------------------------------

def print_reflection():
    """
    Fill in the table below as comments, comparing search/insert cost for:
      - a sorted array
      - a linked list
      - a balanced BST
    Then explain, in a sentence or two, why a database stores its indexes
    as a tree rather than a sorted array.
    """
    # TODO: Sorted array   - search: ???   insert: ???
    # TODO: Linked list    - search: ???   insert: ???
    # TODO: Balanced BST   - search: ???   insert: ???
    # TODO: Why does a database use a tree index instead of a sorted array?
    print("See comments above for the reflection table.")


def main():
    print("=== PART 1: Basic BST operations ===")
    root = None
    starter_values = [50, 30, 70, 20, 40]
    for v in starter_values:
        root = insert(root, v)
    print(in_order(root))
    print(height(root))
    found, comparisons = search(root, 40)
    print(found)
    print(comparisons)

    print("=== PART 2: Same values, different insertion order ===")
    compare_bst_shapes()

    print("=== PART 3: AVL rotations fix the shape ===")
    avl_demo()

    print("=== REFLECTION ===")
    print_reflection()


if __name__ == "__main__":
    main()
