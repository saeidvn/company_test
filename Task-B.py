listOfChars = ['a', 's', 'g', 't', 'y', 'w', 'f', 'p', 'g', 'z', 'n', 'n']

def findDublication(input):
    if type(input) != list:
        print('Input must be list')
        return

    existingSymbols = []
    for symbol in input:
        if symbol not in existingSymbols:
            existingSymbols.append(symbol)
        else:
            return symbol
    return None

duplicate = findDublication(listOfChars)
print(duplicate)