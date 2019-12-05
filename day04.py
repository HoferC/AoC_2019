import itertools


def validPassword(password):
    okNumbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    prevNumber = password[0]
    while prevNumber != okNumbers[0]:
        okNumbers.pop(0)
    doubleSatisfied = False
    for c in password[1:]:
        if c == prevNumber:
            doubleSatisfied = True
        if c not in okNumbers:
            return False
        elif c == okNumbers[0]:
            prevNumber = c
            continue
        else:
            while c != okNumbers[0]:
                okNumbers.pop(0)
        prevNumber = c
    if doubleSatisfied:
        return True
    else:
        return False

def validPassword2(password):
    prevNumber = password[0]
    chain = 1
    for c in password[1:]:
        if c == prevNumber:
            chain += 1
        else:
            if chain == 2:
                return True
            chain = 1
        prevNumber = c
    # If we end on a sequence of 2, we need to accept this one
    if chain == 2:
        return True
    else:
        return False




def star1():
    print("Star 1")
    min = 165432
    max = 707912
    validCount = 0
    # Do the range inclusive
    for i in range(min, max+1):
        if validPassword(str(i)):
            validCount += 1
    print('Valid Count: ', validCount)


def star2():
    print("Star 2")
    min = 165432
    #min = 122222
    max = 707912
    validCount = 0
    # Do the range inclusive
    for i in range(min, max + 1):
        if validPassword(str(i)):
            if validPassword2(str(i)):
                validCount += 1
    print('Valid Count: ', validCount)
    # 771 is too low, 1716 is max