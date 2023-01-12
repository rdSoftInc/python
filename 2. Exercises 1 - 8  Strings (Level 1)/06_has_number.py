
text = input("\nEnter something... : ")

print('-------------------------------------')

numberExists = False

if text.isdigit():
    print('TRUE')
    quit()

for i in text:
    if i.isdigit():
        numberExists = True

if numberExists == True:
    print('TRUE')
else:
    print('FALSE')
