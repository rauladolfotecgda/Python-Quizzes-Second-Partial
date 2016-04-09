#Raúl Adolfo Torres Vargas
#A01400187
#Quiz06

d = 1
while d == 1:
    a = int(input("Please give me a number: "))
    b = int(input("Please give me a different number: "))
    break

def euclides (a,b):
    while b != 0:
        (a,b) = (b, b % a)
    return a

print(euclides(a,b))
d = int(input("Do you try again? If you wanna try again, please select a number: \n 0 = yes or 1 = no: "))