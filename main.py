# Fizz Buzz Game
number % 3 and number % 5 ----> Fizz Buzz
number % 3 ----> Fizz
number % 5 ----> Buzz


target = 20
for number in range(1, target + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
