
# my_dict = dict({"a": 1, "b": 2, "c": 3})

# my_dict = dict({"a": 4, "b": 4, "c": 4})

my_dict = dict()

print('\nDictonary : ' + str(my_dict) + '\n')

constant = None

allSame = True

print('--------------------------------------------')

if len(my_dict) == 0:
    print("\nEmpty\n")
    quit()

for i in my_dict.keys():
    if constant == None:
        constant = my_dict.get(i)
    else:
        if my_dict.get(i) != constant:
            allSame = False

print('\n' + str(allSame) + '\n')
