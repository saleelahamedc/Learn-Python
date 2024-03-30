def log(*values, decor="*", end="\n", padding=2):
    if padding <= 0:
        padding = 1
    for x in values:
        str_value = str(x)
        length = len(str_value)
        dummy_line = decor * (length + (padding*2))
        print(dummy_line)
        print(decor*(padding-1) + " " + str_value + " " + decor*(padding-1))
        print(dummy_line + end)


log(15555, 2525, 45, decor="%", padding=0)
