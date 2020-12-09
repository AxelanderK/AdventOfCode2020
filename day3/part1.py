entries = list(open('day3/input.txt','r').read().split('\n'))

def calThrees(items, rows, cols):
    count = 0
    row = 0
    col = 0
    
    while row < len(items)-1:
        row += rows
        col += cols
        if (items[row][col] == '#'):
            count += 1
    return count

items = []

for e in entries:
    items.append(e * 100)

print(calThrees(items, 1, 3))