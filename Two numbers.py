def two_positive(a, b, c):
    # Check if  two out of three numbers are positive
    positive_count = (a > 0) + (b > 0) + (c > 0)
    return positive_count == 2

# Examples
print(two_positive(2, 4, -3))    # Output: True
print(two_positive(-4, 6, 8))    # Output: True
print(two_positive(-4, 6, 0))    # Output: False
print(two_positive(4, 6, 10))    # Output: False
