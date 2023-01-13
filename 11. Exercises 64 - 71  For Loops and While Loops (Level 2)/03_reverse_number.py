
text = input("\nEnter a number... : ")

final = ""

print('-------------------------------------')

for i in text:
    lastNumber = int(text) % 10
    final = final + str(lastNumber)
    leftText = int(text) / 10
    text = str(int(leftText))

print('Reverse is ' + final + '\n')
