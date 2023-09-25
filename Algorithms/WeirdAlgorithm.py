n = int(input())
t = input()

split_n = t.split(" ")

# Convert the whole input to integers, optional
for i in range(len(split_n)): 
    split_n[i] = int(split_n[i])


rng = list(range(1, n))

for i in rng:
    if(i not in split_n):
        print(i)
    


rng = list(range(1, n))

if 1 in rng:
    print("1")

quit()
while n != 1:
    if n % 2 == 0:
        n = n / 2
    elif n % 2 == 1:
        n = n * 3 + 1

    n = int(n)

    print(str(n) + " ", end="")
