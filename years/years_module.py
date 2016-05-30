from datetime import date


def years(age):
    today = date.today()
    oldage = today.year - age + 100
    return oldage


def main():
    name = input('Please enter your name: ')
    age = int(input('Please enter Your age: '))
    print(years(age))
    return


if __name__ == '__main__':
    main()
