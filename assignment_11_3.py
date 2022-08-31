# write a python script to calculate sum of cubes of first N natural numbers

number=int(input('enter a number :' ))
sum=0
i=1
while i<=number:
    sum=sum+i**3
    i+=1
print('sum of cubes first N natural numbers :',sum )

# using for loop and range()

number=int(input('enter  a number :'))
sum=0
for i in range(1,number+1):
    sum=sum+i**3
print('sum of cubes of first N natural number :',sum)