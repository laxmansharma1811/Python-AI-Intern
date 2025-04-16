# Operators:
# Arithmetic: +, -, *, /, // (floor division), % (modulus), ** (exponent).
# Comparison: ==, !=, <, >, <=, >=.
# Logical: and, or, not.

# Create a program that takes two numbers from the user and prints their sum, difference, product, quotient (with regular division), floor division, modulus, and exponentiation.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum_result = num1 + num2
diff_result = num1 - num2
prod_result = num1 * num2
quot_result = num1 / num2
floor_div_result = num1 // num2
mod_result = num1 % num2
exp_result = num1 ** num2
print(f"Sum: {sum_result}")
print(f"Difference: {diff_result}")
print(f"Product: {prod_result}")
print(f"Quotient: {quot_result}")
print(f"Floor Division: {floor_div_result}")
print(f"Modulus: {mod_result}")
print(f"Exponentiation: {exp_result}")


# Write a program that checks if a number is both divisible by 3 and greater than 10. Print "Valid" if true, otherwise print "Invalid".

num = int(input("Enter a number: "))

if num%3==0 and num>10:
    print("Valid")
else:
    print("Invalid")

