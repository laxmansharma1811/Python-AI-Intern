# Create a dictionary to store budgets for 4 categories (e.g., {"food": 300, "transport": 150, "entertainment": 100, "other": 50}). Write a program to:
# Update the budget for one category based on user input.
# Add a new category with a budget.
# Print all categories and their budgets.
categories = {
    "food": 300,
    "transport": 150,
    "entertainment": 100,
    "other": 50
}

# Update the budget for one category based on user input
category_to_update = input("Enter the category to update: ")
new_budget = float(input(f"Enter the new budget for {category_to_update}: "))
if category_to_update in categories:
    categories[category_to_update] = new_budget
    print(f"Updated budget for {category_to_update}: {new_budget}")
else:
    print(f"Category '{category_to_update}' does not exist. Adding it now.")
    


# Write a program that takes a dictionary of expenses (e.g., {"food": 50, "transport": 20}) and calculates the total spending.

expenses = {
    "food": 50,
    "transport": 20,
    "entertainment": 30,
    "other": 10
}

total_spending = sum(expenses.values())
print("Total spending:", total_spending)