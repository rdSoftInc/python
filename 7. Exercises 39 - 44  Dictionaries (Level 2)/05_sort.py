
my_dict = dict({
    "a": [4, 3, 2],
    "b": [5, 3, 7],
    "c": [1, 9, 10],
    "d": [3, 4, 1]
})


# my_dict = dict()

print('\nDictonary : ' + str(my_dict) + '\n')

print('--------------------------------------------')

for i in my_dict:
    my_dict.get(i).sort()

print('\n' + str(my_dict) + '\n')
