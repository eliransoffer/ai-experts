# Exercise:
# Write a function count_vowels that takes a single string as an argument
# and returns the number of vowels (a, e, i, o, u) in the string.
# It should be case-insensitive, so both uppercase and lowercase vowels should be counted.

# Usage:
# text = "Hello World"
# print(count_vowels(text))  # Output: 3


def count_vowels(text):
    # Define the vowels we want to count
    vowels = "aeiou"
    # Initialize a counter for the number of vowels
    count = 0

    # Iterate over each character in the string
    for char in text.lower():  # Convert to lowercase to handle case-insensitivity
        # Check if the character is a vowel
        if char in vowels:
            count += 1  # Increment the counter if it's a vowel

    return count

