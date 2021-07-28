import csv
import random
import hashlib


def getwords(n):
    word_list = rollthedice(n)
    passphrase = cleaner(word_list)
    return passphrase


def getwordlist(n):
    word_list = rollthedice(n)
    return word_list


def getword(dicecode):
    word = wordfromdice(dicecode)
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
            word = wordfromdice(final)
            word_list.append(word)
        i += 1
        rolls = 0
        final = ""
    return word_list


def wordfromdice(dicecode):
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
        x = random.randint(0, len(chars) - 1)
        password = password + chars[x]
        i += 1
    return password


#######################################################
# BIP39-Compliant Section Starts Here
#######################################################

# Original Method: https://armantheparman.com/bitcoin-seed-with-dice/
# Verify: https://iancoleman.io/bip39/


def getbip39():
    s = bip39_roll()
    indexes = getindexes(s)
    bank = getwordbank()
    bip39 = list(bank.values())
    phraselist = matchwords(indexes, bip39)
    final_word = checksum(s, bip39)
    phraselist[-1] = final_word
    bip39phrase = " "
    bip39phrase = bip39phrase.join(phraselist)
    return bip39phrase


def bip39_roll():
    s = ""
    times = 0
    while times < 256:
        n = random.randint(1, 6)
        if n <= 3:
            d = "0"
        else:
            d = "1"
        s = s + d
        times += 1
    return s


def getindexes(s):
    indexes = []
    i = 0
    while i < 23:
        w = str(int(s[0 + (11 * i):11 + (11 * i)], 2))  # was +1 - I think I was adding twice
        indexes.append(w)
        i += 1
    last_three = s[-3:]
    indexes.append(last_three)
    return indexes


# Get wordbank removed (was duplicated)


def matchwords(indexes, bip39):
    phrase = []
    for index in indexes:
        word = bip39[int(index)]
        phrase.append(word)
        # phrase = phrase+" "+word # return a list instead
    return phrase


def checksum(s, bip39):
    # String of binary to actual bytes
    zz = int(s, 2).to_bytes(len(s) // 8, byteorder="big")

    # Hash it
    h = hashlib.sha256(zz).hexdigest()

    # The first two digits of the hash, then to binary of them
    f = getletternumber(h[0])
    ss = getletternumber(h[1])
    fb = bin(int(f))[2:].zfill(4)
    sb = bin(int(ss))[2:].zfill(4)

    # Add them to the leftovers
    s_last = s[-3:]
    final = s_last + fb + sb

    checksum_word_index = int(final, 2)  # + 1
    final_word = bip39[checksum_word_index]
    return final_word


def getletternumber(letter):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if letter in letters:

        # get the NUMBER and then it's the binary NUMBER (I think...)
        letter = letter.lower()
        i = letters.index(letter)
        i = i + 10  # (a=10,b=11, etc.)
        return i
    else:
        return letter  # nothing to see here - send it back!
