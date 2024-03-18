course = ("Bachelor of commerce")
print(len(course))

food = ("biriyani")
print(len(food))

Bike = ("Royal Enfield")
print(len(Bike))

salary = ("70000")
print(len(salary))

house = ("vattakinar")
print(len(house))

print(course[0])
print(course[-1])
print(course[0:3])
print(course[0:])
print(course[:5])
print(course[:])
print(house[3])


# escape sequences in string
# \"
# \'
# \\
# \n
name_1 = "saleel \'ahamed"
name_2 = "saleel \"ahamed"
name_3 = "saleel \\ahamed"
name_4 = "saleel \nahamed"
print(name_1, name_2, name_3)
print(name_4)


# formatted string
starting_year = "2014"
ending_year = "2017"
print(starting_year + " - " + ending_year)  # not in formatted string
print(f"{starting_year} - {ending_year}")  # this line is formatted string

first_name = "saleel"
last_name = "ahamed"
print(f"{first_name} {last_name}")

house_first_name = "zafsa"
house_second_name = "manzil"
print(f"{house_first_name} {house_second_name}")

place_name_first = "vatta"
place_name_second = "kinar"
print(f"{place_name_first}{place_name_second}")
