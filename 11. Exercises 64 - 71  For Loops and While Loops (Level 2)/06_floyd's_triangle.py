
text = int(input("\nEnter a number... : "))

start = 0

print('-------------------------------------')

for i in range(1, text+1):
    for j in range(1, i+1):
        if j == i:
            start = start + 1
            print(str(start) + ' ')
        else:
            start = start + 1
            print(str(start) + ' ', end="")
