# 1 1 2 3 5 8 13 21 34
from math import sqrt


def Fibonacci(limit):
    count = 1
    while count <= limit:
        result = ((1+sqrt(5))**count-(1-sqrt(5))**count)/(2**count*sqrt(5))
        result = int(round(result))
        print(f"{count}: {result}")
        count += 1


number = int(input("\nNumber (Max is 600): \n> "))
Fibonacci(number)
