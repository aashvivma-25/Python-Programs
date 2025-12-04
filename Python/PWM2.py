row= int(input("enter no of row & col, it nXn square matrix great than 10 \n"))
if row < 100:
    row = 100
per= int(input("enter % of how many 0s you want\n"))
col = row
NoOfZero = (int((per*row)/100))
for i in range(col):
    #print("")
    print(" ",end='')   
    for i in range(NoOfZero):
        print("_",end='')
    NoOfOnes=(row-NoOfZero)
    for i in range(NoOfOnes):
        print("-",end='')