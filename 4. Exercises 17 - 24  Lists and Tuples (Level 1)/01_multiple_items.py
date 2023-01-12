
text = input(
    "\nEnter a list of number or characters separated by space... : ").split(' ')

factor = int(input("\nEnter the factor to multiply... : "))

finalText = []

for i in text:
    if i.isdigit():
        finalText.append(int(i)*factor)
    else:
        finalText.append(i*factor)

print('-------------------------------------')

print(str(finalText) + '\n')
