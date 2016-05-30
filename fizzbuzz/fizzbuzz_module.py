def fizzbuzz(number):
    if number % 15 == 0:
        number = "FizzBuzz"
    elif number % 5 == 0:
        number = "Buzz"
    elif number % 3 == 0:
        number = "Fizz"
    return number


def main():
    for i in range(1, 101):
        print(fizzbuzz(i))
    return

if __name__ == '__main__':
    main()
