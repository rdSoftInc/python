
my_dict = dict({"a": 4, "b": 3, "c": 7})

# my_dict = dict()

print('\nDictonary : ' + str(my_dict) + '\n')

smallest = None

print('--------------------------------------------')

if len(my_dict) == 0:
    print("\n" + str(smallest) + "\n")
    quit()

for i in my_dict.keys():
    if smallest == None:
        smallest = my_dict.get(i)
    else:
        if my_dict.get(i) < smallest:
            smallest = my_dict.get(i)

print('\n' + str(smallest) + '\n')
