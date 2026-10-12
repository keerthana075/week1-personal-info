
# Name: VALLURUPALLI KEERTHANA
# Project: Personal Information Manager
# Description: Stores and displays personal information.

# Welcome message
print("=" * 40)
print("   PERSONAL INFORMATION MANAGER")
print("=" * 40)
print("Welcome to my first Python project!\n")

# Step 1: Store static personal information
name = "Keerthana"
age = 22
city = "Hyderabad"
hobby = "Listening to music"

# Step 2: Get user input with basic validation
print("Please enter your preferences:")
print("-" * 40)

# Ask for favorite food and validate the input
favorite_food = input("What is your favorite food? ").strip()

while not favorite_food:
    print("Input cannot be empty. Please try again.")
    favorite_food = input("What is your favorite food? ").strip()

# Ask for favorite color and validate the input
favorite_color = input("What is your favorite color? ").strip()

while not favorite_color:
    print("Input cannot be empty. Please try again.")
    favorite_color = input("What is your favorite color? ").strip()

# Step 3: Calculate age in months
age_in_months = age * 12

# Step 4: Display all personal information
print("\n" + "=" * 40)
print("       YOUR PERSONAL INFORMATION")
print("=" * 40)

# Use f-strings and string methods for formatting
print(f"Name           : {name.title()}")
print(f"Age            : {age} years ({age_in_months} months old)")
print(f"City           : {city.title()}")
print(f"Hobby          : {hobby.capitalize()}")

print("-" * 40)
print(f"Favorite Food  : {favorite_food.title()}")
print(f"Favorite Color : {favorite_color.title()}")

# Goodbye message
print("\n" + "=" * 40)
print("Thank you for using this program!")
print("Have a great day!")
print("=" * 40)
