import random
words = {"plan": 'we plan', "cars": "Your drive them", "thanks": "To appriciate a gseture",
         "share": "To give with others", "naughty": "Part of santa list", "offer": "To give"}

pick, hint = random.choice(list(words.items()))
print(pick)

print("This word has: ", (len(pick)), "letters")

x = 0
y = 10
hintt = 10
score = 105
while x != 20:
    score = score - 5
    print("Your score is", score)
    if y != 0:
        y = y-1
        hintt = hintt - 1
        if hintt <= 5:
            unlock = str(input("Would you like a hint?: "))
            unlock = unlock.lower()
            if unlock == 'yes':
                print(hint)
                score = score - 50
                print("Your score is now", score)
        print(y + 1, "guesses left.")
        guess = str(input("Please guess a letter in my word: ")[0])
        final = str(input("take your guess?: "))
        if final == pick:
            print("Congratulations you got it")
            print("Your final score is", score)
            x = 20
        elif guess in pick:
            print("Well done, " + guess + " was correct")
            score = score + 5
        else:
            print("Sorry its not in there")
    else:
        final = str(input("Please take your guess: "))
        if final == pick:
            print("Congratulations you got it")
            print("Your final score is", score)
            x = 20
        else:
            print("Sorry that wrong")