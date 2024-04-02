# count = 0
# for number in range(1, 100):
#     if number % 5 == 0:
#         count += 1
#         print(number)
# print(f"we have {count} numbers which is divisible by 5")


# def name(first, second):
#     print(f"hi {first} {second}")


# name("saleel", "ahamed")


# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total


# print(multiply(2, 3, 4, 5))


# first we went to wayanad
# then to idukki
# then to kodaikanal
# at last wonderla


# list = ["wayanad", "idukki", "ooty", "wayanad",
#         "kodaikanal", "wonderla", "kozhikode"]
# for place in list:
#     if place == list[0]:
#         print(f"first we went to {place}")
#     elif place == list[-1]:
#         print(f"at last {place}")
#     else:
#         print(f"then to {place}")

# first we went to wayanad
# then to idukki
# then to kodaikanal
# at last wonderla

# list = ["wayanad", "idukki", "pazhayangadi", "ooty", "wayanad",
#         "kodaikanal", "wonderla", "kozhikode"]
# for index, place in enumerate(list):
#     if index == 0:
#         print(f"first we went to {place}")
#     elif place == "kozhikode" and index == (len(list)-1):
#         print("finally im home")
#     elif place == "kozhikode" or place == "pazhayangadi":
#         print("then to my hometown")
#     elif index == (len(list)-1):
#         print(f"at last {place}")
#     else:
#         print(f"then to {place}")


# list1 = ["wayanad", "idukki", "pazhayangadi", "ooty", "wayanad",
#          "kodaikanal", "wonderla", "kozhikode"]


# print(len(list))


# def enumerate_list(list):
#     tuple_list = []
#     for number in range(len(list) - 1):
#         item = (number, list[number])
#         tuple_list.append(item)
#     return tuple_list


# list1 = ["wayanad", "idukki", "pazhayangadi", "ooty", "wayanad",
#          "kodaikanal", "wonderla", "kozhikode"]
# for index, place in enumerate(list1):
#     print(index, place)


# shopping_cart = [
#     ("shirt", 1000),
#     ("jeans", 800),
#     ("underwear", 350),
#     ("belt", 200)
# ]

# print(list(map(lambda item: item[1]+50, shopping_cart)))


# def sort_price(item):
#     return item[1]


# shopping_cart.sort(key=lambda item: item[1])
# print(shopping_cart)


# print(list(filter(lambda item: item[1] >= 500, shopping_cart)))

# new_list = [item[0] for item in shopping_cart]
# print("new_list", new_list)
# filtering = [item for item in shopping_cart if item[1] >= 500]
# print("filtered list", filtering)


# age should be more than 25
# height should be more than 170
# list = [
#     ["saleel", 29, 179],
#     ["fazal", 23, 170],
#     ["jazim", 30, 160]
# ]

# filtering = [(name, age, "he is eligible")
#              for name, age, height in list if age > 25 and height > 170]
# print("filtered", filtering)


# abc = ["apple", "banana", "cat"]
# efg = ["fruit", "fruit", "pet"]

# print(list(zip(abc, efg)))


# list1 = [
#     {"name": "saleel", "age": 29, "height": 179},
#     {"name": "fazal", "age": 23, "height": 170},
#     {"name": "jazim", "age": 30, "height": 160}
# ]


list = [
    ["saleel", 29, 179],
    ["fazal", 23, 170],
    ["jazim", 30, 160],
]

# create index wih range
# new_list = []
# for num in range(len(list)):
#     item = list[num]
#     item.append(num)
#     print(item)
#     new_list.append(item)
# print(new_list)

# new_list = [[index] + list[index] for index in range(len(list))]

# with enumerate method
# new_list = []
# for x, y in enumerate(list):
#     new_list.append([x] + y)
# print(new_list)

new_list = [[x] + y for x, y in enumerate(list)]
print(new_list)
