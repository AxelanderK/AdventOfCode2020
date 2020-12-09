from functools import reduce

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

slope = []

slope.append(calThrees(items, 1, 1))
slope.append(calThrees(items, 1, 3))
slope.append(calThrees(items, 1, 5))
slope.append(calThrees(items, 1, 7))
slope.append(calThrees(items, 2, 1))

result = 0
for x in slope:
    print(x)
    result += result * x

print(reduce(lambda x, y: x*y, slope))