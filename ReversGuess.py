import random

num = int(input("Enter a number between 1 and 100 and allow me to guess it in seconds: "))
if 100 < num < 0:
    num = int(input("I said a number between 1 and 100, please try again: "))



guess = random.randint(1, 100)
z = 0
while guess != num:
    z = z+1
    print(guess)
    guess = random.randint(1, 100)
    if guess == num:
        print("Ha, your number was: ", num)
        guess = random.randint(1, 100)
        z = 0
        num = int(input("Enter a number between 1 and 100 and allow me to guess it in seconds: "))
    elif z == 300:
        num = int(input("I said a number between 1 and 100, please try again: "))
        z = 0


