#Name: GHnanishtha Bhardwaj
#Class: B.tech CSE 1st Year (AI ML) Section A
#Roll No: 2501730296
#Date: 09/11/2025
#Daily Calorie Tracker Application

import datetime

print("Welcome to the Daily Calorie Tracker Application! \n" \
"This application helps you track your daily calorie intake and expenditure.\n")


meal_count     = int(input("How many meals they would like to log today? "))  # number of meals

meal_data      = []
calorie_list   = []
count          = 0


for i in range(meal_count):

    meal_name   = input("Enter the meal name (e.g., Breakfast, Lunch, Dinner, Snack): ")
    meal_cal    = float(input(f"Enter the calories consumed for {meal_name} in kcal: "))

    meal_data.append((meal_name, meal_cal))  # storing meal name and calorie amount as tuple in list


for record in meal_data:

    calorie_list.append(record[1])
    count = count + 1


total_kcal    = sum(calorie_list)    # total calories consumed
average_kcal  = total_kcal / count   # average calories per meal


daily_target  = float(input("Enter your daily calorie goal: "))


# comparing total calories with daily calorie goal
if total_kcal > daily_target:
    print(f"Warning: You have exceeded your daily calorie goal by {total_kcal - daily_target} kcal.")
elif total_kcal < daily_target:
    print(f"Good job! You are within your daily calorie goal. You have {daily_target - total_kcal} kcal remaining.")
else:
    print("Great! You have met your daily calorie goal exactly.")


# displaying summary of meals
print("\nSummary of your meals today:\n" 
"Meal Name\tCalories (kcal)\n" 
"-------------------------------")

for entry in meal_data:
    print(f"{entry[0]}\t{entry[1]}")

print(f"\nTotal:\t {total_kcal} kcal")   # total calories consumed displayed
print(f"\nAverage:\t {average_kcal} kcal")  # average calories per meal displayed

print("\nThank you for using the Daily Calorie Tracker Application! Stay healthy!")


save_response = input("Would you like to save your meal data? \n"
"Enter 'yes' to save or 'no' to exit: ").lower()

if save_response == "yes":

    file_handle = open("calorie_log.txt", "w")  # opening file in write mode to save data

    file_handle.write("Meal Name\tCalories (kcal)\n")
    file_handle.write("-------------------------------\n")

    for entry in meal_data:
        file_handle.write(f"{entry[0]}\t\t{entry[1]}\n")

    file_handle.write(f"\nTotal Calories Consumed:\t {total_kcal} kcal\n")
    file_handle.write(f"\nAverage Calories per Meal:\t {average_kcal} kcal\n")
    file_handle.write(f"\nLog Date and Time: {datetime.datetime.now()}\n")

    file_handle.close()

    print("Your meal data has been saved to 'calorie_log.txt'.")
