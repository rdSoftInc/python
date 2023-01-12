
text = dict({"January": 45, "February": 56, "March": 67})

print('\nDictionary is ', str(text))

item = input("\nEnter a key & value separated by space.. : ").split()

print('-------------------------------------')

if text.__contains__(item[0]):
    print('\n' + str(text) + '\n')
else:
    text[item[0]] = item[1]
    print('\n' + str(text) + '\n')
