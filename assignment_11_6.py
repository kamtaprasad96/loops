# write a python script to calculate factorial of a given number

number=int(input('enter a number '))
fact=1
i=1
while i<=number:
    fact=fact*i
    i+=1
print('factorial of n numbers :',fact)