
text = int(input("\nEnter a number... : "))

status = "Prime\n"

print('-------------------------------------')

if text == 0 or text == 1:
    print('Not Prime\n')
    quit()

for i in range(2, text+1):
    if text != i and text % i == 0:
        status = "Not Prime\n"

print(status)
