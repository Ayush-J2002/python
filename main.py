x = int(input("enter any no"))
if x > 1:
    for n in range(2, x):
        if x % n == 0:
            print(x, 'not a prime no')
            break

    else:
        print(x, 'is a prime no')
