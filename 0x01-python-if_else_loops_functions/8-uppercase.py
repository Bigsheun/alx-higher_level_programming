#!/usr/bin/python3
def uppercase(str):
    for i in str:
        i = ord(i)
        if 97 <= i <= 122:
            i = i - 32
        print(f"{i:c}", end='')
    print()
