
# text = dict({"a": 4, "b": 6})

text = dict()

print('\nDictionary is ', str(text))

key = input("\nEnter a key to check... : ")

print('-------------------------------------')

if key in text:
    print('True\n')
else:
    print('False\n')
