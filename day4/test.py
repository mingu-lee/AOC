import re

file = open('day4/puzzle.txt', 'r')

# separate into a list of passport chunks
allPassports = file.read().split('\n\n')

# conver the chunks into key/value pairs
def cleanPassport(p):
    pairs = [(k, v) for (k, v) in [row.split(':') for row in [row for row in re.split('[\n|\s]', p)]]]
    return pairs

def checkPassports(passport):
    """
    Returns false if one of the keys is not present in this passport,
    otherwise it returns true and is added to a list of valid passports.
    """
    # ignoring 'cid' because it seems optional
    # it MUST have these exact keys.
    # can't count number of keys because cid could be one and that doesn't count
    KEYS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    keysInThisPassPort = [pair[0] for pair in passport]
    for key in KEYS:
        if key not in keysInThisPassPort:
            return False
    return True

cleanedPassports = [cleanPassport(p) for p in allPassports]

validPassports = [p for p in cleanedPassports if checkPassports(p)]

print(len(list(validPassports)))