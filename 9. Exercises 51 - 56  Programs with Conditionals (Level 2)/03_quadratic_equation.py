
from math import sqrt


text1 = int(input("\nEnter number 1... : "))

text2 = int(input("\nEnter number 2... : "))

text3 = int(input("\nEnter number 3... : "))

positive = 0

negative = -0

denominator = 2*text1

determinant = (text2**2)-(4*text1*text3)

if determinant > 0:
    A = sqrt(determinant)

print('-------------------------------------')

if determinant < 0:
    print('\nComplex Roots\n')
elif determinant == 0:
    positive = (-text2+A) / denominator
    print('\n' + str(positive) + '\n')
else:
    positive = (-text2+A) / denominator
    negative = (-text2-A) / denominator
    print('\n' + str(negative) + ' ' + str(positive) + '\n')
