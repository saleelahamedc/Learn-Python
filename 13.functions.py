# def health_quotes():
# print("smoking causes cancer")
# print("Dont drink and drive")


# health_quotes()


# arguments & paramenters

def health_quotes(first_habit, end_result):
    return (f"{first_habit} causes {end_result}")


print(health_quotes("smoking", "cancer"))
health_message = health_quotes("Drinking", "Death")
print(health_message)
file = open("health_msg.md", "w")
file.write(health_message)
