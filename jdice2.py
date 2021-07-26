import csv
import random


def getwords(n):
    wordbank = getwordbank()
    random_numbers = rollthedice(n)
    wordlist = matcher(random_numbers, wordbank)
    return wordlist


def getwordbank():
    wordbank = {}
    reader = csv.reader(open('bip39-diceware-wordlist.csv'))
    for row in reader:
        key = row[0]
        if key in wordbank:
            # implement your duplicate row handling here
            pass
        wordbank[key] = row[1]
    return wordbank


def rollthedice(numberofwords):
    number_list = []
    final = ""
    i = 0
    rolls = 0
    dice_needed = 5  # first die is acts as the coin
    min, max = 1, 6
    while i < numberofwords:
        while rolls < dice_needed:
            x = random.randint(min, max)
            x = str(x)
            final = final + x
            rolls = rolls + 1
        # Uses the first roll as the coin
        # Even/Heads , Odd/Tails
        if int(final[0]) % 2 == 0:
            final = "h" + final[1:]
        else:
            final = "t" + final[1:]
        if int(final[1:]) > 4362 and final[0] == "t":  # If larger than t4362
            i -= 1  # Roll again!
        else:
            number_list.append(final)
        i += 1
        rolls = 0
        final = ""
    return number_list


def matcher(number_list, wordbank):
    wordlist = []
    passphrase = ""
    for item in number_list:
        wordlist.append(wordbank[item])
    for item in wordlist:
        passphrase = passphrase + " " + item
        passphrase = passphrase.strip()
    return passphrase


#p = getwords(24)
#print(p)