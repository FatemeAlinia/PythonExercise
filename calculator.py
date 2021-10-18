import math

r=0
num1=float(input('enter the number1: '))

while True :
    op=input('enter the op:+ , - ,* , /,^ ,sin , cos, tan , cot ,sqrt:  ')
    if op=='+'or op=='-' or op=='*' or op=='/' or op=='sin' or op=='cos ' or op=='sqrt'  or op=='tan' or op=='cot' or op=='^':
        break
    else:
        print('op is wrong')
if  op=='+'or op=='-' or op=='*' or op=='/'or op=='^':

    num2=float(input('enter the number2: '))

    if op=='+': 
        r=num1+num2
    elif op =='-':
        r=num1-num2
    elif op=='*':
        r=num1*num2
    elif op=='/':
        r=num1/num2
    elif op=='^':
        r=num1**num2
    print(str(num1)+op+ str(num2)+'='+str(r))    
else:
    if op=='sin': 
        r=math.sin(num1)
    elif op =='cos':
        r=math.cos(num1)
    elif op=='tan':
        r=math.tan(num1)
    elif op=='cot':
        r=1/math.tan(num1)
    elif op=='sqrt':
        r=math.sqrt(num1)

    print(op+' '+ str(num1)+'='+str(r))    

    
   