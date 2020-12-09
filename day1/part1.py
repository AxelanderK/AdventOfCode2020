import itertools

def check(a, b):
    return ((a + b) == 2020)

entries = list(map(int, open('day1/input.txt','r').read().split('\n')))

for a, b in itertools.combinations(entries, 2):
    if check(a, b):
        print(a * b)