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
    valid = True

    if (len(parts) > 6):
        if not (len(parts) == 7 and any('cid' in y for y in parts)) or len(parts) == 8:
            byr = getFieldValue(parts, 'byr')
            iyr = getFieldValue(parts, 'iyr')
            eyr = getFieldValue(parts, 'eyr')
            hgt = getFieldValue(parts, 'hgt')
            hcl = getFieldValue(parts, 'hcl')
            ecl = getFieldValue(parts, 'ecl')
            pid = getFieldValue(parts, 'pid')

            #byr
            if len(byr) != 4 or (int(byr) < 1920 or int(byr) > 2002):
                valid = False
            #iyr
            if len(iyr) != 4 or (int(iyr) < 2010 or int(iyr) > 2020):
                valid = False
            #eyr
            if len(eyr) != 4 or (int(eyr) < 2020 or int(eyr) > 2030):
                valid = False
            # hgt
            hgtMatch = re.match(r'^([0-9]*)(cm|in)$', hgt)
            if not hgtMatch:
                valid = False
            else:
                if hgtMatch[2] == 'cm' and (int(hgtMatch[1]) < 150 or int(hgtMatch[1]) > 193):
                    valid = False
                elif hgtMatch[2] == 'in' and (int(hgtMatch[1]) < 59 or int(hgtMatch[1]) > 76):
                    valid = False
            
            #hcl
            hclMatch = re.match(r'^#[0-9a-f]{6}$', hcl)
            if not hclMatch:
                valid = False

            #ecl
            if not ecl in ['amb','blu','brn','gry','grn','hzl','oth']:
                valid = False

            #pid
            pidMatch = re.match(r'^[0-9]{9}$', pid)
            if not pidMatch:
                valid = False
        else:
            valid = False
    else:
        valid = False

    if valid:
        count += 1

print(count)
