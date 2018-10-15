solved = False
while not solved:
    for x in range(1, 50000000):
        if solved == True:
            break
        counter = 0
        print(x)
        for y in range(1,9):
            print(y)
            if solved == True:
                break
            elif x%y == 0:
                counter += 1
                print("counter = ", counter)
                if counter == 19:
                    solution = x
                    solved = True
                continue
            else:
                break
print(solution)

# n = 2, x = 2
# n = 3, x = 6
# n = 4, x = 12 
# n = 5, x = 60
# n = 6, x = 60
# n = 7, x = 420
# n = 8, x = 840
# n = 9, x = 2520