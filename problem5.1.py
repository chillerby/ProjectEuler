n = 21
product = 2
for x in range(3, n+1):
    print("The lowest possible positive whole number that is divisible by numbers 1 to ", x-1, " is ", product)
    if product%x == 0:
        product=product
        continue
    else:
        for y in range(2, x):
            if x%y == 0:
                if (y * product)%x == 0:
                    product = (y * product)
                    break
            elif y == (x-1):
                product = product * x
                break