import sys
import math

def decodeParts(min, max, parts):
    for item in parts:
        diff = (max-min)/2

        if item == 'F' or item == 'L':
            max = math.floor(max-diff)
        elif item == 'B' or item == 'R':
            min = math.ceil(min+diff)

    return min

inputpath = sys.path[0] + '/input.txt'

entries = list(open(inputpath,'r').read().split('\n'))

seatIDs = []

for card in entries:
    items = list(card)
    
    row = decodeParts(0, 127, items[:-3])
    col = decodeParts(0, 7, items[-3:])
    
    print(row)
    print(col)

    seatIDs.append((row * 8) + col)

seatIDs.sort(reverse=True)
print(seatIDs[0])
