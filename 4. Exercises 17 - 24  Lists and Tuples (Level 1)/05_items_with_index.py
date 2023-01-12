
text = input(
    "\nEnter a list of numbers separated by space... : ").split(' ')

print('-------------------------------------')

if len(text) == 1:
    print('Empty List\n')
    quit()

index = 0

for i in text:
    print(i + " " + str(index))
    index = index + 1
