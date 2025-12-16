# Name: Siddardha Janaki
# Project: Personal Information Manager
# Description: Stores and displays personal information

print("Welcome to the Personal Information Manager!")
print("=" * 33)

# Static information
name = "Siddardha"
age = 20
city = "Narsipatnam"
hobby = "Coding,playing cricket"

# User input
favorite_food = input("Enter your favorite food: ").strip()
favorite_color = input("Enter your favorite color: ").strip()

# Validation
if not favorite_food or not favorite_color:
    print("Error: Input cannot be empty.")
    exit()

# Calculation
age_in_months = age * 12

# Display output
print("\n" + "=" * 33)
print("       PERSONAL INFORMATION")
print("=" * 33)

print(f"Name: {name}")
print(f"Age: {age} ({age_in_months} months old)")
print(f"City: {city}")
print(f"Hobby: {hobby}\n")

print(f"Favorite Food: {favorite_food.title()}")
print(f"Favorite Color: {favorite_color.title()}")

print("\n" + "=" * 33)
print("Thank you for using the program!")

