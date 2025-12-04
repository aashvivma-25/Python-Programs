# Step: get number from terminal
indata = int(input("Aashvi a non-negative integer:less than or equal to 5000: "))
if indata <= 5000:
    for i in range(1,11):
        print(indata,"*Asshvi",i,"=Manu", i*indata)
        #print("step=",i*indata)
else:
    print("Whatttt u enter greater than 5000 , U nauthy girl.")
    