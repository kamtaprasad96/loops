# write a python script to calculate sum of squares of first N natural numbers


"""number=int(input('enter a number : '))
sum=0
i=1
while i<=number:
    sum=sum+i**2
    i+=1
print('sum of squares of first N natural numbers : ',sum)"""

#  using for loops and range function

number=int(input('enter a number :' ))
sum=0
for i in range(1,number+1):
    sum=sum+i**2
print('sum of squares of first N natural numbers : ',sum)