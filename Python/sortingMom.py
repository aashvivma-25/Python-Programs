# Create a 3x3x3 array filled with zeros
Childname =["daria","aashvi","saanvi","janet","aadhira","nikitha"]
ChildAge =[150,14,110,12,50,2]

#for i in range(6):
#   for i in range(6):
#      print( Childname[i])
#      print(ChildAge[i])
for counter1 in range(len(ChildAge)):   
    # print(counter1)   
    for counter2 in range(counter1 , len(ChildAge)):
        if ChildAge[counter1]> ChildAge[counter2]:
            temp=ChildAge[counter1]
            tempName=Childname[counter1]
            ChildAge[counter1] = ChildAge[counter2]
            ChildAge[counter2]=temp
            # print(ChildAge)
            Childname[counter1] = Childname[counter2]
            Childname[counter2]=tempName
            # print(Childname)            
for n in range(len(Childname)):
    print(Childname[n] + " : " + str(ChildAge[n]))