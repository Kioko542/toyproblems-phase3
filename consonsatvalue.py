def solve(word):
    # Initialize an empty list to store the values of consonant substrings
    consonant_values = []

    # Split the word into substrings separated by vowels
    substrings = word.split('aeiou')

    # Loop through each consonant substring
    for substring in substrings:
        # Calculate the value of the consonant substring
        value = 0
        for char in substring:
            # Map each character to its numeric value ('a' is 1, 'b' is 2, and so on)
            value += ord(char) - ord('a') + 1
        
        # Add the calculated value to the list
        consonant_values.append(value)

    # Find and return the maximum value among consonant substrings
    max_value = max(consonant_values, default=0)
    return max_value

# Examples
print(solve("zodiacs"))    # Output: 26
print(solve("strength"))   # Output: 57
