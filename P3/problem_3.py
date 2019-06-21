def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # Check if the input list is valid.
    if len(input_list) < 2:
        print('The list should have at least two numbers.')
        return
    for elem in input_list:
        # All elements must be integers.
        if not isinstance(elem, int):
            raise TypeError('All elements must be integers.')
        # Each value should be in the range 0 - 9.
        if not 0 <= elem < 10:
            raise ValueError('Every element should be a positive single-digit integer.')
    # Sort the list using merge-sort.
    reverse_merge_sort(input_list)
    # Divide the sorted list into 2 lists.
    left, right = distribute(input_list)
    # Convert the lists into numbers.
    return int(''.join(str(e) for e in left)), int(''.join(str(e) for e in right))

def distribute(arr):
    left, right = [], []
    for index, value in enumerate(arr):
        if index % 2 == 0:
            left.append(value)
        else:
            right.append(value)
    return left, right

def reverse_merge_sort(arr):
    # divede
    length = len(arr)
    if length < 2:
        return
    mid = length // 2
    left = arr[0:mid]
    right = arr[mid:length]
    # conquer
    reverse_merge_sort(left)
    reverse_merge_sort(right)
    # combine
    combine(left, right, arr)

def combine(l, r, a):
    finger_1 = finger_2 = 0
    while finger_1 + finger_2 < len(a):
        if finger_2 >= len(r) or (finger_1 < len(l) and l[finger_1] >= r[finger_2]):
            a[finger_1 + finger_2] = l[finger_1]
            finger_1 += 1
        else:
            a[finger_1 + finger_2] = r[finger_2]
            finger_2 += 1

def main():
    test_cases = []
    test_case_0 = [[1, 2, 3, 4, 5], [542, 31]]
    test_cases.append(test_case_0)
    test_case_1 = [[4, 6, 2, 5, 9, 8], [964, 852]]
    test_cases.append(test_case_1)
    # edge cases
    test_case_3 = [[], None]
    test_cases.append(test_case_3)
    test_case_4 = [[7], None]
    test_cases.append(test_case_4)
    for test_case in test_cases:
        test_function(test_case)

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if len(test_case[0]) < 2:
        if output == None:
            print('Pass')
        else:
            print('Fail')
    else:
        if sum(output) == sum(solution):
            print("Pass")
        else:
            print("Fail")

if __name__ == '__main__':
    main()
