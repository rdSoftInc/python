
text = input("\nEnter a list of numbers separated by space... : ").split(' ')

textTwo = input(
    "\nEnter a list of numbers separated by space... : ").split(' ')

largerLength = 0
largerList = None

if len(text) > len(textTwo):
    largerLength = len(text)
    largerList = 'text'
else:
    largerLength = len(textTwo)
    largerList = 'textTwo'

finalText = []

for i in range(largerLength):
    if largerList == 'text':
        if text.__contains__(textTwo[i]):
            finalText.append(textTwo[i])
    else:
        if textTwo.__contains__(text[i]):
            finalText.append(text[i])


print('-------------------------------------')

print('Common Items : ' + str(finalText) + '\n')
