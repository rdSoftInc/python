
text = input("\nEnter a statement... : ").split(' ')

finalText = ""

print('-------------------------------------')

for word in text:
    revText = ""
    for i in range(len(word)):
        revText = revText + word[len(word)-1-i]
    swtichdRevText = ""
    for j in range(len(revText)):
        if (revText[j]).isupper():
            swtichdRevText = swtichdRevText + revText[j].lower()
        else:
            swtichdRevText = swtichdRevText + revText[j].upper()

    if finalText == "":
        finalText = finalText + swtichdRevText
    else:
        finalText = finalText + " " + swtichdRevText


print(finalText + '\n')
