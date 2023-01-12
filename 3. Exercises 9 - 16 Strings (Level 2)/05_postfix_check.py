
text = input("\nEnter a statement... : ")

postfix = input("\nEnter a postfix... : ")

postfixMatch = False

print('-------------------------------------')

if text[len(text)-len(postfix):len(text)] == postfix:
    postfixMatch = True

print(str(postfixMatch) + '\n')
