fibonacci = []
for i in range(0, 10):
    if (i == 0 or i == 1):
        fibonacci.append(i)
    else:
        suma = fibonacci[i - 2] + fibonacci[i - 1]
        fibonacci.append(suma)
    print(fibonacci[i])
