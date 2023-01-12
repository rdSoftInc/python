
text = input("\nEnter a word... : ")

count = dict()

characters = ""

for i in range(len(text)):
    if count.__contains__(text[i:i+1]):
        count[text[i:i+1]] = count.get(text[i:i+1]) + 1
    else:
        count[text[i:i+1]] = 1

repeatedCount = 0

for k in count.keys():
    if count[k] > 1:
        repeatedCount = repeatedCount + 1
        characters = characters + " " + k


print('-------------------------------------')

if (repeatedCount > 0):
    print(repeatedCount)
    print(characters)
else:
    print(0)
