
text = int(input("\nEnter a number... : "))

letters = 64

print('-------------------------------------')

for i in range(1, text+1):
    letters = letters + 1
    for j in range(1, i+1):
        if j == i:
            print(chr(letters) + ' ')
        else:
            print(chr(letters) + ' ', end="")
