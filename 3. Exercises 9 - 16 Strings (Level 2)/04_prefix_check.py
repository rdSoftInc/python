
text = input("\nEnter a statement... : ")

prefix = input("\nEnter a prefix... : ")

prefixMatch = False

print('-------------------------------------')

if prefix == text[0:len(prefix)]:
    prefixMatch = True

print(str(prefixMatch) + '\n')
