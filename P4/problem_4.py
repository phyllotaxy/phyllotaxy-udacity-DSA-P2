def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if len(input_list) < 2:
        return input_list
    # As we already know the list consists of only these 3 numbers, we could choose 1 as the pivot.
    pivot = 1
    # The following invariants are maintained:
    # 1. All indexes < left have value strictly less that 1 (i.e., 0).
    # 2. All indexes > right have values strictly greater than 1 (i.e., 2).
    left, right = 0, len(input_list) - 1
    i = left
    # Since:
    # 1. Either i increases or right decreases.
    # 2. Once i > right, the while loop terminates
    # the algorithm is one pass.
    while i <= right:
        if input_list[i] <= pivot:
            if input_list[i] < pivot:
                # If input_list[i] < 1, we swap the value at position i and left.
                input_list[i], input_list[left] = input_list[left], input_list[i]
                # left then points to the next location. Invariant 1 is maintained.
                left += 1
            # If input_list[i] = 1, we do nothing except increment i.
            i += 1
        else:
            # If input_list[i] > 1, we swap the value at position i and right.
            # right then points to the previous location. Invariant 2 is maintained.
            # Note that i should not be changed here.
            input_list[i], input_list[right] = input_list[right], input_list[i]
            right -= 1
        # If we've encountered a value = 1, do nothing and advance i.
    return input_list

def main():
    # normal cases
    test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
    test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
    test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
    # edge cases
    test_function([])
    test_function([1])
    test_function([1, 0])
    test_function([0, 1])
    test_function([2, 0])
    test_function([2, 1])

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

if __name__ == '__main__':
    main()
