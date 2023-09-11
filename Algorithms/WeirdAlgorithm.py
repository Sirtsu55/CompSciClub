n = int(input())

print(n)

while n != 1:
    if n % 2 == 0:
        n = n / 2
    elif n % 2 == 1:
        n = n * 3 + 1

    n = int(n)

    print(str(n) + " ", end="")
