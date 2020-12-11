import re

def getFieldValue(parts, field):
    for part in parts:
        if part[0] == field:
            return part[1]

entries = list(open('day4/input.txt','r').read().split('\n\n'))

passports = [x.replace('\n', ' ').split() for x in entries]
count = 0

for passport in passports:
    parts = [x.split(':') for x in passport]

    if (len(parts) > 6):
        if not (len(parts) == 7 and any('cid' in y for y in parts)) or len(parts) == 8:
            count += 1

print(count)
