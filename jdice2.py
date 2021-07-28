import csv
import random


def getwords(n):
    word_list = rollthedice(n)
    passphrase = cleaner(word_list)
    return passphrase


def getwordlist(n):
    word_list = rollthedice(n)
    return word_list


def getword(dicecode):
    word = bip39lookup(dicecode)
    return word


def firstfour(partialword):
    if len(partialword) < 4:
        return "Partial word must be at least four characters."
    wordbank = getwordbank()
    for word in wordbank.values():
        if partialword[0:4] == word[0:4]:
            return word
    return "Not found!"



def getcode(word):
    wordbank = getwordbank()
    for code, words in wordbank.items():
        if word == words:
            return code
    return "Word not in list!"


def getcodelist(listofwords):
    code_list = []
    for word in listofwords:
        c = getcode(word)
        code_list.append(c)
    return code_list


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
    word_list = []
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
            word = bip39lookup(final)
            word_list.append(word)
        i += 1
        rolls = 0
        final = ""
    return word_list


def bip39lookup(dicecode):
    wordbank = getwordbank()
    try:
        word = wordbank[dicecode]
    except:
        raise ValueError("Improper Dice Code. Must be h1111 through h6666 or t1111 through t4362.")
    return word


def cleaner(wordlist):
    passphrase = ""
    for item in wordlist:
        passphrase = passphrase + " " + item
        passphrase = passphrase.strip()
    return passphrase


def generate_password(passwordLength):
    chars = "!#$%&'()*+,-./23456789:;<=>?@ABCDEFGHJKLMNOPRSTUVWXYZ[\]^_abcdefghijkmnopqrstuvwxyz{|}~"
    password = ""
    i = 0
    while i < passwordLength:
        x = random.randint(0, len(chars)-1)
        password = password+chars[x]
        i += 1
    return password
