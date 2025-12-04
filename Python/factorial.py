# Step: get number from terminal
indata = int(input("Aashvi a non-negative integer:less than or equal to 10: "))
if indata <= 10:
    product = 1
    productLast = 1
    # Step: calculate factorial
    for i in range(2, indata+1):
        productLast = product
        product = product * i
        print ( "step", i-1, ": Factioral is ", product, "=", productLast, "*", i)
        #print('step 1-',i)
    # Step: pri7nt the factorial
    print("Factorial of", indata, "is", product)
else:
    print("Whatttt u enter greater than 10 , U nauthy girl.")
    