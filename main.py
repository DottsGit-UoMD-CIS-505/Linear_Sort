"""
Author: Nicholas Butzke
"""
from linear_sort import linear_sort

arr_1 = [2, 5, 1, 4, 3]
arr_2 = [3, 1, 5, 4, 2]
arr_3 = [5, 4, 3, 2, 1]

input_arrs = [arr_1, arr_2, arr_3]

solution_arr = [1, 2, 3, 4, 5]

for arr in input_arrs:
    output_arr = linear_sort(arr)
    print(f"Final output: {output_arr}")
    print(f"Passed: {output_arr == solution_arr}")
