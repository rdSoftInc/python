
text = input("\nEnter a list of numbers separated by space... : ").split(' ')

count = dict()

for i in range(len(text)):
    item = text.__getitem__(i)
    if count.__contains__(str(item)):
        count[str(item)] = count[str(item)] + 1
    else:
        count[str(item)] = 1

for i in count.keys():
    if count[i] > 1:
        for j in range(count[i]):
            if j != 1:
                text.remove(i)

print('-------------------------------------')

print('Final List : ' + str(text) + '\n')
