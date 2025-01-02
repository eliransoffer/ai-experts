# You have a list of employee dictionaries, each containing their name, department, and salary.
# Task:
# Filter: Select employees from the 'Engineering' department.
# Map: Calculate the annual salary for each employee (assuming monthly salary) and add "annual_salary" field to each employee.
# Sort: Sort the filtered employees by their annual salary in descending order.

# Print the final result
# Expected output:

# [{'annual_salary': 108000,
#   'department': 'Engineering',
#   'name': 'Charlie',
#   'salary': 9000},
#  {'annual_salary': 102000,
#   'department': 'Engineering',
#   'name': 'Eve',
#   'salary': 8500},
#  {'annual_salary': 96000,
#   'department': 'Engineering',
#   'name': 'Alice',
#   'salary': 8000}]

employees = [
    {'name': 'Alice', 'department': 'Engineering', 'salary': 8000},
    {'name': 'Bob', 'department': 'Sales', 'salary': 7000},
    {'name': 'Charlie', 'department': 'Engineering', 'salary': 9000},
    {'name': 'David', 'department': 'Marketing', 'salary': 6000},
    {'name': 'Eve', 'department': 'Engineering', 'salary': 8500}
]
