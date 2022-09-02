import random
words = ['humdrum',
'dysfunctional',
'drunk',
'ancient',
'sulky',
'invent',
'vest',
'tour',
'punish',
'playground',
'handsomely',
'wooden',
'airport',
'planes',
'clean',
'clover',
'receive',
'blot',
'plan',
'cars',
'noxious',
'thank',
'share',
'naughty',
'offer',
'historical',
'longing',
'large']

pick = (random.choice(words))
print(pick)

print("This word has: ",(len(pick)), "letters")

x = 0
y = 16
while x != 20:
    if y != 0:
        y = y-1
        print(y + 1, "guesses left.")
        guess = str(input("Please guess a letter in my word: ")[0])
        final = str(input("Or take your guess: "))
        if guess in pick:
            print("Correct")
        elif final == pick:
            print("Congratulations you got it")
            x = 20
        else:
            print("Sorry its not in there")
    else:
        final = str(input("Please take your guess: "))
        if final == pick:
            print("Congratulations you got it")
            x = 20
        else:
            print("Sorry that wrong")