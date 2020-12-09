entries = list(open('day2/input.txt','r').read().split('\n'))

count = 0

for e in [x.split() for x in entries]:
    charNumbers = e[0].split('-')
    char = e[1].replace(':', '')
    password = e[2]
    
    minChars = int(charNumbers[0])
    maxChars = int(charNumbers[1])

    occurrences = password.count(char)
    if occurrences >= minChars and occurrences <= maxChars:
        count += 1

print(count)