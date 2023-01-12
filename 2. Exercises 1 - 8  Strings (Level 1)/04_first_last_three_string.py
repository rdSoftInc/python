
text = input("\nEnter a statement... : ")

firstText = ""

lastText = ""

textLen = len(text)

print('-------------------------------------')

if (textLen < 6):
    print('')
    quit()

print("First Three Characters : " + text[0:3] + "\n")

print("Last Three Characters : " + text[textLen-3:textLen] + "\n")
