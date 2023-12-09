#!/usr/bin/python3


def greet(name):
    """
    This function greets the person passed in as a parameter.
    """

    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello, World!")


if __name__ == "__main__":
    # Test the greet function
    person_name = input("Enter your name: ")
    greet(person_name)
