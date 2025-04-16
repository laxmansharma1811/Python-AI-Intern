# Write a program that takes a user’s score (0–100) and assigns a letter grade: A (90–100), B (80–89), C (70–79), D (60–69), F (below 60).
while True:
    users_score = int(input("Enter your score (0-100): "))

    if users_score > 100 or users_score < 0:
        print("Invalid score")

    elif users_score >= 90:
        print("Grade: A")

    elif users_score >= 80:
        print("Grade: B")

    elif users_score >= 70:
        print("Grade: C")

    elif users_score >= 60:
        print("Grade: D")

    elif users_score < 60:
        print("Grade: F")
    
    else:
        print("Invalid score")
        break




# Use a for loop to print the first 10 multiples of a number entered by the user.
number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f'{number} x {i} = {number * i}')

# Use a while loop to keep asking the user for a positive number until they enter one, then print its square.

while True:
    positive_number = int(input("Enter a positive number: "))

    if positive_number > 0:
        print(f"The square of {positive_number} is {positive_number ** 2}")
        break
    else:
        print("Please enter a positive number.")