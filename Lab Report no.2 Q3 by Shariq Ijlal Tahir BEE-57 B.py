amount=int(input("Enter Amount: Rs."))
print("1.Personal Financial 2.Personal Homeowner 3.Personal Gold")
print("4.Small Business     5.Big Business       6.Gold Business\n")
a=int(input("Select type of Account: "))
if(a==1):
    c=(2.3/100)*amount
    print("You have selected Personal Financial account.")
    print("Interest on amount of Rs.",amount,"is Rs.",c)
elif(a==2):
    c=(2.6/100)*amount
    print("You have selected Personal Homeowner account.")
    print("Interest on amount of Rs.",amount,"is Rs.",c)
elif(a==3):
    c=(2.9/100)*amount
    print("You have selected Personal Gold account.")
    print("Interest on amount of Rs.",amount,"is Rs.",c)
elif(a==4):
    c=(3.3/100)*amount
    print("You have selected Small Business account.")
    print("Interest on amount of Rs.",amount,"is Rs.",c)
elif(a==5):
    c=(3.5/100)*amount
    print("You have selected Big Business account.")
    print("Interest on amount of Rs.",amount,"is Rs.",c)
elif(a==6):
    c=(3.8/100)*amount
    print("You have selected Gold Business account.")
    print("Interest on amount of Rs.",amount,"is Rs.",c)
else:
    print("INVALID CHOICE, PLEASE SELECT ONE OF THE GIVEN CHOICES.")
