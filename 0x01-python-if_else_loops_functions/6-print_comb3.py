#!/usr/bin/python3
for num in range(0, 10):
    for num2 in range(num + 1, 10):
        if num == 8 and num2 == 9:
            print(f"{num:d}{num2:d}")
        elif num < num2:
            print(f"{num:d}{num2:d}", end=", ")
