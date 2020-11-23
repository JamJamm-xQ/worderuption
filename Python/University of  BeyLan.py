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
