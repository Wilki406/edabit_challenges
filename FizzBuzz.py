# fizzbuzz of specific number
def fizz_buzz(x):
    if (x) % 3 == 0 and x % 5 == 0:
        return "FizzBuzz"

    elif (x) % 3 == 0:
        return "Fizz"

    elif (x) % 5 == 0:
        return "Buzz"

    else:
        return (str(x))

fizz_buzz(3)


# range of numbers fizzbuzz
for i in range(100):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')

    elif i % 3 == 0:
        print('Fizz')

    elif i % 5 == 0:
        print('Buzz')

    else:
        print(i)
        i = i + 1
