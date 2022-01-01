a=int(input("Enter Starting Value: "))
b=int(input("Enter Ending Value: "))
p=1
for i in range(a,b+1):
    p*=i
print("The product of all the numbers(including starting and ending values) in range is:",p)
