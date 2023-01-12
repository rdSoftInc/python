
# text = [[1, 2, 3], [4, 5, 6], [7, 8, 9], 10]

# text = [1, 2, 3, 4, 5, 6, [7, 8, 9]]

text = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]

finalText = []

for i in range(len(text)):
    if type(text[i]) == list:
        finalText.extend(text[i])
    else:
        finalText.append(text[i])

print('-------------------------------------')

print(str(finalText) + '\n')
