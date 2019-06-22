import random

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if ints:
        ints_len = len(ints)
        if ints_len < 2:
            return ints[0], ints[0]
        i = 0
        min = max = ints[0]
        while i + 1 < ints_len:
            if max < ints[i + 1]:
                max = ints[i + 1]
            elif min > ints[i + 1]:
                min = ints[i + 1]
            i += 1
        return min, max
    print('The list should not be empty.')
    return None

def main():
    ## Example Test Case of Ten Integers
    l = [i for i in range(0, 10)]  # a list containing 0 - 9
    random.shuffle(l)
    print("Pass" if get_min_max(l) == (0, 9) else "Fail")
    # edge cases
    l = []
    print("Pass" if get_min_max(l) is None else "Fail")
    l = [5]
    print("Pass" if get_min_max(l) == (5, 5) else "Fail")

if __name__ == '__main__':
    main()
