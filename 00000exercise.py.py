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


list1 = ["wayanad", "idukki", "pazhayangadi", "ooty", "wayanad",
         "kodaikanal", "wonderla", "kozhikode"]


# print(len(list))


# def enumerate_list(list):
#     tuple_list = []
#     for number in range(len(list) - 1):
#         item = (number, list[number])
#         tuple_list.append(item)
#     return tuple_list


print(enumerate_list(list1))


