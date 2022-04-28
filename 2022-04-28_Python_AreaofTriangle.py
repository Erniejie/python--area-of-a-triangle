#Python Program
# Find the Area of A Triangle

A = float(input("Enter The First Side a: "))
B = float(input("Enter The First Side b: "))
C= float(input("Enter The First Side c: "))

S = (A+B+C)/2    # Semi Perimeter Calculation in Python

Area  = (S*(S-A)*(S-B)*(S-C))**0.5   # Heron's Formula

print("The Area Of The Triangle is: %0.2f" % Area)
