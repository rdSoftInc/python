
text = int(input("\nEnter year... : "))

print('-------------------------------------')

if text % 4 != 0:
    print('\nNo\n')
elif text % 100 != 0:
    print('\nYes\n')
elif text % 400 != 0:
    print('\nNo\n')
else:
    print('\nYes\n')
