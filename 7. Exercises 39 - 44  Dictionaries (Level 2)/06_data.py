
my_dict = dict({
    "description": "shoe",
    "price": 4.56,
    "colors": ["green", "blue", "red"],
})

final_dict = []

print('--------------------------------------------')

for i in my_dict:
    temp = []
    temp.append(i)
    temp.append(my_dict.get(i))
    final_dict.append(temp)

print('\n' + str(final_dict) + '\n')
