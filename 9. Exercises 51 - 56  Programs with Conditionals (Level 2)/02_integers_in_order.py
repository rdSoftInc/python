
text1 = int(input("\nEnter number 1... : "))

text2 = int(input("\nEnter number 2... : "))

text3 = int(input("\nEnter number 3... : "))

print('-------------------------------------')

if text3 > text2 > text1:
    print('\nIncreasing Order\n')
elif text1 > text2 > text3:
    print('\nDecreasing Order\n')
else:
    print('\nNone\n')
