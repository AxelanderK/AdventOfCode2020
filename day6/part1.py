import sys

inputpath = sys.path[0] + '/input.txt'

entries = list(open(inputpath,'r').read().split('\n\n'))
items = [x.replace('\n', ' ').split() for x in entries]
count = 0

for item in items:
    answers = []
    for x in item:
        for char in list(x):
            if not char in answers:
                answers.append(char)

    count += len(answers)

print(count)
