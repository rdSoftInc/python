
text = int(input("\nEnter a number... : "))

print('-------------------------------------')

for i in range(1, text+1):
    for j in range(1, i+1):
        if j == i:
            print('* ')
        else:
            print('* ', end="")
