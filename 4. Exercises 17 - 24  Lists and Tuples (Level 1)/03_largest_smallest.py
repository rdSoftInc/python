
text = input(
    "\nEnter a list of numbers separated by space... : ").split(' ')

if len(text) == 1:
    print('None\n')
    quit()

print('-------------------------------------')

print(str(max(list(map(int, text)))) + ' ' +
      str(min(list(map(int, text)))) + '\n')
