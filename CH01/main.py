import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


# --- Exercise 1: linear search ---
def linear_search(arr, item):
    """
    Search for `item` in `arr` one element at a time.
    Returns a tuple: (index_found_or_None, number_of_steps_taken)
    """
    # TODO: Step 1 - initialize a steps counter to 0
    steps = 0
    for index, value in enumerate(arr):
        steps += 1
        if value == item:
            return index, steps
    return None, steps
    # TODO: Step 2 - loop through each element of arr, keeping track of its index
    # TODO: Step 3 - each time you check an element, increment the steps counter
    # TODO: Step 4 - if the current element equals item, return (index, steps)
    # TODO: Step 5 - if the loop finishes without finding item, return (None, steps)
    return None, 0


# --- Exercise 2: binary search ---
def binary_search(arr, item):
    """
    Search for `item` in a SORTED `arr` by repeatedly checking the middle
    element and eliminating half the remaining items.
    Returns a tuple: (index_found_or_None, number_of_steps_taken)
    """
    # TODO: Step 1 - set low = 0 and high = len(arr) - 1
    # TODO: Step 2 - initialize a steps counter to 0
    # TODO: Step 3 - while low <= high:
    #         - increment steps
    #         - compute mid = (low + high) // 2
    #         - guess = arr[mid]
    #         - if guess == item: return (mid, steps)
    #         - elif guess > item: high = mid - 1
    #         - else: low = mid + 1
    # TODO: Step 4 - if the loop ends without finding item, return (None, steps)
    low = 0
    high = len(arr) - 1
    steps = 0
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return mid, steps
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None, steps


# --- Exercise 3: confirm step counts from the book's exercises ---
def max_steps_binary_search(n):
    """
    Build a sorted list of size n (values 0..n-1) and search for an item
    that is NOT present (worst case). Return only the number of steps taken.
    """
    # TODO: Step 1 - build a sorted list of n elements: list(range(n))
    # TODO: Step 2 - call binary_search on that list for an item not present (e.g. -1)
    # TODO: Step 3 - return just the steps count (not the index)
    arr = list(range(n))
    _, steps = binary_search(arr, -1)
    return steps


if __name__ == "__main__":
    # Hardcoded sample sorted list for basic testing (Exercises 1 & 2)
    sample_sorted_list = [2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 72, 89, 95]

    # TODO: call linear_search on sample_sorted_list for item 67, store the
    # returned (index, steps), and print both values
    found_index_linear, steps_linear = linear_search(sample_sorted_list, 67)
    print(found_index_linear)
    print(steps_linear)

    # TODO: call binary_search on sample_sorted_list for item 67, store the
    # returned (index, steps), and print both values
    found_index_binary, steps_binary = binary_search(sample_sorted_list, 67)
    print(found_index_binary)
    print(steps_binary)

    # --- Exercise 3: confirm step counts from the book's exercises ---
    book_sizes = (128, 256, 1024, 2048)
    for n in book_sizes:
        # TODO: call max_steps_binary_search(n) and store the result in `steps`
        steps = max_steps_binary_search(n)
        naive_formula = math.ceil(math.log2(n)) + 1
        print(n)
        print(steps)
        print(naive_formula)

    # --- Exercise 4: empirical growth, linear vs. binary ---
    sizes = [10, 100, 1000, 10000, 100000, 1000000]
    linear_counts = []
    binary_counts = []

    for n in sizes:
        arr = list(range(n))
        _, l_steps = linear_search(arr, -1)
        _, b_steps = binary_search(arr, -1)
        linear_counts.append(l_steps)
        binary_counts.append(b_steps)
        print(n)
        print(l_steps)
        print(b_steps)
        # TODO: build a sorted list of size n using list(range(n))
        # TODO: search for an item not in the list (e.g. -1) using linear_search
        # TODO: search for an item not in the list (e.g. -1) using binary_search
        # TODO: append each step count to linear_counts and binary_counts
        # TODO: print n, the linear step count, and the binary step count


    # Plot comparisons vs n for both algorithms
    plt.figure(figsize=(8, 5))
    plt.plot(sizes, linear_counts, marker="o", label="Linear search: O(n)")
    plt.plot(sizes, binary_counts, marker="o", label="Binary search: O(log n)")
    # TODO: plot sizes vs linear_counts with marker="o" and label "Linear search: O(n)"
    # TODO: plot sizes vs binary_counts with marker="o" and label "Binary search: O(log n)"
    plt.xscale("log")
    plt.xlabel("List size (n)")
    plt.ylabel("Comparisons (worst case)")
    plt.title("Growth of linear vs. binary search")
    plt.legend()
    plt.tight_layout()
    plt.close()

    # --- Exercise 5 (Bonus): verify step counts for 1024 vs 2048 names ---
    # TODO: call max_steps_binary_search(1024) and store the result
    steps_1024 = max_steps_binary_search(1024)
    # TODO: call max_steps_binary_search(2048) and store the result
    steps_2048 = max_steps_binary_search(2048)
    print(steps_1024)
    print(steps_2048)
