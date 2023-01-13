

text = input("\nEnter a statement... : ")

print('-------------------------------------')

for i in text:
    if (ord(i) > 64 and ord(i) < 91) or (ord(i) > 96 and ord(i) < 123):
        if i in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
            print(i + ' is a vowel\n')
        else:
            print(i + ' is a consonant\n')
    else:
        print(i + ' is not a letter\n')

# if ord(i) > 64 and ord(i) < 91 for A to Z
# if ord(i) > 96 and ord(i) < 123 for a to z
