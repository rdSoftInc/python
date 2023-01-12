
text = input(
    "\nEnter a statement... : ")

freq_dict = dict()

print('--------------------------------------------')

for i in text:
    if not i.isspace() and not i.isdigit():
        if i.lower() in freq_dict:
            freq_dict[i.lower()] = freq_dict[i.lower()] + 1
        else:
            freq_dict[i.lower()] = 1

print('\n' + str(freq_dict) + '\n')
