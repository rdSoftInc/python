
text = input("\nEnter a word... : ")

textLen = len(text)

oddCharacters = ""

print('-------------------------------------')

if (textLen < 2):
    print(text)
    quit()

for i in range(len(text)):
    if i % 2 != 0:
        oddCharacters = oddCharacters + text[i:i+1]

print('Odd Characters are ' + oddCharacters + '\n')
