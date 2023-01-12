
my_dict = [["a", 1], ["b", 2], ["c", 3], ["d", 4]]

# my_dict = dict()

res_dict = dict()

print('\nDictonary : ' + str(my_dict) + '\n')

print('--------------------------------------------')

for i in range(len(my_dict)):

    temp = my_dict[i]

    res_dict[temp[0]] = str(temp[1])

print('\n' + str(res_dict) + '\n')
