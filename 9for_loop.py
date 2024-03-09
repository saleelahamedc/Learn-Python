is_successful = False
for number in range(3):
    print("saleel")
    if is_successful:
        print("done")
        break
# for else loop
else:
    print("Attempt Failed")


# nested loops

for x in range(3):
    for y in range(3):
        for z in range(3):
            print(f"{x} {y} {z}")

# iterable
# range functions returns range object which is iterable
shopping_cart = ["shirt", "jeans", "shoe", "belt"]
for item in shopping_cart:
    if item == "shoe":
        print(item)
        break
