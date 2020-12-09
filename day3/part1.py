entries = list(open('day3/input.txt','r').read().split('\n'))
entries = entries * 100

row = 0
col = 0

while row <= len(entries):
    row += 1
    col += 3
    print(entries[row][col])

#print(entries)