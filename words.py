# 1
def print_upper_words(words):
    """Print each word on a seperate line, but all in uppercase."""

    for word in words:
        print(word.upper())

print_upper_words(['hello','my', 'name', 'is', 'Marian'])


# 3
def print_upper_words3(words,):
    """Change the function so it only prints words that start with e (either upper or lowercase)"""

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

print_upper_words3(['Eello','my', 'name', 'is', 'earian'])

# 4
def print_upper_words4(words, must_start_with):
    """Print each word on sep line, uppercased, if starts with one of given"""

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())


print_upper_words4(['Hello','my', 'name', 'is', 'Marian'],["h","m","H","M"])

