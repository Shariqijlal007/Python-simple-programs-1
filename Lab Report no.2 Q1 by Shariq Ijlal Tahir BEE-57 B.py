a=input("Enter 't' for Triangle or 's' for Square.\n")
if(a=='t'):
    b=int(input("Enter Base: "))
    h=int(input("Enter Height: "))
    A=(b*h)/2
    print("The area of your selected choice is:",A,"square meter")
elif(a=='s'):
    b=int(input("Enter Side: "))
    A=b*b
    print("The area of your selected choice is:",A,"square meter")
else:
    print("INCORRECT CHOICE, PLEASE SELECT ONE OF THE GIVEN CHOICES.")
