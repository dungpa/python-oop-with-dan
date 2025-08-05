# Turn this program into as many sensible functions as you can define
# Then, call those functions to make sure they still work (and the program works as it did before)
import random


size = int(input("Enter a list size: "))
lower = int(input("Enter a lower bound: "))
upper = int(input("Enter an upper bound: "))
my_list = []
for _ in range(size):
    my_list.append(random.randint(lower, upper))
total = 0
for num in my_list:
    total += num
average = total / len(my_list)
