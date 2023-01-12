
import itertools


# text = [1, 2, 3]

text = ['a', 'b', 'c']

print('-------------------------------------')

for v in itertools.permutations(text):
    print(v)
