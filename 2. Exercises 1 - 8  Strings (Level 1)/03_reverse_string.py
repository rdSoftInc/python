
text = input("\nEnter a statement... : ")

revText = ""

textLen = len(text)

print('-------------------------------------')

if (textLen == 0):
    print('')
    quit()

for i in range(textLen):
    revText = revText + text[(textLen-1)-i]

print("Reverse of the string : " + revText + "\n")
