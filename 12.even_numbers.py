numbers = range(1, 11)
even_numbers = 0
for number in numbers:
    if (number % 2) == 0:
        print(number)
        even_numbers = even_numbers + 1
else:
    print(f"we have {even_numbers} even numbers")
