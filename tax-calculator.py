print("ROAD TAX CALCULATOR")

cost=int(input("Enter cost price of Bike : "))
tax=0;
if cost>100000:
   tax=cost*0.15
elif cost > 50000 and cost <=100000 :
   tax=cost*0.10
elif cost <= 50000 :
   tax=cost*0.5
else: print("Invalid cost")

print("BIKE costs : ",cost,", tax: ",tax)
