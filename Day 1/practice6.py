# Create a list of expense categories with duplicates (e.g., ["food", "transport", "food", "entertainment", "transport"]). Convert it to a set to get unique categories and print them.
categories = ["food", "transport", "food", "entertainment", "transport"]
unique_categories = set(categories)
print("Unique categories:", unique_categories)

# Write a program that takes two sets of categories (e.g., set1 = {"food", "transport"}, set2 = {"transport", "entertainment"}) and prints their union, intersection, and difference.
set1 = {"food", "transport"}
set2 = {"transport", "entertainment"}

print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference (set1 - set2):", set1.difference(set2))
