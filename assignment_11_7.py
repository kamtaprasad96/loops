# write a python script to count digit in a given number

number=int(input('enter a number :'))
count=0
while number>0:
    number=number//10
    count+=1
print(count)