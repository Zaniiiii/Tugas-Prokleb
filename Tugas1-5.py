a = int(input())

for i in range(a, 1, -1):
    for space in range(0, a-i):
        print("  ", end="")
    for j in range(i, 2*i-1):
        print("* ", end="")
    for j in range(1, i-1):
        print("* ", end="")
    print()