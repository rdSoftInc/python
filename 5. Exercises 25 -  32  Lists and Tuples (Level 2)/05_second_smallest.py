
text = input(
    "\nEnter a list of numbers separated by space... : ").split(' ')

print('-------------------------------------')

if len(text) == 1:
    print('None\n')
    quit()

smallest = None

for i in text:
    if smallest == None:
        smallest = int(i)
    else:
        if smallest > int(i):
            smallest = int(i)

secondSmallest = int(text[1])

for i in range(len(text)):
    if int(text[i]) > smallest:
        if int(text[i]) < secondSmallest:
            secondSmallest = int(text[i])


print('Second Smallest : ' + str(secondSmallest) + '\n')
