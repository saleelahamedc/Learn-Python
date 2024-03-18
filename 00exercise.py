# def get_irish_time_with_ist(indian_time):
#     time_diff = 5.50
#     converted_ist = float(indian_time)
#     ireland_time = 0.0
#     temp_ireland_time = converted_ist - time_diff

#     if converted_ist > 24:
#         # Immediately stop the function if user input is greater than 24 hrs
#         return print(" :( Invalid Input, Please enter hour within 24")

#     if converted_ist > time_diff:
#         ireland_time = temp_ireland_time
#     else:
#         ireland_time = 24 + temp_ireland_time

#     message = ""

#     if ireland_time > 12:
#         message = "PM"
#         ireland_time = ireland_time - 12
#     else:
#         message = "AM"

#     print(f"Now Irish time is {ireland_time} {message}")


# get_irish_time_with_ist(input("Enter Indian time in 24 hour format (HH.MM): "))


# 4th chapter excercise
fizzbuzz

we have to create a function that can check if it is divisible by 3 & 5
if the number is divisible by 3 there should be a message that shows fizz


