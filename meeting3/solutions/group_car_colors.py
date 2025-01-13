# Exercise: Analyze Car Models and Colors
# Write a function group_car_colors that takes two lists as input:
#
# A list models representing car models.
# A list colors representing car colors, where each color corresponds to a car model in the same position in the list.
# The function should group the colors by car model, ensuring that each car model is associated with a
# list of unique colors (without duplicates).
# The function should return a dictionary where the keys are the car models and the values are lists of colors.

# Example input:
models = ["Mazda 3", "Toyota Yaris", "Volvo S40", "Mazda 2", "Toyota Yaris", "Volvo S40"]
colors = ["red", "white", "red", "blue", "black", "red"]


# Example output:
# {
#     "Mazda 3": ["red"],
#     "Toyota Yaris": ["white", "black"],
#     "Volvo S40": ["red"],
#     "Mazda 2": ["blue"]
# }

# Function Requirements:
# Group by Model: For each car model in the models list, gather all corresponding colors from the colors list.
# Handle Duplicates: Ensure that the colors for each model are unique (i.e., no repeated colors).
# Return a Dictionary: Return a dictionary where:
# The keys are car model names.
# The values are lists of unique colors for each model, sorted alphabetically.

def group_car_colors(models, colors):
    # Initialize an empty dictionary to store the grouped colors by model
    car_colors = {}

    # Loop through the models and colors simultaneously
    for model, color in zip(models, colors):
        # If the model is not yet in the dictionary, add it with an empty list
        if model not in car_colors:
            car_colors[model] = []

        # Add the color to the list of the model (only if it's not already in the list)
        if color not in car_colors[model]:
            car_colors[model].append(color)

    # Sort the colors alphabetically for each model
    for model in car_colors:
        car_colors[model].sort()

    return car_colors


# Example usage:
models = ["Mazda 3", "Toyota Yaris", "Volvo S40", "Mazda 2", "Toyota Yaris", "Volvo S40"]
colors = ["red", "white", "red", "blue", "black", "red"]

result = group_car_colors(models, colors)
print(result)
