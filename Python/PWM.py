row= int(input("enter no of row & col, it nXn square matrix"))
per= int(input("enter % of how many 0s you want"))
col = row
NoOfZero = (int((per*row)/100))
for i in range(col):
    print('')    
    for i in range(NoOfZero):
        print("_",end='')
    NoOfOnes=(row-NoOfZero)
    for i in range(NoOfOnes):
        print("-",end='')