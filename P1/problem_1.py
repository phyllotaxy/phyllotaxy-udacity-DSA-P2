def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        print('The number must be non-negative.')
        return None
    if number < 1:
        return 0
    # Probe the upper bound of the square root as fast as possible using factorial.
    square_root = 1
    while square_root ** 2 < number:
        # keep updating the lower bound
        lower_bound = square_root
        square_root *= square_root + 1
    # Upper bound found. Use binary search to find the square root.
    upper_bound = square_root
    while True:
        if square_root ** 2 <= number < (square_root + 1) ** 2:
            # Square root found.
            return square_root
        if number < square_root ** 2:
            # approximation too big
            upper_bound = square_root
        else:
            # approximation too small
            lower_bound = square_root
        square_root = (lower_bound + upper_bound) // 2

# test cases
def main():
    # edge cases
    print("Pass" if  (sqrt(0) == 0) else "Fail")
    sqrt(-1)
    #print('Pass' if (sqrt(123456789) == 11111) else "Fail")
    # normal cases
    print("Pass" if  (sqrt(9) == 3) else "Fail")
    print("Pass" if  (sqrt(16) == 4) else "Fail")
    print("Pass" if  (sqrt(1) == 1) else "Fail")
    print("Pass" if  (sqrt(27) == 5) else "Fail")

if __name__ == '__main__':
    main()
