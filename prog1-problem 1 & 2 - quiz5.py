#Raúl Adolfo Torres Vargas
#A01400187
#Quiz05 problem 1 and 2

# -*- coding: utf-8 -*-
def is_palindrome(word):
    wd = word[::-1]
    return (wd == word)

def find_three_numbers(amount):
    the_sum = 0
    my_list = []
    for number in amount:
        if number % 3 == 0:
            my_list.append(number)
            the_sum += number
    print(my_list)
    return the_sum

a = int(input("How many number will you give me?: "))
z = []
new_list = []
for i in range(a):
    b = int(input("Please give me a number: "))
    z.append(b)

word = str(input("Please give me a word: "))
print(find_three_numbers(z))
print(is_palindrome(word))