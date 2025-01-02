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
    pass