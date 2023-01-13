
text1 = int(input("\nEnter number 1... : "))

text2 = int(input("\nEnter number 2... : "))

text3 = int(input("\nEnter number 3... : "))

print('-------------------------------------')

if (text1 > text2) and (text1 > text3):
    print('\n' + str(text1) + '\n')
elif (text2 > text1) and (text2 > text3):
    print('\n' + str(text2) + '\n')
else:
    print('\n' + str(text3) + '\n')
