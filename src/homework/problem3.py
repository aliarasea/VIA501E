# Randomly generate a 6 x 6 list that has exactly 12 ones placed in random locations in the list. The rest
# of the entries should be zeroes. Note you can visualize the 2D list using display function.

import random


def problem3():
    matrix = [[0 for _ in range(6)] for _ in range(6)]
    for r in range(12):
        while True:
            row = random.randint(0, 5)
            col = random.randint(0, 5)
            if matrix[row][col] == 0:
                matrix[row][col] = 1
                break

    for i in range(6):
        print(matrix[i])


problem3()
