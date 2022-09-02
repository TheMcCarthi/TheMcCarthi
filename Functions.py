'''def lots ( *parameters ):
    numberofpar = len(parameters)
    print("You have: ", numberofpar, "items")
    for items in parameters:
        print(items)

lots('love', 'hello', 10)
lots()'''

def name(name):
    print("Good day " + name)

name('johnny')

def summ(*parameters):
    for items in summ:
        try:
           d = items =+ items
           return d
        except:
            print("Only Numbers Please")



print(summ(10, 50, 30, 70, 4, 22))

def testing(test="No value given"):
    print(test)

testing('Hello')
testing()
x = int(input("Please add a number: "))
def outter(x):
    x = x * x
    def inside(x):

        x = x + 10
        print("Your inner value is: ", x)
    inside(x)

    print("Your outer value is: ", x)

outter(x)








