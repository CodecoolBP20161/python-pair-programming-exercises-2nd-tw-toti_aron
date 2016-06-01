import random
import string


def passwordgen():
    alphabet_upp = string.ascii_uppercase
    alphabet_low = string.ascii_lowercase
    num = str("0123456789")
    sym = str("!@#$%^&*()?")
    pass_length = 8
    mypass = ''

    for i in range(0, 2):
        next_index = random.randrange(len(alphabet_low))
        mypass = mypass + alphabet_upp[next_index]
    for j in range(0, 2):
        next_index = random.randrange(len(alphabet_upp))
        mypass = mypass + alphabet_low[next_index]
    for k in range(0, 2):
        next_index = random.randrange(len(num))
        mypass = mypass + num[next_index]
    for k in range(0, 2):
        next_index = random.randrange(len(sym))
        mypass = mypass + sym[next_index]
    return mypass


def main():
    passw = passwordgen()
    print(passw)
    return


if __name__ == '__main__':
    main()
