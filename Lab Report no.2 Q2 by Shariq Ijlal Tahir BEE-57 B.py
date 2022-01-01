A=int(input("Enter 1st integer: "))
B=int(input("Enter 2nd integer: "))
C=int(input("Enter 3rd integer: "))
if(A>B)&(A>C):
    print(A,"is greater than",B,"and",C)
elif(B>A)&(B>C):
    print(B,"is greater than",A,"and",C)
elif(C>A)&(C>B):
    print(C,"is greater than",A,"and",B)
else:
    print("Either two or all of the entered integers are equal.")
