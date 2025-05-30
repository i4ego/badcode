from random import randint
from secret import * #ne trogat

number = int(input())
random_number = randint(0, 10)

if number==random_number:
    print("You win!")
else:
    print("You lose.")