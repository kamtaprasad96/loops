# write a python script to calculate sum of digit of a given numbers

number=int(input('enter a number :'))
sum=0
while number>0:
    digit=number%10
    number=number//10
    sum=sum+digit
print('sum of given digit:', sum)
