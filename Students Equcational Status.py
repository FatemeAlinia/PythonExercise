r=0
name=(input('enter the name: '))
s1=float(input('enter first score: '))
s2=float(input('enter second score: '))
s3=float(input('enter third score: '))
r=(s1+s2+s3)/3
if r>17:
    print(name + 'Great')
if r<17:
   if r>15:
    print (name +'Normal')
if r<15:
    print(name + 'Fail')


