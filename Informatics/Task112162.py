a = int(input())

if 0 < a < 13:
    if a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
        print(31)
    if a == 4 or a == 6 or a == 9 or a == 11:
        print(30)
    if a == 2:
        print(28)
else:
    print(0)