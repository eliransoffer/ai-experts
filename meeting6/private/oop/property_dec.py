class Person:
    def __init__(self, age):
        self._age = age  # Store age as an internal attribute

    @property
    def age(self):
        """Getter for age"""
        return self._age

    @age.setter
    def age(self, new_age):
        """Setter for age"""
        if new_age < 0:
            raise ValueError("Age cannot be negative")
        self._age = new_age


p = Person(18)
p.age = 18