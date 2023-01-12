
text = input(
    "\nEnter a list of number or characters separated by space... : ").split(' ')

finalText = ""

for i in text:
    finalText = finalText + " " + str(i)

print('-------------------------------------')

print(finalText + '\n')
