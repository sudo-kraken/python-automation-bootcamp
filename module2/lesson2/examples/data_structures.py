# data_structures.py
# Demonstrates the use of lists, tuples, sets, and dictionaries in Python.

def list_operations():
    fruits = ["apple", "banana", "cherry", "banana"]
    fruits.append("date")
    print("List (with duplicates):", fruits)

def tuple_operations():
    coordinates = (10, 20, 30)
    print("Tuple:", coordinates)

def set_operations():
    numbers = {1, 2, 3, 3, 2, 1}
    print("Set (duplicates removed):", numbers)

def dictionary_operations():
    person = {"name": "Alice", "age": 30, "city": "London"}
    print("Dictionary:", person)
    print("Name from dictionary:", person.get("name"))

def main():
    print("=== Data Structures Demo ===")
    list_operations()
    tuple_operations()
    set_operations()
    dictionary_operations()

if __name__ == "__main__":
    main()
