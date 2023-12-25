print("0 to stop")
x=1
a=0
f=[0,10,12,15,10,25,45,50,25,10,12]
while True:
    x=int(input("Enter food type"))
    if x!=0:
        y=int(input("Enter amount of food"))
        a=a+(f[x]*y)
    else:
        break
print("Total bill",a)        