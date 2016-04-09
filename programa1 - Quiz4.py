#Raúl Adolfo Torres Vargas
#A01400187
#Quiz04

from math import factorial
from math import fabs

def fact(x):
    r = 1
    for i in range(1,x+1):
        r = r * 1
    return (r)

def calc_euler(prec):
    n = 0
    prev = 100
    e = 0
    diff = fabs(e - prev)
    print ("diff is: ", diff)
    while (diff >prec):
        prev = e
        e = e + 1.0/factorial(n)
        n = n + 1
        diff = abs(e-prev)
        print ("n is: ", n, "e is: ",e)
    return e

number = calc_euler(0.00000000000000000000000000000000000000000000001)
print(number)