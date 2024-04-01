# 1-take any name and gender as 2 inputs then greet with his/her name
# 2-example : "welcome {mr/mrs} {name}"

# name = input("name: ")
# gender = input("gender: ")
# if gender == "male":
#     print(f"welcome mr {name}")
# elif gender == "female":
#     print(f"welcome mrs {name}")
# else:
#     print(f"welcome {name}")

# name = input("name: ")
# gender = input("gender: ")
# age = input("age: ")
# age = int(age)

# if age>= 30:
#     eligible_message = "you are eligible"
# else:
#     eligible_message = "you are not eligible"

# def message_formatter(value=""):
#     return f"welcome {value} {name}, {eligible_message}"

# if gender == "male":
#     message = message_formatter("mr")
# elif gender == "female":
#     message = message_formatter("mrs") 
# else:
#     message = message_formatter()
# print(message)


# name = input("name: ")
# gender = input("gender: ")
# age = input("age: ")
# age = int(age)
# eligible_message = "you are eligible" if age>=30 else "you are not eligible"
# if gender == "male":
#     print(f"welcome mr {name}, {eligible_message}")
# elif gender == "female":
#     print(f"welcome mrs {name}, {eligible_message}")
# else:
#     print(f"welcome {name}, {eligible_message}")

# -------------------------------------------------------------------------------------------------------------------------

name = input("name: ")
gender = input("gender: ")
age = input("age: ")
age = int(age)

eligible_message = "you are eligible" if age>=30 else "you are not eligible"

def message_formatter(value=""):
    return f"welcome {value} {name}, {eligible_message}"

if gender == "male":
    message = message_formatter("mr")
elif gender == "female":
    message = message_formatter("mrs") 
else:
    message = message_formatter()
print(message)