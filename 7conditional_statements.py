# temparature = int(input("weather: "))
temparature = 50
if temparature < 20:
    print("it is cold")
    print("cover up and snuggle")
elif temparature > 35:
    print("go and drink water")
    print("dont go outside")
else:
    print("good weather")


height = 179
if height < 100:
    print("good height")
    print("selected")
elif height < 150:
    print("bad height")
    print("not selected")
else:
    print("done thank you for visit")


age = 30
if age > 25:
    print("not eligible")
else:
    print("you are eligible")

message = "not eligible" if age > 25 else "you are eligible"
print(message)

# the same conditional statement can be written in ternary operator = that means to cut short the code to single line

money = 25000
message = "eligible" if money <= 26000 else "not eligible"
print(message)


location = 10
message = "near" if location <= 5 else "far"
print(message)
