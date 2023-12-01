"""
Author: Nicholas Butzke
"""


def linear_sort(arr):
    """
    Sorts a list of integers 1 through n in O(n) time
    """
    n = len(arr)
    count = [0] * (n + 1)

    # Count the frequency of unique elements
    for ele in arr:
        count[ele] += 1

    # Compute offset
    for i in range(1, n + 1):
        count[i] += count[i - 1]

    # Place elements based off of the offset
    sorted_arr = [0] * n
    for ele in arr[::-1]:
        sorted_arr[count[ele] - 1] = ele
        count[ele] -= 1
    return sorted_arr
