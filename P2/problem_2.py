def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if input_list:
        if len(input_list) == 1:
            if input_list[0] == number:
                return 0
            return -1
        # Find the index of the smallest element, i.e., the first element of the
        # array before rotation.
        lower_bound, upper_bound = 0, len(input_list) - 1
        i = (lower_bound + upper_bound) // 2
        while True:
            if input_list[i] > input_list[i + 1]:
                # Index found.
                i += 1
                break
            if input_list[i] > input_list[upper_bound]:
                # The smallest element is on the right.
                lower_bound = i
            elif input_list[i] < input_list[lower_bound]:
                # The smallest element is on the left.
                upper_bound = i
            i = (lower_bound + upper_bound) // 2
        # i is now the index of the smallest element.
        # Find the number
        if number >= input_list[0]:
            # The number is in the bigger list.
            return binary_search(input_list, 0, i - 1, number)
        # The number is in the smaller list.
        return binary_search(input_list, i, len(input_list) - 1, number)
    return -1

def binary_search(sorted_arr, lo, hi, x):
    """
    Try to find an item x in a subarray of a sorted array using binary search.
    Return -1 when not found.

    Args:
        input_list(array), lo(non-negative int), hi(non-negative int):
        hi and lo together specify the subarray, x: the item to be searched
    Returns:
        int: index or -1
    """
    i = (lo + hi) // 2
    while lo <= hi:
        if sorted_arr[i] == x:
            # Element found.
            return i
        if sorted_arr[i] < x:
            # approximation too small
            lo = i + 1
        else:
            # approximation too big
            hi = i - 1
        i = (hi + lo) // 2
    return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

# test cases
def main():
    # edge cases
    test_function([[], 1])
    test_function([[9], 9])
    test_function([[9], 7])
    test_function([[9, 8], 8])
    test_function([[9, 8], 7])
    # normal cases
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 8])
    test_function([[6, 7, 8, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 10])

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

if __name__ == '__main__':
    main()
