
text = input("\nEnter a statement... : ").split(' ')

stagingText = []

finalText = ""

for i in text:
    stagingText.append(sorted(i.lower()))

for i in stagingText:
    for j in i:
        finalText = finalText + j
    finalText = finalText + " "

print('-------------------------------------')

print(finalText + '\n')
