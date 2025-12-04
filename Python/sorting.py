# Create a 3x3x3 array filled with zeros
Childname =["daria:","aashvi","saanvi:","janet:","aadhira:","nikitha:"]
ChildAge =[150,14,110,12,50,2]

#for i in range(6):
#   for i in range(6):
#      print( Childname[i])
#      print(ChildAge[i])
for lpc in range(6):      
    for loc in range(lpc , 6):
        if ChildAge[lpc]> ChildAge[loc]:
            temp=ChildAge[lpc]
            ChildAge[lpc] = ChildAge[loc]
            ChildAge[loc]=temp
            print(ChildAge)