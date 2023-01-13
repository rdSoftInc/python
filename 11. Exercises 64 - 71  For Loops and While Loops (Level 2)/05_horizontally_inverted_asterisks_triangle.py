
text = int(input("\nEnter a number... : "))

limit = text - 1

print('-------------------------------------')

for i in range(0, text):

    for j in range(0, text):

        if j < limit:
            print('  ', end="")
        else:
            if j == text-1:
                print(' *')
                limit = limit - 1
            else:
                print(' *', end="")
