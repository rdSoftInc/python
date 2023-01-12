
text = input("\nEnter a list of numbers separated by space... : ").split(' ')

item_to_remove = input("\nEnter item to remove... : ")

finalText = list()

print('-------------------------------------')

if len(text) == 1:
    print('Empty List\n')
    quit()

found = False

for i in text:
    if i.isdigit():
        if int(i) != int(item_to_remove):
            finalText.append(i)
        else:
            found = True
    elif i.isalpha():
        if i != item_to_remove:
            finalText.append(i)
        else:
            found = True

if not found:
    print('Not Found\n')
    quit()

print(str(finalText) + "\n")
