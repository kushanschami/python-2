a=0
marks=[]
f=open("marks.txt","w")
print("Enter -1 to stop")
while True:
    x=int(input("Enter index number:"))
    if x!=-1:
        y=input("Enter marks:")
        marks1=y.split(",")
        for i in marks1:
            i=int(i)
            marks.append(i)
        f.write("Index_no_%s"%x)
        f.write(",mark_%s"%x)
        f.write("%s"%marks[a])

        f.write(",mark_%s"%x)
        f.write("%s"%marks[a+1])

        f.write(",mark_%s"%x)
        f.write("%s\n"%marks[a+2])

        a=a+3
    else:
        break
f.close()    
