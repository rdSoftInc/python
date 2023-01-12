
my_dict = dict({"a": 4, "b": 3, "c": 7})

# my_dict = dict()

print('\nDictonary : ' + str(my_dict) + '\n')

largest = None

print('--------------------------------------------')

if len(my_dict) == 0:
    print("\n" + str(largest) + "\n")
    quit()

for i in my_dict.keys():
    if largest == None:
        largest = my_dict.get(i)
    else:
        if my_dict.get(i) > largest:
            largest = my_dict.get(i)

print('\n' + str(largest) + '\n')
