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


age = 25
if age > 25:
    print("not eligible")
else:
    print("you are eligible")

message = "not eligible" if age > 25 else "you are eligible"
print(message)
