import pandas as pd
import csv
import os
from datetime import datetime

# Initialize data
transactions = []
categories = ["food", "transport", "entertainment", "other"]
budgets = {"food": 200.0, "transport": 100.0, "entertainment": 50.0, "other": 50.0}
filename = "transactions.csv"

# Load transactions from CSV file
def load_transactions():
    if not os.path.exists(filename):
        return
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                transactions.append({
                    "amount": float(row["amount"]),
                    "category": row["category"],
                    "date": row["date"]
                })
    except Exception as e:
        print(f"Error loading transactions: {e}")

# Save transactions to CSV file
def save_transactions():
    try:
        with open(filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["amount", "category", "date"])
            writer.writeheader()
            for transaction in transactions:
                writer.writerow(transaction)
    except Exception as e:
        print(f"Error saving transactions: {e}")

# Add a new transaction
def add_transaction():
    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        category = input(f"Enter category ({', '.join(categories)}): ").lower()
        if category not in categories:
            raise ValueError(f"Category must be one of {', '.join(categories)}.")
        date = input("Enter date (YYYY-MM-DD, press Enter for today): ").strip()
        if not date:
            date = datetime.now().strftime("%Y-%m-%d")
        else:
            # Validate date format
            datetime.strptime(date, "%Y-%m-%d")
        transaction = {"amount": amount, "category": category, "date": date}
        transactions.append(transaction)
        save_transactions()
        print("Transaction added successfully!")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# View transaction history
def view_history():
    if not transactions:
        print("No transactions found.")
        return
    df = pd.DataFrame(transactions)
    print("\nTransaction History:")
    print(df.to_string(index=False))
    print(f"\nTotal Spending: ${df['amount'].sum():.2f}")

# View spending by category and budget status
def view_by_category():
    if not transactions:
        print("No transactions found.")
        return
    df = pd.DataFrame(transactions)
    summary = df.groupby("category")["amount"].sum().to_dict()
    print("\nSpending by Category:")
    for category in categories:
        spent = summary.get(category, 0.0)
        budget = budgets.get(category, 0.0)
        status = "Under" if spent <= budget else "Over"
        print(f"{category.capitalize()}: Spent ${spent:.2f}, Budget ${budget:.2f}, Status: {status}")
    total_spent = df["amount"].sum()
    total_budget = sum(budgets.values())
    print(f"\nTotal: Spent ${total_spent:.2f}, Budget ${total_budget:.2f}")

# Update budget for a category
def update_budget():
    try:
        category = input(f"Enter category to update ({', '.join(categories)}): ").lower()
        if category not in categories:
            raise ValueError(f"Category must be one of {', '.join(categories)}.")
        amount = float(input(f"Enter new budget for {category}: "))
        if amount < 0:
            raise ValueError("Budget cannot be negative.")
        budgets[category] = amount
        print(f"Budget for {category} updated to ${amount:.2f}.")
    except ValueError as e:
        print(f"Error: {e}")

# Main menu
def main():
    load_transactions()
    while True:
        print("\n=== Expense Tracker Menu ===")
        print("1. Add Transaction")
        print("2. View Transaction History")
        print("3. View Spending by Category")
        print("4. Update Budget")
        print("5. Exit")
        choice = input("Enter choice (1-5): ").strip()
        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_history()
        elif choice == "3":
            view_by_category()
        elif choice == "4":
            update_budget()
        elif choice == "5":
            print("Thank you for using Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()