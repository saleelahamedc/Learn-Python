age = 4
donation = 25000
is_home_reachable_distance = False

if (age >= 4 and donation >= 25000) and is_home_reachable_distance:
    print("eligible for admission")
elif (age >= 4 and donation >= 25000) and not is_home_reachable_distance:
    print("need a bus")
else:
    print("not eligible")
