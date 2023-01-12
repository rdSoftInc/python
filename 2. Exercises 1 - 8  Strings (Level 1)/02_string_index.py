

text = input("\nEnter a statement... : ")

print('-------------------------------------')

if (len(text) == 0):
    print('Empty String...\n')
    quit()

index = input("Enter a index to fetch the character... : ")

if (int(index) > (len(text) - 1)):
    print('Index is out of range...\n')
    quit()

print(text[int(index):int(index)+1] + ' is at ' + str(index) + '\n\n')
