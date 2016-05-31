def palindrome(word):
    result = ""
    word = word.lower()
    word = word.replace(" ", '')
    if word == word[::-1]:
        result = True
    else:
        result = False
    return result


def main():
    word=input("Please enter a word and I will tell you that it's a palindrome or not: ")
    status = palindrome(word)
    if status == False:
        print("This is not a palindrome")
    else:
        print("This is a palindrome")
    return


if __name__ == '__main__':
    main()
