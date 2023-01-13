
text = input("\nEnter a string... : ")

print('-------------------------------------')

textLength = len(text)

while textLength > -1:
    print(text[textLength-1:textLength], end="")
    textLength = textLength - 1

print('\n')
