items = [
    ("shabeer", 1996),
    ("shafeel", 1995),
    ("erfan", 1997),
    ("saleel", 1995),
]
# year_list = []
# for name, birth_year in items:
#     # print(birth_year)
#     year_list.append(birth_year)

# print(year_list)


year_list = list(map(lambda item: item[1], items))
print(year_list)
