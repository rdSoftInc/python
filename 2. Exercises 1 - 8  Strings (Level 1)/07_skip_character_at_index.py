
text = input("\nEnter a statement... : ")

index = int(input("\nEnter a index to skip the character... : "))

textLen = len(text)

finalText = ""

print('-------------------------------------')

for i in range(len(text)):
    if i != index:
        finalText = finalText + text[i]

print('Skipped the indexed character, final text is : ' + finalText + '\n')
