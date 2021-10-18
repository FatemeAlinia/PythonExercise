r=0
num1=float(input('enter the number1: '))

while True :
    op=input('enter the op:+ , - ,* , /  ')
    if op=='+'or op=='-' or op=='*' or op=='/':
        break
    else:
        print('op is wrong')

num2=float(input('enter the number2: '))

if op=='+': 
    r=num1+num2
elif op =='-':
    r=num1-num2
elif op=='*':
    r=num1*num2
elif op=='/':
    r=num1/num2

print(str(num1)+op+ str(num2)+'='+str(r))        

    
   