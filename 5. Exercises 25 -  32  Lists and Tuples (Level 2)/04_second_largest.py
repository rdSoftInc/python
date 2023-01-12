
text = input(
    "\nEnter a list of numbers separated by space... : ").split(' ')

print('-------------------------------------')

if len(text) == 1 or len(text) == 2:
    print('None\n')
    quit()

secondLargest = None
Largest = None

for i in text:
    if Largest == None:
        secondLargest = int(i)
        Largest = secondLargest
    else:
        if Largest < int(i):
            secondLargest = Largest
            Largest = int(i)

print('Second Largest : ' + str(secondLargest) + '\n')
