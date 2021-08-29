def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    r3 = int(input())
    r5 = int(input())
    r7 = int(input())

    if (r3 == r7):
        for j in range(105):
            if (j % 21 == 0):
                d = j + r3
                if ( d % 5 == r5 ):
                    your_age = d
    elif (r3 == r5):
        for j in range(105):
            if (j % 15 == 0):
                d = j + r3
                if ( d % 7 == r7 ):
                    your_age = d
    elif (r5 == r7):
        for j in range(105):
            if (j % 35 == 0):
                d = j + r5
                if ( d % 3 == r3 ):
                    your_age = d


    print("Your age is " + str(your_age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")
    ans = int(input())
    while ans != 2 :
        print("Please, try again.")
        ans = int(input())
    print('Completed, have a nice day!')


def end():
    print('Congratulations, have a nice day!')


greet('EyaBot', '2021')  # change it as you need
remind_name()
guess_age()
count()
test()
end()

