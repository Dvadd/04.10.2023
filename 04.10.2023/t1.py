початок = 1500
кінець = 2700
for число in range(початок,кінець +1):
    if число % 7 == 0 and число % 5 == 0:
        print(число)
        