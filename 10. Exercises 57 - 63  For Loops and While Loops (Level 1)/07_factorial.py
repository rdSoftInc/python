
text = int(input("\nEnter a number greater or equal to 2... : "))

factorial = 1

print('-------------------------------------')

for i in range(1, text+1):
    factorial = factorial * i

print(factorial)
