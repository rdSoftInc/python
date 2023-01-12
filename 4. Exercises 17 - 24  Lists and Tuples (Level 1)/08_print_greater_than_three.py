
text = input("\nEnter a list of numbers separated by space... : ").split(' ')

count = 0

if len(text) == 1:
    print('Total Values Greater Than Three : ' + str(count) + '\n')
    quit()

for i in range(len(text)):
    if int(text[i]) > 3:
        count += 1

print('-------------------------------------')

print('Total Values Greater Than Three : ' + str(count) + '\n')
