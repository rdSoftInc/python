
my_dict = dict({
    "a": 4,
    "b": 4,
    "c": 2,
    "d": 7,
    "e": 4,
    "f": 2,
    "g": 7,
    "h": 7
})

# my_dict = dict()

freq_dict = dict()

print('\nDictonary : ' + str(my_dict) + '\n')

print('--------------------------------------------')

if len(my_dict) == 0:
    print("\nEmpty\n")
    quit()

for i in my_dict.keys():
    if my_dict.get(i) in freq_dict:
        freq_dict[my_dict.get(i)] = freq_dict[my_dict.get(i)] + 1
    else:
        freq_dict[my_dict.get(i)] = 1

print('\n' + str(freq_dict) + '\n')
