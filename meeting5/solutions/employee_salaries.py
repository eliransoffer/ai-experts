# You have a list of employee dictionaries, each containing their name, department, and salary.
# Task:
# Filter: Select employees from the 'Engineering' department.
# Map: Calculate the annual salary for each employee (assuming monthly salary) and add "annual_salary" field to each employee.
# Sort: Sort the filtered employees by their annual salary in descending order.
from pprint import pprint

employees = [
    {'name': 'Alice', 'department': 'Engineering', 'salary': 8000},
    {'name': 'Bob', 'department': 'Sales', 'salary': 7000},
    {'name': 'Charlie', 'department': 'Engineering', 'salary': 9000},
    {'name': 'David', 'department': 'Marketing', 'salary': 6000},
    {'name': 'Eve', 'department': 'Engineering', 'salary': 8500}
]

# Filter employees from the 'Engineering' department
filtered = filter(lambda x: x['department'] == 'Engineering', employees)
mapped = map(lambda e: {**e, "annual_salary": e["salary"] * 12}, filtered)

# Sort employees by annual salary in descending order
sorted_employees = sorted(mapped, key=lambda x: x['annual_salary'], reverse=True)

pprint(sorted_employees)