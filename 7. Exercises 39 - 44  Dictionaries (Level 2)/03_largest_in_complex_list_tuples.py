
my_dict = dict({
    "a": [1, 2, 3],
    "b": [4, 0, -4],
    "c": [3, 5, 9],
    "d": [45, 12, 100]
})


# my_dict = dict()

total = 0

print('\nDictonary : ' + str(my_dict) + '\n')

print('--------------------------------------------')

for i in my_dict.keys():

    total = sum(my_dict.get(i))

print('\n' + str(total) + '\n')
