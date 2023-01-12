
text = input("\nEnter a statement... : ")

curr_char = input("\nEnter currenct character to replace : ")

new_char = input("\nEnter new character to replace the currenct character : ")

textLen = len(text)

finalText = ""

index = 0

print('-------------------------------------')

for i in text:
    index = index + 1
    if i == curr_char:
        finalText = finalText + new_char
    else:
        finalText = finalText + i

print('Character\'s Swapped, final text is : ' + finalText + '\n')
