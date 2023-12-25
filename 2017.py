n=input("Enter house number:")
x=int(input("Enter previous units:"))
y=int(input("Enter new units:"))
z=y-x #z=monthly units
if z>64:
    a=z-64
    total_bill=64*5+a*10
else:
    total_bill=z*5
print(total_bill)        

f=open("debt.txt","w")
f.write("House number %s \n"%x)
f.write("Monthly units %s \n"%z)
f.write("Total bill %s \n"%total_bill)
f.close()