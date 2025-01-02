# you have the following data:
# dishes: A dictionary where keys are dish names (strings) and values are sets of ingredients (strings).
# allergies: A dictionary where keys are person names (strings) and values are sets of allergies (strings).

# Task:
# Determine if the dish is safe for the person to eat


dishes = {
    "Pizza": {"cheese", "tomatoes", "pepperoni"},
    "Salad": {"lettuce", "tomatoes", "cucumbers"},
    "Cake": {"peanuts", "cacao", "sugar"},
    "Sushi": {"rice", "fish", "seaweed"}
}

allergies = {
    "Alice": {"nuts", "fish"},
    "Bob": {"cheese"},
    "Charlie": {"peanuts", "tree nuts"}
}


def is_dish_safe(dish_name, person_name):
    """
    Checks if a given dish is safe for a person to eat based on their allergies.

    Args:
        dish_name: The name of the dish.
        person_name: The name of the person.

    Returns:
        True if the dish is safe, False otherwise.
    """
    try:
        dish_ingredients = dishes[dish_name]
        person_allergies = allergies[person_name]
    except KeyError:
        print(f"Error: Dish '{dish_name}' or person '{person_name}' not found.")
        return False

    # Use set intersection to check for any overlapping allergies
    return not dish_ingredients.intersection(person_allergies)


# Example usage
if __name__ == '__main__':
    dish_to_check = "Cake"
    person_to_check = "Bob"

    if is_dish_safe(dish_to_check, person_to_check):
        print(f"{dish_to_check} is safe for {person_to_check}.")
    else:
        print(f"{dish_to_check} is not safe for {person_to_check}.")