s=int(input("1.mies/gallon\n2.km/liters\nSelect one unit:"))
if(s==1):
      r=float(input("Enter the miles you have driven: "))
      t=float(input("Enter the gallons of gasoline your car has consumed: "))
      g=(t/r)*100
      print("Your car has gotten",r,"miles per",t,"gallons.")
      print("Your car average speed is",g,"gallons per 100 miles.")
elif(s==2):
    r=float(input("Enter the kilometers you have driven: "))
    t=float(input("Enter the liters of petrol your car has consumed: "))
    g=(t/r)*100
    print("Your car has gotten",r,"kilometers per",t,"liters of petrol.")
    print("Your car average speed is",g,"liters per 100 kilometers.")
