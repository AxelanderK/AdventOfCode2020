import itertools

def check(a, b, c):
    return ((a + b + c) == 2020)

entries = list(map(int, open('day1/input.txt','r').read().split('\n')))

for a, b, c in itertools.combinations(entries, 3):
    if check(a, b, c):
        print(a * b * c)