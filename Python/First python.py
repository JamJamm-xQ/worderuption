print('Hello! Welcome To Rotinum')
name=input('What\'s Your Name?\n')
print ('What\'s Your Name?'); print ('Hello, '+name+'! \n Welcome!')

print ('How Old Are You?')
age=int(input())

confirm=str(input('Is This Correct?'))
if confirm=='Yes':
    print ('All Set!')

#---
#---
#---

students=["Kofi","Efua","Ama","Kojo"]
numb=int(input('Enter a number'))

if numb==0:
    print (students[0])
elif numb==1:
    print (students[1])
    
#-----

students=["Kofi","Efua","Ama","Kojo"]
numb=str(input('Enter your username\n-->'))

if numb=='Kofi' or numb=='0':
    print (students[0])
elif numb=='Efua' or numb=='1':
    print (students[1])
elif numb=='Ama' or numb=='2':
    print (students[2])
elif numb=='Kojo' or numb=='3':
    print (students [3])
else:
    print ('Invaild Input!!')

#-----
#-----
#-----

print ('University of BeyLan Student Registration')
a1=[str(input('Name\n')), int(input('Age\n'))]
b2=[a1, int(input('Index Number\n')), str(input('Program\n'))]
print ('Name: '+str(a1[0])+'\nAge: '+str(a1[1])+'\nIndex Number: '+str(b2[1])+'\nProgram: '+str(b2[2]))
print ('Is this correct?')
ans=str(input())
if ans=='Yes' or ans=='yes':
    print('Welcome to University of BeyLan!')
elif ans=='No' or ans=='no':
    print('Oops! Guess you\'d have to start all over. Sorry!')
else:
    print('Sorry, invalid input. Is this correct?')
    ans=str(input())
    if ans=='Yes' or ans=='yes':
        print('Welcome to University of BeyLan!')
    else:
        print('Oops! Guess you\'d have to start all over. Sorry!')

#-----

matrix_test=[
    [2,3,4],
    ['a','b','c'],
    ['g',6,'q']
    ]
print(matrix_test[0][2])

#-----


