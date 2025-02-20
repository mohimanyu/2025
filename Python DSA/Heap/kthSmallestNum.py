from Heap import MaxHeap


def find_kth_smallest(nums, k):
    my_heap = MaxHeap()

    for num in nums[:k]:
        my_heap.insert(num)

    for num in nums[k:]:
        if num < my_heap.heap[0]:
            my_heap.remove()
            my_heap.insert(num)

    return my_heap.heap[0]


# Test cases
nums = [
    [3, 2, 1, 5, 6, 4],
    [6, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 6],
    [3, 2, 3, 1, 2, 4, 5, 5, 6],
]
ks = [2, 3, 4, 7]
expected_outputs = [2, 3, 4, 5]

for i in range(len(nums)):
    print(f"Test case {i+1}...")
    print(f"Input: {nums[i]} with k = {ks[i]}")
    result = find_kth_smallest(nums[i], ks[i])
    print(f"Output: {result}")
    print(f"Expected output: {expected_outputs[i]}")
    print(f"Test passed: {result == expected_outputs[i]}")
    print("---------------------------------------")


"""
    EXPECTED OUTPUT:
    ----------------
    Test case 1...
    Input: [3, 2, 1, 5, 6, 4] with k = 2
    Output: 2
    Expected output: 2
    Test passed: True
    ---------------------------------------
    Test case 2...
    Input: [6, 5, 4, 3, 2, 1] with k = 3
    Output: 3
    Expected output: 3
    Test passed: True
    ---------------------------------------
    Test case 3...
    Input: [1, 2, 3, 4, 5, 6] with k = 4
    Output: 4
    Expected output: 4
    Test passed: True
    ---------------------------------------
    Test case 4...
    Input: [3, 2, 3, 1, 2, 4, 5, 5, 6] with k = 7
    Output: 5
    Expected output: 5
    Test passed: True
    ---------------------------------------

"""
