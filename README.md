# toyproblems-phase3


This repository contains solutions to three Python coding challenges. Each challenge is designed to test and improve your problem-solving skills using Python programming. The challenges cover different aspects of programming, including time conversion, conditional logic, and string manipulation.
Challenge 1: Converting 12-hour time to 24-hour time
Problem Statement:

Write a function that takes an hour (1 to 12), minute (0 to 59), and period ("am" or "pm") as input and returns a four-digit string representing the time in 24-hour format.
Usage:

python

convert_to_24_hour(8, 30, "am")  # Output: "0830"
convert_to_24_hour(8, 30, "pm")  # Output: "2030"

Challenge 2: Two numbers are positive
Problem Statement:

Write a function that takes three integers as arguments and returns True if exactly two of the three integers are positive numbers (greater than zero), and False otherwise.
Usage:

python

two_positive(2, 4, -3)   # Output: True
two_positive(-4, 6, 8)   # Output: True
two_positive(4, -6, 9)   # Output: True
two_positive(-4, 6, 0)   # Output: False
two_positive(4, 6, 10)   # Output: False
two_positive(-14, -3, -4)  # Output: False

Challenge 3: Consonant value
Problem Statement:

Write a function that takes a lowercase string containing only alphabetic characters and no spaces. The function should return the highest value of consonant substrings, where consonants are any letters except "aeiou."
Usage:

python

solve("zodiacs")     # Output: 26
solve("strength")    # Output: 57

Feel free to explore, modify, and test the solutions. Happy coding!
