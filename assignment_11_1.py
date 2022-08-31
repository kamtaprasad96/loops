# write a python program to calculate sum of first N number natural 

number=int(input('enter a first N natural number  : '))
'''sum=0
i=1
while i<=number:
    sum=sum+i
    i+=1
print('sum of first N natural number is :',sum)'''


# using for loops and range function sum of first N natural number

sum=0
for i in range(1,number+1):
    sum=sum+i
print('sum of first N natural numbers is: ',sum)
