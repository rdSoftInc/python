
text = input("\nEnter a statement... : ")

textLen = len(text)

finalText = ""

print('-------------------------------------')

for i in range(len(text)):
    if text[i:i+1] != ' ':
        finalText = finalText + text[i:i+1]

print('Spaces removed, final text is : ' + finalText + '\n')
