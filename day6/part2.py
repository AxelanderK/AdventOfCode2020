import sys

def test(item):
    answers = {}
    persons = len(item)
    count = 0

    for x in item:
        for char in list(x):
            if char in answers:
                answers[char] = int(answers[char]) + 1
            else:
                answers[char] = 1
    
    for answer in answers:
        if answers[answer] == persons:
            count +=1

    return count

inputpath = sys.path[0] + '/input.txt'

entries = list(open(inputpath,'r').read().split('\n\n'))
items = [x.replace('\n', ' ').split() for x in entries]
count = 0

for item in items:
    count += test(item)

print(count)
