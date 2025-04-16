# Create a list of 6 expenses (e.g., [45.5, 20.0, 100.0, 30.5, 60.0, 15.0]). Write a program to:
# Add a new expense to the list.
# Remove the smallest expense.
# Sort the list in ascending order.
# Print the final list and its average.

expenses = [45.5, 20.0, 100.0, 30.5, 60.0, 15.0] 

# Add a new expense to the list
expenses.append(50.0)
print("Expenses after adding a new expense:", expenses)

# Remove the smallest expense
expenses.remove(min(expenses))
print("Expenses after removing the smallest expense:", expenses)

# Sort the list in ascending order
expenses.sort()
print("Sorted expenses:", expenses) 

# Calculate the average of the expenses
average_expense = sum(expenses) / len(expenses)
print("Average expense:", average_expense)

# Write a program that takes a list of numbers and returns a new list containing only the even numbers.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_number = []

for number in numbers:
    if number % 2 == 0:
        even_number.append(number)

print("Even numbers:", even_number)