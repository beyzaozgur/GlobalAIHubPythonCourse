#Beyza Özgür

def prime_first(num):
    if num in range(0, 500):
        if num > 1:
            for i in range(2, num):
                if (num % i == 0):
                    break
            else:
                print(num)


def prime_second(num):
    if num in range(500, 1000):
        if num > 1:
            for i in range(2, num):
                if (num % i == 0):
                    break
            else:
                print(num)


for i in range(0, 1000):
    prime_first(i)  # prints prime numbers between 0 and 500
    prime_second(i)  # prints prime numbers between 500 and 1000