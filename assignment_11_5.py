# write a python script to calculate sum of first N even natural numbers



number=int(input('enter a number :'))
sum=0
i=1
while i<=number:
    sum=sum+2*i
    i+=1
print('sum of first N even natural numbers :',sum)

# using for loop and range()

number=int(input('enter a number :'))
sum=0
for i in range(1,number+1):
    sum=sum+2*i
print('sum of first N even natural numbers :',sum)