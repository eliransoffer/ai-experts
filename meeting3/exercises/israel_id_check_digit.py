# Exercise
# Write a function check_digit that takes one argument - 8 digits of Israeli id as string
# and returns int that represents check digit for this id

# Calculation
# 1  2  3  4  5  6  7  8
# 1  2  1  2  1  2  1  2
# Multiplication:
# 1  4  3  8  5  12 7  16
# Sum of 2-digit multiplications:
# 1  4  3  8  5  3  7  7
# Total sum: 38
# Completion to 40: 2
# Check difit: 2

# Usage
# check_digit("12345678") # output: 2