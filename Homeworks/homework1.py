#Beyza Özgür

import random as rnd

def isPrime(number):
    if (number <= 1):
        return False

    for i in range(2, number):
        if (number % i == 0):
            return False
    return True

matrix = []

for i in range(1):
  number = rnd.randint(1, 100)
  x = []

  if isPrime(number):
     for j in range(3):

        x.append(number)
        matrix.append(x)
  else:
    while True:
        number = rnd.randint(1,100)

        if isPrime(number):
            for j in range(3):

                x.append(number)
                matrix.append(x)

            break


for i in range(3):
    for j in range(3):
        print(matrix[i][j], end=" ")
    print()

