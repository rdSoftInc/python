
alphabets = ('abcdefghijklmnopqrstuvwxyz')

text = input("\nEnter a statement... : ")

alphaCount = 26

print('-------------------------------------')

for i in range(len(alphabets)):
    if text.__contains__(alphabets[i:i+1]):
        alphaCount = alphaCount - 1

if alphaCount == 0:
    print('True\n')
else:
    print('False\n')
