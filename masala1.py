son=input("Son kiriting  ")
lst=[]
for i in son:
    lst.append(int(i))
for i in lst:
    count=0     
    for j in lst:
        if i==j:
            count+=1
    print(i,count)

#print(lst.sort())