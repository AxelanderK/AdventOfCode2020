entries = list(open('day2/input.txt','r').read().split('\n'))

count = 0

for e in [x.split() for x in entries]:
    charNumbers = e[0].split('-')
    char = e[1].replace(':', '')
    password = e[2]
    
    yesChar = int(charNumbers[0])
    noChar = int(charNumbers[1])

    occurrences = 0
    if password[yesChar-1] == char:
        occurrences += 1

    if password[noChar-1] == char:
        occurrences += 1

    if occurrences == 1:
        count += 1
        
print(count)