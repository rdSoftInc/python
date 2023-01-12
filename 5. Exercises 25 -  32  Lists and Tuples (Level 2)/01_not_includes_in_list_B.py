
text = input("\nEnter a list of numbers separated by space... : ").split(' ')

textTwo = input(
    "\nEnter a list of numbers separated by space... : ").split(' ')

for i in textTwo:
    if text.__contains__(i):
        text.remove(i)


print('-------------------------------------')

print('List Left : ' + str(text) + '\n')
