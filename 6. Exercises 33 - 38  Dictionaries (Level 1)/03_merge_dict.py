
my_dict1 = dict({"a": 1, "b": 2, "c": 3})

my_dict2 = dict({"c": 4, "d": 6, "e": 8})

final_dict = dict()

print(my_dict1, my_dict2)

for i in my_dict1.keys():
    final_dict[i] = my_dict1.get(i)

for i in my_dict2.keys():
    final_dict[i] = my_dict2.get(i)


print('---------------------------------------------------------------------------')

print('\n' + str(final_dict) + '\n')
