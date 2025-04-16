# Variables and Data Types:
# Variables store data and are dynamically typed in Python.
# Common data types: int, float, str, bool.

# Write a program that declares variables for a person's name (str), age (int), height in meters (float), and whether they are a student (bool). Print each variable along with its data type.

name = "Laxman Sharma"
age = 20
height = 1.75
is_student = True

print(f"Name: {name}, Type: {type(name)}")
print(f"Age: {age}, Type: {type(age)}") 


# Swap the values of two variables (e.g., a = 5, b = 10) without using a temporary variable.

a = 5
b = 10

a,b = b,a
print(f"After swapping: a = {a}, b = {b}")