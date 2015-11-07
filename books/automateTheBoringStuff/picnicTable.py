#!/usr/bin/python3

def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for i, j in itemsDict.items():
        print(i.ljust(leftWidth, '.') + str(j).rjust(rightWidth))

picniceItems = {'sandwiches': 4, 'apples': 12, 'cups': 4 'cookies': 8000}

printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)
