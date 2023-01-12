
from math import sqrt


text = input("\nEnter 3 co-ordinates for point A... : ").split(' ')

textTwo = input(
    "\nEnter 3 co-ordinates for point B... : ").split(' ')

total = 0.0

partA = int(text[0]) - int(textTwo[0])
partA = partA**2

partB = int(text[1]) - int(textTwo[1])
partB = partB**2

partC = int(text[2]) - int(textTwo[2])
partC = partC**2

total = float(sqrt(partA + partB + partC))

print('-------------------------------------')

print('Distance : ' + str(total) + '\n')
