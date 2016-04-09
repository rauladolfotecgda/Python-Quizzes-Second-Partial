#Raúl Adolfo Torres Vargas
#A01400187
#Quiz04

from math import factorial

def euler_calc(n):
    for i in range(n):
        return sum(1/float(math.factorial(i)))

n = int(input("Please give me a number: "))

print(euler_calc(n))